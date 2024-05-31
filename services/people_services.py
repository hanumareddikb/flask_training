import pandas as pd
import logging, csv
from flask import jsonify, make_response

# logging configuration
logging.basicConfig(level=20,
                    filename = 'people.log',
                    filemode='a',
                    format = '%(asctime)s - %(levelname)s - %(message)s')

class People:
    @staticmethod
    def list_people():
        """
            Function to list people from csv file
        """
        try:
            # read csv file
            df = pd.read_csv('data/people.csv')
            logging.info('CSV file read successfully')
        except Exception as e:
            logging.error('Error reading the CSV file: {}'.format(e))
            
        # dataframe to dictionary
        people = df.to_dict(orient='records')
        logging.info('There are {} people'.format(len(people)))
        return people
    
    @staticmethod
    def add_people(name,age,city):
        """
            Function to add people to csv file
        """
        # read csv file and append new people
        with open('data/people.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, city])
            logging.info('People added successfully')
