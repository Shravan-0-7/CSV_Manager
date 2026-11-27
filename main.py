
import pandas as pd
import os
import sys

print("File Operation Started")

# Loading CSV File

while True: 
     
    fname = input("Enter the CSV file name for operations: ")

    if os.path.exists(fname):
        try:
            df = pd.read_csv(fname, index_col="Name")
            df_backup = df.copy()

            print(f"\nSUCCESS: File '{fname}' loaded with {len(df)} rows.")
            print("'Name' is set as the index.")
            break

        except Exception as e:
            print(f"ERROR: Unable to read file. Details: {e}")
            sys.exit(1)

    else:
        print(f"ERROR: File '{fname}' not found. Please try again.")


# Main Menu

while True:

    print("\nEnter the operation to be performed:")
    print("1: Cleaning | 2: Searching | 3: Replace")
    print("4: Display | 5: Restore Backup | 6: Exit")

    try:
        ch = int(input("Choice: "))  
    except ValueError:
        print("ERROR: Please enter a valid number (1-6).")
        continue

    if ch == 6:
        print("\nExiting program. Goodbye! 👋")
        break

    if ch == 1:

        # Cleaning Operations

        print("\nAvailable columns:", ", ".join(df.columns))

        try:
            op = int(input(
                "1: Delete rows with missing value\n"
                "2: Delete a column\n"
                "Choice: "
            ))
        except ValueError:
            print("ERROR: Invalid cleaning choice.")
            continue

        if op == 1:

            colname = input("Enter the column name to search for missing values: ")

            try:
                before = len(df)
                df = df.dropna(subset=[colname])
                deleted = before - len(df)

                print(f"SUCCESS: {deleted} row(s) deleted from '{colname}'.")

            except KeyError:
                print(f"ERROR: Column '{colname}' not found.")

            except Exception as e:
                print(f"Unexpected error: {e}")

        elif op == 2:

            colname = input("Enter the column name to delete: ")

            try:
                df = df.drop(columns=[colname])
                print(f"SUCCESS: Column '{colname}' deleted!")

            except KeyError:
                print(f"ERROR: Column '{colname}' not found.")

            except Exception as e:
                print(f"Unexpected error: {e}")

        else:
            print("Invalid cleaning operation choice.")


    elif ch == 2:

        # Searching Operations
        print("\nSearch Options:")
        print("1: Search by index (Name)")
        print("2: Search across all columns")
        try:
            s_choice = int(input("Choice: "))
        except ValueError:
            print("ERROR: Invalid search choice.")
            continue

        if s_choice == 1:

            key = input("Enter the name of the record (index) to be searched: ")

            try:
                result = df.loc[key]

                print("-" * 30)
                print(f"Search Result for '{key}':")
                print(result)
                print("-" * 30)

            except KeyError:
                print(f"ERROR: Record '{key}' not found.")

        elif s_choice == 2:

            term = input("Enter the term to search for: ")

            results = df[
                df.apply(
                    lambda row: row.astype(str).str.contains(
                        term, case=False
                    ).any(),
                    axis=1
                )
            ]

            if not results.empty:
                print("\nSearch Results:")
                print(results)
            else:
                print("No matching records found.")

        else:
            print("Invalid search choice.")


    elif ch == 3:

        # Replace Operation

        print("\nAvailable columns:", ", ".join(df.columns))
        colname = input("Enter the column name to operate on: ")

        try:
            old = input("Enter the old value to be replaced: ")
            new = input(f"Enter the new value for '{old}': ")

            count = (df[colname] == old).sum()
            df[colname] = df[colname].replace({old: new})

            print(
                f"SUCCESS: {count} instance(s) of '{old}' "
                f"replaced with '{new}' in column '{colname}'."
            )

        except KeyError:
            print(f"ERROR: Column '{colname}' not found.")

        except Exception as e:
            print(f"Unexpected error: {e}")


    elif ch == 4:

        # Display Operation

        try:
            cho = int(input(
                "1: Display Entire data\n"
                "2: Display chunks (default view)\n"
                "Choice: "
            ))
        except ValueError:
            print("ERROR: Invalid display choice.")
            continue

        if cho == 1:

            print("-" * 50)
            print("Entire DataFrame:")
            print(df.to_string())
            print("-" * 50)

        elif cho == 2:

            print("-" * 50)
            print("DataFrame (Head/Tail View):")
            print(df)
            print("-" * 50)

        else:
            print("Invalid display choice.")


    elif ch == 5:
        # Restore Backup
        df = df_backup.copy()
        print("\nBackup restored successfully!")


    else:
        print(f"ERROR: Choice '{ch}' is not valid (1-6).")


    # Saving Changes

    save = input("\nDo you want to save changes to file? (y/n): ").lower()

    if save == 'y':

        try:
            df.to_csv(fname)
            print(f"SUCCESS: Changes saved to '{fname}'.")

        except Exception as e:
            print(f"ERROR: Failed to save file. Details: {e}")
