import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
print(df)

# Add 'overweight' column
# Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing
# their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight.
# Use the value 0 for NOT overweight and the value 1 for overweight.

overweight = df['weight']/(df['height']*df['height']/10000)

df['overweight'] = overweight > 25

df.replace({False: 0, True: 1}, inplace=True)

print(df["overweight"])



# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    fig = None

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

if __name__ == "__main__":
    pass

