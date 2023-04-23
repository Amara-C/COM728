import matplotlib.pyplot as plt 
import pandas as pd
import tui
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
