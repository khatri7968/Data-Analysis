import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot Use matplotlib to create a scatter plot using the Year column as the x - axis and the
    # CSIRO Adjusted Sea Level column as the y-axis.
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit.
    # Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to
    # predict the sea level rise in 2050.
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = np.arange(1880, 2051, 1)

    line = [slope * xi + intercept for xi in years_extended]

    plt.plot(years_extended, line, color='orange', label="Fitting Line", linewidth=1)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=5, marker='.', label="Sample Point", color='dodgerblue')
    plt.xticks(range(2014, 2051, 2))

    # Create second line of best fit

    new_df = df.loc[df['Year'] >= 2000]

    extended_years = range(2000, 2051)

    line = [slope * xi + intercept for xi in extended_years]

    plt.plot(extended_years, line, color='red', label="Fitting Line", linewidth=1)
    plt.scatter(new_df['Year'], new_df['CSIRO Adjusted Sea Level'], s=5, marker='.', label="Sample Point", color='dodgerblue')
    plt.xticks(range(2014, 2051, 2))

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == "__main__":
    print(draw_plot())