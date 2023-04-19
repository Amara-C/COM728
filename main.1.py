import tui
import process
import os
import csv


# Define the load csv file function
def load_csv_file():
    tui.welcome()
    # Prompt user to enter file name without adding .csv
    file_name = input("Enter the file name: ")
    file_path = './'

    file_path = os.path.join(file_path, file_name)
    # Check if file exists
    if not os.path.isfile(file_path):
        print("File not found, please enter the correct file name")
    else:
        print(f"successfully loaded {file_name} ")

        try:

            # Load data from CSV file into memory
            with open(file_path, "r", encoding="utf-8") as csvfile:
                csv.reader(csvfile)
                # Return the file name if it is found
                return file_path

        #     print the try except block error message
        except IOError:
            print("Error reading file")


def main():
    file_path = load_csv_file()
    if not file_path:
        return

    while True:
        tui.show_menu()
        selection = input("Enter your option: ").strip()

        if selection == "1":
            while True:
                tui.show_csv_menu()
                csv_selection = input("Enter your option: ").strip()

                if csv_selection == "1":
                    host_id = input("Enter the host ID: ")
                    # print the result
                    result = process.get_host_id(file_path, host_id)
                    print(result)
                    tui.press_enter_to_continue()

                elif csv_selection == "2":
                    location = input("Enter location").strip()
                    result = process.get_location(file_path, location)
                    print(result)
                    tui.press_enter_to_continue()

                elif csv_selection == "3":
                    property_type = input("Please enter the property type: ").strip()
                    result = process.get_property_type(file_path, property_type)
                    print(result)
                    tui.press_enter_to_continue()

                elif csv_selection == "4":
                    host_location = input("Enter a location: ").lower()
                    result = process.random_hosts(file_path, host_location)
                    print(result)
                    tui.press_enter_to_continue()

                elif csv_selection == "5":
                    break

                else:
                    tui.error("Invalid option, please select a valid option")

        # elif selection == "2":
        #     while True:
        #         show_df_menu()
        #         df_selection = input("Enter your option: ").strip()
        #
        #         if df_selection == "1":
        #             top_amenities = int(input(f"Enter the number of top amenities you want to see: "))
        #             result = process_data.top_n_amenities(top_amenities)
        #             print(result)
        #             press_enter_to_continue()
        #
        #         elif df_selection == "2":
        #             result = process_data.average_price()
        #             print(result)
        #             press_enter_to_continue()
        #
        #         elif df_selection == "3":
        #             result = process_data.average_review()
        #             print(result)
        #             press_enter_to_continue()
        #
        #         elif df_selection == "4":
        #             result = process_data.average_response()
        #             print(result)
        #             press_enter_to_continue()
        #
        #         elif df_selection == "5":
        #             break
        #
        #         else:
        #             error
