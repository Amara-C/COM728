import csv
import random
import tui

# Define the get host id function
def get_host_id(file_name):

    # repeatedly ask user to enter the host id until an integer is entered
    while True:
        try:
            host_id = int(input("Please enter the host ID you would like to retrieve: "))
            break
        except ValueError:
            print("Invalid input! Please enter numeral values.")

    # initialize row data dictionary to empty
    row_data = {}

    # including the try except block to handle errors
    try:
        # open the file in read mode
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            # create a CSV reader object
            csv_reader = csv.reader(csv_file)

            # loop through each row in the CSV file
            for row in csv_reader:
                
                # check if the host ID matches with the given ID
                if row[0] == str(host_id):
                    # if a match is found, create a dictionary with required data
                    row_data = {
                        "Name": row[1],
                        "Host_Name": row[3],
                        "Description": row[2],
                        "Host_Location": row[5],
                        "Host_Since": row[4]
                    }
                    break

            # check if the row data is empty
            if not row_data:
                print(f"Invalid! The ID '{host_id}' cannot be found. Please enter the correct host ID.")

    except FileNotFoundError:
        # handle the file not found error
        print(f"Invalid! The ID '{host_id}' cannot be found. Please enter the correct host ID.")
    except Exception as e:

        # handle other exceptions

        print(f"An error occurred while processing the file: {e}")

    # print the result
    return row_data

def get_location(file_name):
    # Prompt user to enter location
    location = input("Enter location: ").lower()

    try:
        # Open CSV file and read data
        with open(file_name, mode='r', encoding='utf-8', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Initialize a counter for matching rows
            match_count = 0

            # Create list to hold data for each matching row
            data_list = []

            # Loop through each row and retrieve data for specified location
            for row in csv_reader:
                if row[5].lower() == location:
                    host_name = row[3]
                    property_type = row[13]
                    price = row[20]
                    minimum_nights = row[21]
                    maximum_nights = row[22]

                    # Add retrieved data for each matching row to data list
                    data_list.append([host_name, property_type, price, minimum_nights, maximum_nights])

                    match_count += 1

            # Check if no matching rows were found
            if match_count == 0:
                print(f"No matching rows found for location: {location}")
            else:
                # Print data in ASCII table format
                print(f"| {'Host Name':<30} | {'Property Type':<20} | {'Price':<10} | {'Minimum Nights':<15} | {'Maximum Nights':<15} |")
                print("-" *100 )
                for data_row in data_list:
                    print(f"| {data_row[0]:<30} | {data_row[1]:<20} | {data_row[2]:<10} | {data_row[3]:<15} | {data_row[4]:<15} |")

    except FileNotFoundError:
        # handle the file not found error
        print(f"Invalid! The file '{file_name}' cannot be found.")
    except Exception as e:
        # handle other exceptions
        print(f"An error occurred while processing the file: {e}")


def get_property_type(file_name):

    # ask user to enter the property type
    property_type = input("Please enter the property type: ").lower()

    # initialize row data list to empty
    row_data = []

    # including the try except block to handle errors
    try:
        # open the file in read mode
        with open(file_name, 'r', encoding='utf-8', newline='') as csv_file:
            # create a CSV reader object
            csv_reader = csv.reader(csv_file)

            # loop through each row in the CSV file
            for row in csv_reader:
                # check if property type matches with the given property type
                if row[13].lower() == property_type:
                    # if a match is found, append the row to the row_data list
                    row_data.append(row)

            # check if the row data is empty
            if not row_data:
                print(f"Invalid! The property type '{property_type}' cannot be found. Please enter the correct property type.")
            else:
                # print the row data
                for row in row_data:
                    Room_Type = row[14]
                    Accommodates = row[15]
                    Bathrooms = row[16]
                    Bedrooms = row[17]
                    Beds = row[18]
                    print(f"Room Type: {Room_Type}, Accommodates: {Accommodates}, Bathrooms: {Bathrooms}, Bedrooms: {Bedrooms}, Beds: {Beds}")

    except FileNotFoundError:
        # handle the file not found error
        print(f"Invalid! The property type '{property_type}' cannot be found. Please enter the correct property type.")
    except Exception as e:
        # handle other exceptions
        print(f"An error occurred while processing the file: {e}")



def random_hosts(file_name):
    # Prompt the user for the location they're interested in
    host_location = input("Enter a location: ").lower()

    # Open the CSV file
    with open(file_name, 'r', encoding='utf-8', newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)

        # Skip the header row
        next(reader)

        # Create an empty list to hold the hosts in the specified location
        hosts_in_location = []

        # Loop through each row in the CSV file
        for row in reader:
            # Check if the row represents a host in the specified location
            if row[5].lower() == host_location:
                # If so, add it to the hosts_in_location list
                hosts_in_location.append(row)

        # If there are no hosts in the specified location, let the user know and exit
        if len(hosts_in_location) == 0:
            print("Sorry, there are no hosts in that location.")
            exit()

        # Sort the hosts in the specified location by their review_scores_rating
        hosts_in_location.sort(key=lambda x: float(x[27]), reverse=True)

        # Select 5 random hosts from the top-rated hosts
        top_rated_hosts = [host for host in hosts_in_location if float(host[27]) == float(hosts_in_location[0][27])]
        selected_hosts = random.sample(top_rated_hosts, k=5)

        # Display specific columns from the selected hosts
        print(f"Here are the details of the randomly selected top rated hosts from {host_location}:")
        for host in selected_hosts:
            print("Host Name: {}".format(host[3]))
            print("Total Listings: {}".format(host[10]))
            print("Number of Reviews: {}".format(host[24]))
            print("Review Scores Rating: {}".format(host[27]))
            print()
        

 