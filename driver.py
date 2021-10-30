from os import stat
import pandas
from CSVParser import CSVParser
from Hospital import Hospital
from Treatment import Treatment

class Driver:
    def __init__(self):
        self.hospital_list = []
        self.hospital_dataset = ''
        self.prices_dataset = ''
        self.concepts_dataset = ''

    @staticmethod
    def create_hospital_object(hospital_row):
        h = Hospital(hospital_row['hospital_id'], hospital_row['hospital_name'])
        h.city = hospital_row['city']
        h.state = hospital_row['state']

        return h

    @staticmethod
    def create_hospital_list(hospital_dataset):
        hospitals = CSVParser.readfile_to_dict(hospital_dataset)
        
        hospital_object_list = []
        for h in hospitals:
            hospital = driver.create_hospital_object(h)
            hospital_object_list.append(hospital)

        return hospital_object_list

    @staticmethod
    def add_treatment_price_data_to_hospitals(price_dataset):
        treatments = CSVParser.readfile_to_dict(price_dataset)

        # add logic to map all price data to treatment ids belonging to each hospital
        

    def add_treatment_data_to_hospitals(treatment_dataset):

         # add logic to map all concept ids to hospital ids
        pass



if __name__ == '__main__':
    
    driver = Driver()
    
    # add proper path checking and move these values to config 
    driver.hospital_dataset = 'data/hospital.csv'
    driver.prices_dataset = 'data/price.csv'
    driver.concepts_dataset = 'data/concept.csv'

    hospital_list = driver.create_hospital_list(driver.hospital_dataset)
