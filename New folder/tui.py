#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

LINE_WIDTH = 100

def welcome():
    output = f"Operation started...."
    dashes = "=" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")


def start(msg = "Welcome to Amarachi's Airbnb 2022 Exploratory Data Analysis"):
    output = f"Operation started: {msg}..."
    dashes = "=" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")
    
    
def load_data():
    dashes = "=" * LINE_WIDTH
    print(f"{dashes}\n")
    
    
def completed():
    dashes = "=" * LINE_WIDTH
    print(f"\n{dashes}\nOperation Completed.\n{dashes}\n")

def error(msg):
    print(f"Error! {msg}\n")

def clear_console():
    """Clear the console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(header_text):
    """Print header text with underline"""
    print(header_text)
    print("=" * len(header_text))

def press_enter_to_continue():
    """Pause and wait for user to press enter"""
    input("\nPress Enter to continue...")
    
    
def go_back():
    if current_menu == 'csv':
        show_csv_menu()
    elif current_menu == 'df':
        show_df_menu()
    elif current_menu == 'visualization':
        show_visualization_menu()
    else:
        print("Invalid menu")



def show_menu():
        print("""
        Please select the option to explore:
        1. Csv Exploration
        2. Pandas Exploration
        3. plot visualization
        4. Exit
        """)
#         selection = input("Select your option: ").strip()
        

def show_csv_menu():
    print("""
    Please select one of the following options:
    1. Get a listing name by host ID
    2. Get a host name by location
    3. Get data by property type
    4. Get host data by location
    5. Back to main menu
    """)
    
    
def show_df_menu():
            print("""
            Please select one of the following options:
            1. Show most popular amenities
            2. Show average price for each location
            3. Show average review score rating for each location
            4. Show special selection
            5. Back to main menu
            """)
        
                       
def show_visualization_menu():
        print("""
        Please select one of the following options:
        1. Show the proportion of number of bedrooms
        2. Show the number of listings for each room type
        3. Show the relationship between accommodation and price
        4. Show the Airbnb prices from 2019 to 2022
        5. Show the review score ratings and average price
        6. Back to main menu
        """)

