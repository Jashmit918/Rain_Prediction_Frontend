import matplotlib
matplotlib.use('Agg')  # Set backend before importing pyplot
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_graphs():
    # List to hold base64 strings of each graph
    graphs = []

    #  import the csv
    df = pd.read_csv("cleaned_data.csv")

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')

    # 1st graph(2008 rainfall overall)
    df_2008 = df[df['Date'].dt.year == 2008]
    fig = plt.figure(figsize=(6, 4))
    plt.bar(df_2008['Date'], df_2008['Rainfall'])
    plt.title('2008 Rainfall Overall Data')
    plt.xlabel('Month')
    plt.ylabel('Rainfall(in mm)')

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    # 2nd Graph
    #Extract Month for knowing the average min and max temperature
    df_2008["Month"] = df_2008["Date"].dt.month
    monthly_avg_min = df_2008.groupby(['Month'])['MinTemp'].mean().reset_index()
    monthly_avg_max = df_2008.groupby(['Month'])['MaxTemp'].mean().reset_index()
    newdf2008 = pd.merge(monthly_avg_min, monthly_avg_max, on='Month')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = newdf2008["Month"]
    bar_width = 0.35
    ax.bar(x - bar_width/2, newdf2008["MinTemp"], width=bar_width, label="MinTemp", color='skyblue')
    ax.bar(x + bar_width/2, newdf2008["MaxTemp"], width=bar_width, label="MaxTemp", color='salmon')

    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Monthly Min and Max Temperatures of Year 2008")
    ax.set_xticks(newdf2008["Month"])
    ax.legend()
    plt.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    # 3rd Graph(2009 rainfall overall)
    df_2009 = df[df['Date'].dt.year == 2009]
    fig = plt.figure(figsize=(6, 4))
    plt.bar(df_2009['Date'], df_2009['Rainfall'])
    plt.title('2009 Rainfall Overall Data')
    plt.xlabel('Month')
    plt.ylabel('Rainfall(in mm)')
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    # 4th Graph
    #Extract Month for knowing the average min and max temperature
    df_2009["Month"] = df_2009["Date"].dt.month
    monthly_avg_min = df_2009.groupby(['Month'])['MinTemp'].mean().reset_index()
    monthly_avg_max = df_2009.groupby(['Month'])['MaxTemp'].mean().reset_index()
    newdf2009 = pd.merge(monthly_avg_min, monthly_avg_max, on='Month')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = newdf2009["Month"]
    bar_width = 0.35
    ax.bar(x - bar_width/2, newdf2009["MinTemp"], width=bar_width, label="MinTemp", color='skyblue')
    ax.bar(x + bar_width/2, newdf2009["MaxTemp"], width=bar_width, label="MaxTemp", color='salmon')

    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Monthly Min and Max Temperatures of Year 2009")
    ax.set_xticks(newdf2009["Month"])
    ax.legend()
    plt.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    
    # 5th Graph(2010 rainfall overall)
    df_2010 = df[df['Date'].dt.year == 2010]
    fig = plt.figure(figsize=(6, 4))
    plt.bar(df_2010['Date'], df_2010['Rainfall'])
    plt.title('2010 Rainfall Overall Data')
    plt.xlabel('Month')
    plt.ylabel('Rainfall(in mm)')
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    # 6th Graph
    #Extract Month for knowing the average min and max temperature
    df_2010["Month"] = df_2010["Date"].dt.month
    monthly_avg_min = df_2010.groupby(['Month'])['MinTemp'].mean().reset_index()
    monthly_avg_max = df_2010.groupby(['Month'])['MaxTemp'].mean().reset_index()
    newdf2010 = pd.merge(monthly_avg_min, monthly_avg_max, on='Month')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = newdf2010["Month"]
    bar_width = 0.35
    ax.bar(x - bar_width/2, newdf2010["MinTemp"], width=bar_width, label="MinTemp", color='skyblue')
    ax.bar(x + bar_width/2, newdf2010["MaxTemp"], width=bar_width, label="MaxTemp", color='salmon')

    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Monthly Min and Max Temperatures of Year 2010")
    ax.set_xticks(newdf2010["Month"])
    ax.legend()
    plt.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))


    # 7th Graph(2008 Evaporation Overall)
    df_2008 = df[df['Date'].dt.year == 2008]
    fig = plt.figure(figsize=(6, 4))
    plt.bar(df_2008['Date'], df_2008['Evaporation'])
    plt.title('2008 Evaporation Overall Data')
    plt.xlabel('Month')
    plt.ylabel('Evaporation(in mm)')
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    # 8th Graph(2008 Sunshine Overall)
    df_2008 = df[df['Date'].dt.year == 2008]
    fig = plt.figure(figsize=(6, 4))
    plt.bar(df_2008['Date'], df_2008['Sunshine'])
    plt.title('2008 Sunshine Overall Data')
    plt.xlabel('Month')
    plt.ylabel('Sunshine(in hours)')
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    # 9th Graph(2008 WindGustSpeed Overall)
    df_2008 = df[df['Date'].dt.year == 2008]
    fig = plt.figure(figsize=(6, 4))
    plt.bar(df_2008['Date'], df_2008['WindGustSpeed'])
    plt.title('2008 WindGustSpeed Overall Data')
    plt.xlabel('Month')
    plt.ylabel('WindGustSpeed(in km/h)')
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    # 10th Graph(2008 WindSpeed9am Overall)
    df_2008 = df[df['Date'].dt.year == 2008]
    fig = plt.figure(figsize=(6, 4))
    plt.bar(df_2008['Date'], df_2008['WindSpeed9am'])
    plt.title('2008 WindSpeed @ 9am Overall Data')
    plt.xlabel('Month')
    plt.ylabel('WindSpeed9am(in km/h)')
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150)
    plt.close(fig)
    graphs.append(base64.b64encode(buf.getvalue()).decode('utf-8'))

    #SEND TO HTML
    return render_template('index.html', graphs=graphs)

if __name__ == '__main__':
    app.run(debug=True)