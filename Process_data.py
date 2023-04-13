#!/usr/bin/env python
# coding: utf-8

# # Part A

# # 1. Load  data from a CSV file into memory using the CSV module

# In[11]:


import csv
import os
import random

# Defint the load csv file function
def load_csv_file():
    # Prompt user to enter file name
    file_name = input("Enter the file name: ").lower() + '.csv'

    # Check if file exists
    if not os.path.isfile(file_name):
        print("File not found, please enter the correct file name")
    else:
    #     the try except block error handling
        try:
            # Load data from CSV file into memory
            with open(file_name, "r", encoding="utf-8") as csvfile:
                csvreader = csv.reader(csvfile)
                # Return the file name if it is found
                return file_name


    #     print the try except block error message    
        except IOError:
            print("Error reading file")

# Call the load csv file function and store the result in the file_name variable
file_name = load_csv_file()


# # 2. Retrieve a name of listing for an individual host by host_id

# In[12]:


# Define the get host id function
def get_host_id(file_name):
    

    # ask user to enter the host id
    host_id = input("Please enter the host ID you would like to retrieve: ")

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
                if row[0] == host_id:
                    # if a match is found, create a dictionary with required data
                    row_data = {
                        'Name': row[1],
                        'Host_Name': row[3],
                        'Description': row[2],
                        'Host_Location': row[5],
                        'Host_Since': row[4]
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
    print(row_data)
# Call the get host id function
get_host_id(file_name)


# # 3. Retrieve host_name and other info of all listing for a specified location

# In[13]:


def get_location(file_name):
    # Prompt user to enter location
    location = input("Enter location: ").lower()

    try:
        # Open CSV file and read data
        with open(file_name, mode='r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader) # Skip header row

            # Initialize a counter for matching rows
            match_count = 0

            # Loop through each row and retrieve data for specified location
            for row in reader:
                if row[5].lower() == location:
                    host_name = row[3]
                    property_type = row[13]
                    price = row[20]
                    minimum_nights = row[21]
                    maximum_nights = row[22]

                    # Print retrieved data for each matching row
                    print(f"Host Name: {host_name}\nProperty Type: {property_type}\nPrice: {price}\nMinimum Nights: {minimum_nights}\nMaximum Nights: {maximum_nights}\n")

                    match_count += 1

            # Check if no matching rows were found
            if match_count == 0:
                print(f"No matching rows found for location: {location}")

    except FileNotFoundError:
        # handle the file not found error
        print(f"Invalid! The file '{file_name}' cannot be found.")
    except Exception as e:
        # handle other exceptions
        print(f"An error occurred while processing the file: {e}")

# Call the function and pass the file name as an argument
get_location(file_name)


# # 4. Retrieve room_type and other info of all listing for a specified property type
# 

# In[14]:



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


# call the get_property_type function
get_property_type(file_name)


# # 5. Randomly retrieve some details of hosts with highest review score rating by location

# In[28]:



import random

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
        print("Here are the details of the randomly selected top rated hosts:")
        for host in selected_hosts:
            print("Host Name: {}".format(host[3]))
            print("Total Listings: {}".format(host[10]))
            print("Number of Reviews: {}".format(host[24]))
            print("Review Scores Rating: {}".format(host[27]))
            print()
        
random_hosts(file_name)


# # Part B

# # 1. Load data from a CSV file into memory using the pandas module

# In[40]:


# Define the load pd function
def load_pd():
    import pandas as pd
    import os

    # Prompt user to enter file name
    file_name = input("Enter the file name: ").lower() + '.csv'

    # Check if file exists
    if not os.path.isfile(file_name):
        print("File not found, please enter the correct file name")
    else:
    # the try except block
        try:
            # Load CSV file into a pandas DataFrame
            df = pd.read_csv(file_name)
            return df
        except csv.Error:
            # Handle errors that occur while reading the CSV file
            print("An error occurred while reading the file")
df= load_pd()


# # 2. Identifying the most popular  top amenities

# In[43]:


# Define the top_n_amenities function
def top_n_amenities():
    # Prompt user to enter the number of top amenities they want to see
    top_amenities = int(input(f"Enter the number of top amenities you want to see: "))

    # Create a dictionary to store the counts of each amenity
    amenities_counts = {}

    # Loop through each row of the 'amenities' column
    for amenities_list in df['amenities']:
        # Remove special characters from the amenities string
        amenities = amenities_list.replace('[', '').replace(']', '').replace('"', '').replace("'", "").replace(" ", "").split(',')
        # Loop through each amenity and add it to the counts dictionary
        for amenity in amenities:
            if amenity in amenities_counts:
                amenities_counts[amenity] += 1
            else:
                amenities_counts[amenity] = 1

    # Sort the amenities by count in descending order
    sorted_amenities = sorted(amenities_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the top n amenities as specified by the user
    print(f"Top {top_amenities} amenities:")
    for i in range(top_amenities):
        print(f"{i+1}. {sorted_amenities[i][0]}: {sorted_amenities[i][1]}")

# Call the top_n_amenities function
top_n_amenities()


# # 3. Analysing the average price of stay in each location

# In[51]:


# Define the average price function

def average_price(df):
    # Prompt user to enter location
    location = input("Enter location: ").lower()

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

# call the average price function 
average_price(df)


# # 4. Analysing the average review scores rating for each location

# In[52]:


# Define the average review function
def average_review(df):
    # Get input from user for the location
    location = input("Enter the location for which you want to calculate the average review scores rating: ").lower()

    # Filter the data for the specified location
    location_df = df[df['host_location'].str.lower() == location]

    # Calculate the mean of review_scores_rating for the specified location
    avg_rating = location_df['review_scores_rating'].mean()

    # Print the average review scores rating for the specified location
    print(f"Average review scores rating for {location.capitalize()} is: {avg_rating:.1f}")

# call the average review function
average_review(df)


# # Redo analysis

# In[9]:


# Define the random selection function
def random_selection(df):
    # Get user input for number of hosts to randomly select
    num_hosts = int(input("Enter the number of hosts to be randomly selected: "))

    # Randomly select hosts and their listing titles
    random_hosts = df.sample(n=num_hosts)
    print(f"Randomly selected {num_hosts} hosts and their listing titles:")
    for index, host in random_hosts.iterrows():
        print(f"- Host: {host['host_name']},   Name: {host['name']},   Bedrooms: {host['bedrooms']}, Price: {host['price']},  Reviews: {host['number_of_reviews']}")

# Call the random selection function
random_selection(df)


# # Part C

# # 1. Proportion of number of bedrooms of Airbnb listing using pie chart
# 

# In[34]:


#printing out the number of counts for each bedroom
bedroom_counts = df['bedrooms'].value_counts().sort_index()
print(bedroom_counts)


# In[63]:


import matplotlib.pyplot as plt  
def bedroom_number():
    fig = plt.figure(figsize=(8, 8))

    bedrooms = ['1', '2', '3', '4', '5', '6', '7', '10']
    count = [df['bedrooms'].eq(1).sum(), df['bedrooms'].eq(2).sum(), 
           df['bedrooms'].eq(3).sum(), df['bedrooms'].eq(4).sum(),
           df['bedrooms'].eq(5).sum(), df['bedrooms'].eq(6).sum(),
           df['bedrooms'].eq(7).sum(), df['bedrooms'].eq(10).sum()]
    
    plt.axis("equal")
    plt.pie(count, labels=bedrooms, autopct='%1.1f%%')
    plt.legend(loc="best",bbox_to_anchor=(1.2,1))
    plt.title('Proportion of Number of Bedrooms in Airbnb Listings')
    plt.show()
bedroom_number()


# # 2 Displaying the number of listings for each room type using bar chart

# In[40]:


# checking the room types and their numbers
room_type_counts = df['room_type'].value_counts().sort_index()
print(room_type_counts)


# In[39]:


def listing_number():
    
    x = ['Hotel room','private room','shared room','home/apt'] # x axis
    y = [1,3010,14,5414] # y axis - height of bar chart

    fig = plt.figure(figsize=(8,8)) 

    plt.bar(x,y, label="Number of listings")# plotting the graph

    plt.xlabel("Room types") # create a label for x-axis
    plt.ylabel("Number of listings") # create a label for y-axis

    plt.title("Number of listings for each room type ") # create a title for your graph 

    plt.legend() # create a legend

    plt.show() # show the graph
    
listing_number()


# # 3. Displaying the r/ship b/w accommodates and price using scatter plot

# In[65]:


#define the relationship function
def relationship():

    plt.scatter(df['accommodates'], df['price'], color = 'teal')
    plt.title('Relationship between Accommodates and Price')
    plt.xlabel('Accommodates')
    plt.ylabel('Price')
    plt.grid(True, linewidth= 1, linestyle="--") 
    plt.show()
relationship()


# # 4. Displaying Airbnb prices from 2019 - 2022 with line chart using subplots
# 

# In[82]:


def prices():

    # convert the host since column to datetime
    df['host_since'] = pd.to_datetime(df['host_since'])

    # filter data by year
    df_2019 = df[df['host_since'].dt.year == 2019]
    df_2020 = df[df['host_since'].dt.year == 2020]
    df_2021 = df[df['host_since'].dt.year == 2021]
    df_2022 = df[df['host_since'].dt.year == 2022]

    # create subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15,10))

    # plot data for each year
    axes[0,0].plot(df_2019['host_since'], df_2019['price'])
    axes[0,0].set_title('Airbnb Prices in 2019')
    axes[0,0].set_xlabel('host_since')
    axes[0,0].set_ylabel('Price')

    axes[0,1].plot(df_2020['host_since'], df_2020['price'])
    axes[0,1].set_title('Airbnb Prices in 2020')
    axes[0,1].set_xlabel('host_since')
    axes[0,1].set_ylabel('Price')

    axes[1,0].plot(df_2021['host_since'], df_2021['price'])
    axes[1,0].set_title('Airbnb Prices in 2021')
    axes[1,0].set_xlabel('host_since')
    axes[1,0].set_ylabel('Price')

    axes[1,1].plot(df_2022['host_since'], df_2022['price'])
    axes[1,1].set_title('Airbnb Prices in 2022')
    axes[1,1].set_xlabel('host_since')
    axes[1,1].set_ylabel('Price')

    plt.tight_layout()
    plt.show()

prices()


# # 5. Displaying the review score ratings and avearge prices

# In[81]:


def review_price():

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

review_price()


# In[ ]:




