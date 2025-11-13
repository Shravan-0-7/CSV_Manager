import pandas as pd
import sys
import os

print("File Operation Started")

# Load file
while True:
    fname = input("Enter the CSV file name for operations: ")
    if not os.path.exists(fname):
        print(f"ERROR: File '{fname}' not found. Please try again.")
        continue
    try:
        df = pd.read_csv(fname, index_col="Name")
        df_backup = df.copy()
        print(f"\nSUCCESS: File '{fname}' loaded with {len(df)} rows. 'Name' is set as the index.")
        break
    except Exception as e:
        print(f"ERROR: Could not read CSV file or 'Name' column is missing. Details: {e}")
        sys.exit(1)

# Menu loop
while True:
    try:
        print("\nEnter the operation to be performed:")
        print("1: Cleaning | 2: Searching | 3: Replace | 4: Display | 5: Restore Backup | 6: Exit")
        ch = int(input("Choice: "))
    except ValueError:
        print("ERROR: Invalid input. Please enter a number (1-6).")
        continue

    if ch == 6:
        print("\nExiting program. Goodbye! 👋")
        break

    match ch:
        case 1:  # Cleaning
            print("\nAvailable columns:", ", ".join(df.columns))
            try:
                op = int(input("How do you want to clean the data?\n1: Delete rows with missing value\n2: Delete a column\nChoice: "))
            except ValueError:
                print("ERROR: Invalid input for cleaning choice. Please enter 1 or 2.")
                continue

            if op == 1:
                colname = input("Enter the column name to search for missing values: ")
                try:
                    rows_before = len(df)
                    df = df.dropna(subset=[colname])
                    deleted_count = rows_before - len(df)
                    print(f"\nSUCCESS: {deleted_count} row(s) deleted based on missing values in column '{colname}'.")
                except KeyError:
                    print(f"ERROR: Column '{colname}' not found.")
                except Exception as e:
                    print(f"Caught an unexpected error during row deletion: {e}")

            elif op == 2:
                colname = input("Enter the column name to delete: ")
                try:
                    df = df.drop(columns=[colname])
                    print(f"\nSUCCESS: Column '{colname}' deleted!")
                except KeyError:
                    print(f"ERROR: Column '{colname}' not found.")
                except Exception as e:
                    print(f"Caught an unexpected error during column deletion: {e}")
            else:
                print("Invalid cleaning operation choice.")

        case 2:  # Searching
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
                    print(f"ERROR: Record with name '{key}' not found.")
            elif s_choice == 2:
                term = input("Enter the term to search for: ")
                results = df[df.apply(lambda row: row.astype(str).str.contains(term, case=False).any(), axis=1)]
                if not results.empty:
                    print("\nSearch Results:")
                    print(results)
                else:
                    print("No matching records found.")
            else:
                print("Invalid search choice.")

        case 3:  # Replace
            print("\nAvailable columns:", ", ".join(df.columns))
            colname = input("Enter the column name to operate on: ")
            try:
                old = input("Enter the old value to be replaced: ")
                new = input(f"Enter the new value for '{old}': ")
                count_replaced = (df[colname] == old).sum()
                df[colname] = df[colname].replace({old: new})
                print(f"\nSUCCESS: {count_replaced} instance(s) of '{old}' replaced with '{new}' in column '{colname}'.")
            except KeyError:
                print(f"ERROR: Column '{colname}' not found.")
            except Exception as e:
                print(f"Caught an unexpected error during replacement: {e}")

        case 4:  # Display
            try:
                cho = int(input("1: Display Entire data\n2: Display chunks (default view)\nChoice: "))
            except ValueError:
                print("ERROR: Invalid input for display choice. Please enter 1 or 2.")
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

        case 5:  # Restore backup
            df = df_backup.copy()
            print("\nBackup restored successfully!")

        case _:  # Invalid input
            print(f"ERROR: Choice '{ch}' is not valid (1-6).")

    # Ask to save changes
    save = input("\nDo you want to save changes to file? (y/n): ").lower()
    if save == 'y':
        try:
            df.to_csv(fname)
            print(f"SUCCESS: Changes saved to '{fname}'.")
        except Exception as e:
            print(f"ERROR: Failed to save file. Details: {e}")