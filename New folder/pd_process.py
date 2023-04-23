
import csv
import pandas as pd
import tui

##PART B


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






def average_price(df, location):
    
    try:
        # Filter the dataframe to include only the specified location
        location_df = df.loc[df['host_location'].str.contains(location, case=False)]

        # Calculate the average price for the specified location
        avg_price = location_df['price'].mean()

        # Print the average price for each location
        print(f"The average price for stays in {location.capitalize()} is £{avg_price:.2f} per night.")

    except KeyError:
        print(f"Error: 'host_location' column not found in dataset. Please check and try again.")

    except ValueError:
        print(f"Error: no data found for location '{location}'. Please check the spelling and try again.")

        
    # Get a list of unique locations in the dataset
    locations = df['host_location'].unique()


    
    

def average_review(df, location):
    
    try:
        # Filter the data for each location
        location_df = df[df['host_location'].str.lower() == location]

        # Calculate the mean of review_scores_rating for the each location
        avg_rating = location_df['review_scores_rating'].mean()

        # Print the average review scores rating for each location
        print(f"Average review scores rating for {location.capitalize()} is: {avg_rating:.1f}")

    except KeyError:
        print(f"Error: 'host_location' or 'review_scores_rating' column not found in dataset. Please check and try again.")

    except ValueError:
        print(f"Error: no data found for location '{location}'. Please check the spelling and try again.")
        

    # Get a list of unique locations in the dataset
    locations = df['host_location'].unique()


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

