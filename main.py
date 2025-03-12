import pandas as pd
import matplotlib.pyplot as plt

def visualize_covid_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Convert date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Plot data
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['TotalConfirmed'], label='Total Confirmed', color='blue')
    plt.plot(df['Date'], df['ActiveCases'], label='Active Cases', color='orange')
    plt.plot(df['Date'], df['TotalDeaths'], label='Total Deaths', color='red')
    
    # Customize plot
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('COVID-19 Trends Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    
    # Show plot
    plt.show()

file_path = 'covid_data.csv'  
visualize_covid_data(file_path)
