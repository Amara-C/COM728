import csv
import random
import os
import pandas as pd
import matplotlib.pyplot as plt
import tui

# Define the load csv file function
def load_csv_file():
    tui.welcome("Welcome to coded codes")
    # Prompt user to enter file name without adding .csv
    file_name = input("Enter the file name: ")
    file_path = 'Airbnb/' 
    
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
    tui.completed()
    # Call the load csv file function and store the result in the file_name variable
file_name =load_csv_file()
