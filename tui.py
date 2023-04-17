import os


LINE_WIDTH = 85

def welcome(msg="Welcome to my coded codes"):
    dashes = "=" * LINE_WIDTH
    output = f"Operation started: {msg}..."
    print(f"{dashes}\n{output}\n")
    
def completed():
    dashes = "=" * LINE_WIDTH
    print(f"\n{dashes}\nOperation Completed.\n{dashes}\n")


    
def show_menu():
    while True:
        print("""
        Please select one of the following options:
        1. File_Processing
        2. Data_Query
        3. Plot_visualization
        4. Exit
        """)