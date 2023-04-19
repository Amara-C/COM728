import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
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
                        "Host_Since": row[4]}
                   
                
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
        
        
##PART B


# 1.Identifying the top 10 most popular amenities or features that Airbnb hosts provide to customers

def top_10_amenities(df):
    try:
        # Create an empty dictionary to store amenities and their counts
        amenities_counts = {}

        # Loop through each amenities list in the 'amenities' column of the dataframe
        for amenities_list in df['amenities']:
            # Clean up the amenities list by removing unnecessary characters and splitting into separate amenities
            amenities = amenities_list.replace('[', '').replace(']', '').replace('"', '').replace("'", "").replace(" ", "").split(',')
            # Loop through each amenity in the cleaned up amenities list
            for amenity in amenities:
                # Increment the count for the amenity in the amenities_counts dictionary
                if amenity in amenities_counts:
                    amenities_counts[amenity] += 1
                # Add the amenity to the amenities_counts dictionary with a count of 1 if it doesn't exist
                else:
                    amenities_counts[amenity] = 1

        # Sort the amenities_counts dictionary items by count in descending order and get the top 10
        top_amenities = sorted(amenities_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        # Print the top 10 amenities with their counts
        print("Top 10 amenities:")
        for i, amenity in enumerate(top_amenities, start=1):
            print(f"{i}. {amenity[0]}: {amenity[1]}")
    
    except KeyError:
        print("Error: 'amenities' column not found in dataset. Please check and try again.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

        
# Define the average price function
def average_price(df):
    
    try:
        

        # Filter the dataframe to include only the specified location
        location_df = df.loc[df['host_location'].str.contains(location, case=False)]

        # Calculate the average price for the specified location
        avg_price = location_df['price'].mean()

        # Print the average price for the specified location
        print(f"The average price for stays in {location.capitalize()} is £{avg_price:.2f} per night.")

    except KeyError:
        print(f"Error: 'host_location' column not found in dataset. Please check and try again.")

    except ValueError:
        print(f"Error: no data found for location '{location}'. Please check the spelling and try again.")
# Read in the dataframe from the CSV file

    # Get a list of unique locations in the dataset
    locations = df['host_location'].unique()


def average_review(df):
    """
    Calculates the average review score for stays in each location.
    
    Parameters:
    df (pandas.DataFrame): The dataframe to be analyzed.
    location (str): The location to filter and calculate the average review score.
    
    Returns:
    None
    """
    try:
        # Filter the data for the specified location
        location_df = df[df['host_location'].str.lower() == location.lower()]

        # Calculate the mean of review_scores_rating for the specified location
        avg_rating = location_df['review_scores_rating'].mean()

        # Print the average review scores rating for the specified location
        print(f"Average review scores rating for {location.capitalize()} is: {avg_rating:.1f}")

    except KeyError:
        print(f"Error: 'host_location' or 'review_scores_rating' column not found in dataset. Please check and try again.")

    except ValueError:
        print(f"Error: no data found for location '{location}'. Please check the spelling and try again.")
        

    # Get a list of unique locations in the dataset
    locations = df['host_location'].str.lower().unique()


def average_response(df):
    try:
        # Filter the dataframe to include only listings with the highest ratings
        highest_ratings = df['review_scores_rating'].max()
        filtered_df = df[df['review_scores_rating'] == highest_ratings].copy()

        # Convert the host_response_rate column to float and divide by 100 to get percentage
        filtered_df['filtered_response_rate'] = filtered_df['host_response_rate'].str.rstrip('%').astype('float') / 100.0

        # Calculate the average filtered response rate for each location
        grouped = filtered_df.groupby('host_location')
        for location, group in grouped:
            avg_response_rate = group['filtered_response_rate'].mean()
            print(f"The average response rate of hosts with the highest ratings in {location} is {avg_response_rate*100:.2f}%")

    except KeyError:
        print(f"Error: 'review_scores_rating', 'host_response_rate' or 'host_location' column not found in dataset. Please check and try again.")

    except ValueError:
        print(f"Error: invalid value found in 'host_response_rate' column. Please check and try again.")


        
# PART C



def bedroom_number(df):
    try:
        
        fig = plt.figure(figsize=(8, 8))

        bedrooms = ['1', '2', '3', '4', '5', '6', '7', '10']
        count = [df['bedrooms'].eq(1).sum(), df['bedrooms'].eq(2).sum(), 
               df['bedrooms'].eq(3).sum(), df['bedrooms'].eq(4).sum(),
               df['bedrooms'].eq(5).sum(), df['bedrooms'].eq(6).sum(),
               df['bedrooms'].eq(7).sum(), df['bedrooms'].eq(10).sum()]

        colors = ['#ffa600', '#ff6e54', '#dd5182', '#955196', '#5e4fa2', '#306998', '#008080', '#0c2c84']
        explode = (0, 0.1, 0, 0, 0, 0, 0, 0)
        wedgeprops = {'linewidth': 1, 'edgecolor': 'white'}

        plt.pie(count, labels=bedrooms, autopct='%1.1f%%', colors=colors,
                startangle=90, explode=explode, shadow=True, wedgeprops=wedgeprops)

        plt.legend(loc="best", bbox_to_anchor=(1.2,1))
        plt.title('Proportion of Number of Bedrooms in Airbnb Listings')
        plt.show()
    except Exception as e:
        print(f"Error occurred: {e}")


def listing_number(df):
    x = ['Hotel room', 'private room', 'shared room', 'home/apt'] # x axis
    y = [1, 3010, 14, 5414] # y axis - height of bar chart

    try:
        
        fig = plt.figure(figsize=(8, 8)) 
        colors = ['#008080', '#c08000', '#a0c080', '#8060c0'] # custom colors
        bars = plt.bar(x, y, color=colors, label="Number of listings") # plotting the graph

        plt.xlabel("Room types") # create a label for x-axis
        plt.ylabel("Number of listings") # create a label for y-axis

        plt.title("Number of listings for each room type") # create a title for your graph 

        plt.legend() # create a legend

        # add numbers above each bar
        for bar in bars:
            height = bar.get_height()
            plt.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                         xytext=(0, 3),  # 3 points vertical offset
                         textcoords="offset points",
                         ha='center', va='bottom')

        plt.show() # show the graph
    except Exception as e:
        print(f"An error occurred: {e}")



def relationship(df):
    try:
        # define custom colors
        colors = ['#008080']

        # create the scatter plot
        plt.scatter(df['accommodates'], df['price'], color=colors, alpha=0.6)

        # set the title and axis labels
        plt.title('Relationship between Accommodates and Price', fontsize=16, fontweight='bold')
        plt.xlabel('Accommodates', fontsize=12, fontweight='bold')
        plt.ylabel('Price', fontsize=12, fontweight='bold')

        # set the tick parameters for the x and y axis
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        # customize the grid lines
        plt.grid(True, linewidth=1, linestyle='--')

        # remove top and right spines
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)

        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def year_prices(df):
    try:
        # Convert host_since column to datetime
        df['host_since'] = pd.to_datetime(df['host_since'])

        # Filter data by year
        year_2019 = df[df['host_since'].dt.year == 2019]
        year_2020 = df[df['host_since'].dt.year == 2020]
        year_2021 = df[df['host_since'].dt.year == 2021]
        year_2022 = df[df['host_since'].dt.year == 2022]

        # Group data by month and sum the prices for each year
        df_2019 = year_2019.groupby(year_2019.host_since.dt.month)["price"].sum()
        df_2020 = year_2020.groupby(year_2020.host_since.dt.month)["price"].sum()
        df_2021 = year_2021.groupby(year_2021.host_since.dt.month)["price"].sum()
        df_2022 = year_2022.groupby(year_2022.host_since.dt.month)["price"].sum()

        # Create subplots
        fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(15,15))

        # Plot data for each year
        axes[0].plot(df_2019.index, df_2019.values, color='blue', linestyle='-', label='2019')
        axes[0].set_title('Airbnb Prices in 2019', fontsize=14)
        axes[0].set_xlabel('2019', fontsize=12)
        axes[0].set_ylabel('Price', fontsize=12)
        axes[0].grid(True)

        axes[1].plot(df_2020.index, df_2020.values, color='red', linestyle='--', label='2020')
        axes[1].set_title('Airbnb Prices in 2020', fontsize=14)
        axes[1].set_xlabel('2020', fontsize=12)
        axes[1].set_ylabel('Price', fontsize=12)
        axes[1].grid(True)

        axes[2].plot(df_2021.index, df_2021.values, color='green', linestyle='-.', label='2021')
        axes[2].set_title('Airbnb Prices in 2021', fontsize=14)
        axes[2].set_xlabel('2021', fontsize=12)
        axes[2].set_ylabel('Price', fontsize=12)
        axes[2].grid(True)

        axes[3].plot(df_2022.index, df_2022.values, color='purple', linestyle=':', label='2022')
        axes[3].set_title('Airbnb Prices in 2022', fontsize=14)
        axes[3].set_xlabel('2022', fontsize=12)
        axes[3].set_ylabel('Price', fontsize=12)
        axes[3].grid(True)

        # Add legend
        axes[3].legend(loc='upper right', fontsize=12)

        # Adjust spacing between subplots
        plt.tight_layout()

    except Exception as e:
        print(f"An error occurred: {e}")

    else:
        # Show plot
        plt.show()
        
        
def review_price(df):
    try:
        # Group the data by review scores rating and calculate the average price
        avg_prices = df.groupby('review_scores_rating')['price'].mean()

        # Create a bar chart of average prices by property type
        fig, ax = plt.subplots(figsize=(10,6))
        ax.bar(avg_prices.index, avg_prices.values)
        ax.set_xlabel('review_scores_rating')
        ax.set_ylabel('Average Price')
        ax.set_title('Average Airbnb Prices by review score rating')
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
