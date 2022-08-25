import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")


# Add 'overweight' column
# Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing
# their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight.
# Use the value 0 for NOT overweight and the value 1 for overweight.

weight = df['weight']/(df['height']*df['height']/10000)

df['overweight'] = weight > 25

df.replace({False: 0, True: 1}, inplace=True)



# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0.
# If the value is more than 1, make the value 1.

df['cholesterol'] = np.where(df['cholesterol'].values > 1, 1, 0)

df['gluc'] = np.where(df['gluc'].values > 1, 1, 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars= ['cholestrol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat["total"] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index =False).count()

    # Draw the catplot with 'sns.catplot()'

    sns.set_theme(style='darkgrid')
    fig = sns.catplot(x="variable", y="total", data=df_cat, hue="value", kind="bar", col='cardio').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

def draw_scatter_plot():
    fig = sns.regplot(x="height", y="weight", hue="active", style="gender", data=df)
    fig.savefig('scatterplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.025))

    ]

    # Calculate the correlation matrix
    corr = df_heat.corr(method="Pearson")

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12,12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt=".1f", center=0.08, cbar_kws={"shrink":0.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

if __name__ == "__main__":
    draw_cat_plot()

