import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df['date'] = pd.to_datetime(df['date'])
t025 = df['value'].quantile(0.025)
b025 = df['value'].quantile(0.975)
df = df[(df['value']>=t025) & (df['value']<=b025)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,5))
    plt.plot(df['date'],df['value'])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar[date]).year
    df_bar['month'] = pd.DatetimeIndex(df_bar[date]).month

    # Draw bar plot
    df_bar = df_bar.groupny(['year','month'])['value'].mean().unstack()
     months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig = df_bar.plot.bar()
    fig.legend(months,title='Months',prop={'size':8})
    fig.xlabel('Years')
    fig.ylabel('Avreage Page Views')
    plt.tight_layout()
    fig = fig.figure




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

