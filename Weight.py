import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# save path of weight csv
weight_save_path = 'Weight.csv'

'''
#create charts
data = {'Date': [datetime(2021, 11, 1), datetime(2021, 11, 8), datetime(2021, 11, 15)], 'Weight': [96.85, 96.25, 95]}
df = pd.DataFrame(data)
df.to_csv(weight_save_path, index=False)
#'''

# update weight csv on current date
def updateChart(update_weight: float):
    # read in data chart
    df = pd.read_csv(weight_save_path, index_col=False)
    
    # read in latest date
    latest_date =  df.iloc[-1]['Date']
    
    # get current date
    current_date = datetime.now().strftime('%Y-%m-%d')
  
    if latest_date != current_date:
        # append row to dataframe
        new_row = {'Date': current_date, 'Weight': update_weight} 
        df = df.append(new_row, ignore_index=True)

        # save new chart
        df.to_csv(weight_save_path, index=False)
        return
    else:
        # update latest index if current date is the as latest date in table
        df.loc[ len(df) - 1, ['Weight'] ] = update_weight

        # save new chart
        df.to_csv(weight_save_path, index=False)
        return 


# display chart from csv file
def displayChart():
    df = pd.read_csv(weight_save_path, index_col=False)
    
    dates = df['Date'].to_list()
    weights = df['Weight'].to_list()
    
    
    
    # store date time objects in list
    datetime_list = []

    # create date time objects from csv dates
    for date in dates:
        # split string into year, month and date integers
        split_date = date.split('-')
        year = int(split_date[0])
        month = int(split_date[1])
        date = int(split_date[2])
        
        datetime_list.append( datetime(year, month, date) )
    
    

    offset = 2.5
    plt.ylim( min(weights)-offset, max(weights)+offset )
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.plot_date(datetime_list, weights, color='green', linestyle=':')
    plt.tick_params(axis='x', rotation=65)
    plt.tight_layout()
    plt.show()


# CLI for adding weight
def addWeight():
    while(1):
        # input weight
        weight = input('Enter current weight in kg: ')

        # check if number is inputted 
        try:
            weight = float(weight)
            updateChart(weight)
            print('Chart updated\n')
            break
        except ValueError:
            print('Invalid input\n')






if __name__ == '__main__':
    while(1):
        option = input()
        
        if option == 'quit' or option == 'add' or option == 'display' or option == 'help':

            if option == 'quit':
                print('Quitting\n')
                exit()

            if option == 'add':
                addWeight()
            
            if option == 'display':
                print('Displaying chart\n')
                displayChart()

            if option == 'help':
                print('quit : exit program \nadd : update weight\ndisplay : display chart\n')
            


        else:
            print('invalid command\n')
        
        
    
    
