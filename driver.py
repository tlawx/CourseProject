from json.encoder import JSONEncoder
from os import stat
import re
from collections import defaultdict, namedtuple
from typing import Dict, NamedTuple
import pandas
from CSVParser import CSVParser
from Hospital import Hospital
from Treatment import Treatment
from Price import Price
import json

class Driver:
    def __init__(self):
        self.hospital_list = []
        self.treatment_list = []
        self.price_dict = {}
        self.categories_dataset = 'data/hcpcs_categories.csv'
        self.hospital_dataset = 'data/hospital.csv'
        self.prices_dataset = 'data/price.csv'
        self.concepts_dataset = 'data/concept.csv'
        self.category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
        self.hospital_index = None
        self.city_dict = {}


    def set_treatment_list(self, treatment_list):
        self.treatment_list = treatment_list

    def set_hospital_list(self, hospital_list):
        self.hospital_list = hospital_list

    def set_city_dict(self, city_dict):
        self.city_dict = city_dict

    def get_treatment_list(self):
        return self.treatment_list

    def get_hospital_list(self):
        return self.hospital_list

    def get_city_dict(self):
        return self.city_dict 
    
    def create_city_dict_of_hopital_list(self):
        """
        Creates dictionary with city (key) and hospital list with the city (value)
        """
        hospitals = CSVParser.readfile_to_dict(self.hospital_dataset)

        city_dict = defaultdict(list)

        for h in hospitals:
            city_dict[re.sub('[^\w\s]'," ",h['city'].lower())].append(h)
 
        return city_dict

    @staticmethod
    def create_hospital_index(hospital_obj_list):
        """
        Creates an hospital index (dict) of hospital_id (keys) and hospital objects (values)
        """
        hospital_index = {}

        for hospital_obj in hospital_obj_list:
            hospital_index[hospital_obj.hospital_id] = hospital_obj

        return hospital_index
    
    
    def create_hospital_dict(self):
        """
        Creates a dict of Treatment objects; concept_id (key) and Treatment_object (value)
        """
        hospitals = CSVParser.readfile_to_dict(self.hospital_dataset)

        hospital_obj_dict = {}

        for h in hospitals:
            hospital_obj_dict[h['hospital_id']] = Hospital(h['hospital_id'], h['hospital_name'], h['hospital_npi'], h['city'], h['state'], h['affiliation'], h['disclosure'])
        
        return hospital_obj_dict


    def create_treatment_dict(self):
        """
        Creates a dict of Treatment objects; concept_id (key) and Treatment_object (value)
        """
        treatments = CSVParser.readfile_to_dict(self.concepts_dataset)

        treatment_obj_dict = {}

        for t in treatments:
            treatment_obj_dict[t['concept_id']] = Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name'])
        
        return treatment_obj_dict

    def create_hospital_list(self, hospital_dataset):
        """
        Creates hospital list
        """
        hospitals = CSVParser.readfile_to_dict(hospital_dataset)
        
        hospital_object_list = []
        for h in hospitals:
            hospital_object_list.append(self.create_hospital_object(h))

        return hospital_object_list

    @staticmethod
    def create_hospital_object(hospital_row):
        """
        Creates hospital objects
        """
        h = Hospital(hospital_row['hospital_id'], hospital_row['hospital_name'], hospital_row['hospital_npi'])
        h.city = hospital_row['city']
        h.state = hospital_row['state']
        return h
    

    def create_hospital_treatment_filtered_dict(self, treatments_list_from_search):
        """
        Creates a dict of dicts of treatment_id (concept_id) keys and a dict value as all matching hospitals for that treatment with value as tuple (hospita, price) objects

        This will only fetch treatments belonging to hospitals in the city parameter using city-hospital index

        output_dict = {
            treatment_id : {
                hospital_id: (hospital_object, price_object),
                hospital_id: (hospital_object, price_object),
                ...
            },
            treatment_id : {
                hospital_id: (hospital_object, price_object),
                hospital_id: (hospital_object, price_object),
                ...
            },
            ...
            ...
        }
        """
        
        # Create a list of hospital objects from hospital dataset enties
        self.hospital_list = self.create_hospital_list(self.hospital_dataset)

        if not self.hospital_index:
            self.hospital_index = self.create_hospital_index(self.hospital_list)

        # This logic is meant for using the city to make sure hospital list is only mapped to selected city
        #hospitals_in_city_list = self.create_city_dict_of_hopital_list()[city]

        # Parse prices dataset that links between treatment/hospital/price columns
        prices = CSVParser.readfile_to_dict(self.prices_dataset)
        
        # Parser concept dataset and generate a dict of objects to later in matching concept_code to concept_id
        treatment_dict = self.create_treatment_dict()
        
        # concept_id_to_concept_code_dict = {}
        # for k, v in treatment_dict.items():
        #     concept_id_to_concept_code_dict[v.concept_id] = v.concept_code

        
        prices_filtered = []
        hospital_id_set = set(self.hospital_index.keys())

        
        for entry in prices:
            # Getting only price entries for hospital IDs in city parameter
            # if entry['hospital_id'] in hospital_id_set:
            #     prices_filtered.append(entry)
            
            # Matching concept code entries with concept id entries
            if entry['concept_id'] in treatment_dict:
                entry['concept_code'] = treatment_dict[entry['concept_id']].concept_code
        

        
        
        # build {treatment_id: {hospital_id: (hospital, price)} dict of dicts
        treatment_hospital = dict()
        d = self.create_treatment_dict() #added this
        for entry in prices:
            treatment_code, hospital_id, price_type, amount, concept_code = entry['concept_id'], entry['hospital_id'], entry['price'], entry['amount'], None
            if 'concept_code' in entry.keys():
                concept_code = entry['concept_code']
            # print(entry)

            # Making sure we are only fetching treatments that match treatment code entries from search output
            if treatment_code in treatments_list_from_search:      
                hospital_obj = self.hospital_index[hospital_id]
                
                if treatment_code not in treatment_hospital.keys():
                    p = Price()
                    p.set_price_amount(price_type.lower(), amount)

                    #treatment_hospital[d[treatment_code].concept_code] = dict()         
                    treatment_hospital[treatment_code] = dict()
                    #treatment_hospital[d[treatment_code].concept_code][hospital_id] = (hospital_obj, p)
                    treatment_hospital[treatment_code][hospital_id] = (hospital_obj, p)
                else:
                    if hospital_id in treatment_hospital[treatment_code]:
                        hospital_obj, p = treatment_hospital[treatment_code][hospital_id]
                        p.set_price_amount(price_type.lower(), amount)
                        treatment_hospital[treatment_code][hospital_id] = (hospital_obj, p)
                    else:
                        treatment_code_short = ""
                        if concept_code:
                            treatment_code_short = concept_code
                        else:
                            treatment_code_short = treatment_code
                        treatment_hospital[treatment_code]["Hospital Not Found"] = "No Hospitals Found for Treatment {} in Your Area".format(treatment_code_short)

        return treatment_hospital

    @staticmethod
    def create_category_files(category_description_dataset, category_letter_set):
        """
        Creates files by category that contain HCPCS, short description, long description
        *Updated the original treatment/category file to remove commas*
        """
        category_letter_dict = {} #dictionary of open files
        category_dict_list = {}

        for letter in category_letter_set: #open all files
            category_letter_dict[letter] = (open('files_for_config/%s.csv' %letter, 'a'))
            category_dict_list[letter] = []

        category_descriptions = CSVParser.readfile_to_dict(category_description_dataset)

        for line in category_descriptions:
            current_hcpcs_code = line['hcpcs_code'][:1]   
            if current_hcpcs_code in category_letter_set:
                category_dict_list[current_hcpcs_code].append(line['hcpcs_code'])
                category_letter_dict[current_hcpcs_code].write("%s %s %s \n" % (line['hcpcs_code'], line['short_description'], line['long_description']))

        for letter in category_letter_set: #close all files
            category_letter_dict[letter].close()

        return category_dict_list  

   

if __name__ == '__main__':
    

    #For Testing Purposes

    driver = Driver()
    #create files by category that contain hcpcs, short description, long description separated by spaces. 
    #driver.category_dict_list_hcpcs = driver.create_category_files(driver.category_description_dataset, driver.category_name_set) 

    #mocked_treatment_code_list = ["45754689", "45754690", "40661570"]
    mocked_treatment_code_list = ["44781957", "2721272", "44782131", "44786590", "2615330", "2718775", "915797"]
    print(driver.create_hospital_treatment_filtered_dict(mocked_treatment_code_list))