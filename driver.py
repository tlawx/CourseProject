from os import stat
from collections import defaultdict, namedtuple
from typing import Dict, NamedTuple
import pandas
from CSVParser import CSVParser
from Hospital import Hospital
from Treatment import Treatment
from Category import Category
from Price import Price

class Driver:
    def __init__(self):
        #self.hospital_dataset = ''
        #self.prices_dataset = ''
        #self.concepts_dataset = ''
        #self.categories_dataset = ''
        #self.category_description_dataset =''
        self.hospital_list = []
        self.treatment_list = []
        self.category_list = []
        self.category_name_set = []
        self.category_treatment_dict = {}
        self.category_treatment_list = []
        self.price_dict = {}
        self.category_treatment_dict = {}
        self.category_treatment_dict_list = []
        self.category_dict_list_hcpcs = {}
        self.categories_dataset = 'data/hcpcs_categories.csv'
        self.hospital_dataset = 'data/hospital.csv'
        self.prices_dataset = 'data/price.csv'
        self.concepts_dataset = 'data/concept.csv'
        self.category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
        self.hospital_index = None


    def set_treatment_list(self, treatment_list):
        self.treatment_list = treatment_list


    def set_category_list(self, category_list):
        self.category_list = category_list
    

    def set_category_name_set(self, category_name_set):
        self.category_name_set = category_name_set


    def set_category_dict_list_hcpcs(self, category_dict_list_hcpcs):
        self.category_dict_list_hcpcs = category_dict_list_hcpcs


    def set_category_treatment_dict(self, category_treatment_dict):
        self.category_treatment_dict = category_treatment_dict


    def set_category_treatment_dict_list(self, category_treatment_dict_list):
        self.category_treatment_dict_list = category_treatment_dict_list

    @staticmethod
    def get_treatment_list(self):
        return self.treatment_list

    @staticmethod
    def get_category_list(self):
        return self.category_list

    @staticmethod
    def get_category_treatment_dict(self):
        return self.category_treatment_dict

    @staticmethod
    def get_category_treatment_dict(self):
        return self.category_treatment_list  
    
    def create_city_dict_of_hopital_list(self):
        hospitals = CSVParser.readfile_to_dict(self.hospital_dataset)

        city_dict = defaultdict(list)

        for h in hospitals:
            city_dict[h['city']].append(h)
 
        return city_dict

    @staticmethod
    def create_hospital_object(hospital_row):
        h = Hospital(hospital_row['hospital_id'], hospital_row['hospital_name'], hospital_row['hospital_npi'])
        h.city = hospital_row['city']
        h.state = hospital_row['state']
        return h

    # clean up - not used
    @staticmethod
    def create_hospital_list(hospital_dataset):
        hospitals = CSVParser.readfile_to_dict(hospital_dataset)
        
        hospital_object_list = []
        for h in hospitals:
            hospital_object_list.append(driver.create_hospital_object(h))

        return hospital_object_list

    @staticmethod
    def create_treatment_list(treatment_dataset):
        treatments = CSVParser.readfile_to_dict(treatment_dataset)

        treatment_obj_list = []

        for t in treatments:
            treatment_obj_list.append(Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name']))
 
        return treatment_obj_list

    @staticmethod
    def create_treatment_dict(treatment_dataset):
        """
        Creates a dict of Treatment objects; concept_id (key) and Treatment_object (value)
        """
        treatments = CSVParser.readfile_to_dict(treatment_dataset)

        treatment_obj_dict = {}

        for t in treatments:
            treatment_obj_dict[t['concept_id']] = Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name'])
        
        return treatment_obj_dict

    @staticmethod
    def create_hospital_dict(hospital_dataset):
        """
        Creates a dict of Treatment objects; concept_id (key) and Treatment_object (value)
        """
        hospitals = CSVParser.readfile_to_dict(hospital_dataset)

        hospital_obj_dict = {}

        for h in hospitals:
            hospital_obj_dict[h['hospital_id']] = Hospital(h['hospital_id'], h['hospital_name'], h['hospital_npi'], h['city'], h['state'], h['affiliation'], h['disclosure'])
        
        return hospital_obj_dict

    @staticmethod
    def create_category_list(category_dataset):
        """
        Creates a list of category objects, setting the name and letter
        """
        categories = CSVParser.readfile_to_dict(category_dataset)

        category_obj_list = []
        category_name_set = set()

        for line in categories:
            new_cat = Category(line['category_name'], line['category_letter'])
            category_name_set.add(line['category_letter'])
            category_obj_list.append(new_cat)

        return category_obj_list, category_name_set


    @staticmethod
    def create_category_treatment_dict(category_letter_set ,category_dataset, treatment_dataset):
        """
        Creates a dict of dicts. Category_letters (keys) and treatment_dict (values) with treatment_id (keys) and treatment objects (values)
        """
        categories = CSVParser.readfile_to_dict(category_dataset)
        treatments = CSVParser.readfile_to_dict(treatment_dataset)

        category_dict = {}

        for c in categories:
            category_dict[c['category_letter']] = {}

        for t in treatments:
            current_category_letter = t['concept_code'][:1] 
            if current_category_letter in category_letter_set: # Only add treatments in established categories
                category_dict[current_category_letter][t['concept_code']] = Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name'])
     
        return category_dict

    @staticmethod
    def create_price_dict(price_dataset):
        """
        Creates a dict of dicts. Gross/Cash/Min/Max (keys) and dict (keys) with "hospital_id concept_id" (values)
        """
        prices = CSVParser.readfile_to_dict(price_dataset)

        price_dict = {}

        price_dict['gross'] = {}
        price_dict['cash'] = {}
        price_dict['max'] = {}
        price_dict['min'] = {}

        for p in prices:
            #price_dict[p['price']][1] = p['amount']
            price_dict[p['price']][p['hospital_id']+" "+p['concept_id']] = p['amount']

        return price_dict

    @staticmethod
    def create_category_treatment_list(category_treatment_dict):
        """
        Creates a dict of lists. Category letter key and value is dict of key as line number with value as the treatment object
        """
        category_dict = {}

        for c in category_treatment_dict:
            count = 0
            category_dict[c] = []
            for t in category_treatment_dict[c]: 
                category_dict[c].insert(count,category_treatment_dict[c][t])
                count = count + 1

        return category_dict

    @staticmethod
    def create_category_files(category_description_dataset, category_letter_set):
        """
        Creates files by category that contain HCPCS, short description, long description
        *Needs a little work because there are spaces in the original descriptions file*
        **Updated the original treatment/category file to remove commas**
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

    @staticmethod
    def create_treatment_index(treatment_obj_list): 
        """
        Creates a dict of treatment_id (keys) and treatment objects (values)
        """
        treatment_index = {}

        for treatment_obj in treatment_obj_list:
            treatment_index[treatment_obj.concept_id] = treatment_obj

        return treatment_index

    @staticmethod
    def create_hospital_index(hospital_obj_list):
        """
        Creates an index (dict) of hospital_id (keys) and hospital objects (values)
        """
        hospital_index = {}

        for hospital_obj in hospital_obj_list:
            hospital_index[hospital_obj.hospital_id] = hospital_obj

        return hospital_index

    @staticmethod
    def create_category_index(category_obj_list): 
        """
        Creates a dict of treatment_id (keys) and treatment objects (values)
        """
        category_index = {}

        for cat_obj in category_obj_list:
            category_index[cat_obj.letter] = cat_obj

        return category_index

    # clean up
    @staticmethod
    def create_index_with_given_key(id_field, obj_list):
        """
        Creates a dict with specified key and matching object id as value
        """
        index = {}

        for obj in obj_list:
            index[obj.__dataclass_fields__[id_field]] = obj

        return index
    
    def create_hospital_treatment_filtered_dict(self, city):
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
        if not self.hospital_index:
            self.hospital_index = self.create_hospital_index(driver.hospital_list)

        hospitals_in_city_list = self.create_city_dict_of_hopital_list()[city]

        prices = CSVParser.readfile_to_dict(self.prices_dataset)

        prices_filtered = []
        hospital_id_set = set([h['hospital_id'] for h in hospitals_in_city_list])
        
        # Getting only price entries for hospital IDs in city parameter
        for entry in prices:
            if entry['hospital_id'] in hospital_id_set:
                prices_filtered.append(entry)


        print("Treatments avaialble in this city:", len(prices_filtered))
        
        # build {treatment_id: {hospital_id: (hospital, price)} dict of dicts
        treatment_hospital = {}
        for entry in prices_filtered:
            treatment_code, hospital_id, price_type, amount = entry['concept_id'], entry['hospital_id'], entry['price'], entry['amount']
            
            hospital_obj = self.hospital_index[hospital_id]
            
            if hospital_id not in treatment_hospital:
                p = Price()
                p.set_price_amount(price_type.lower(), amount)

                treatment_hospital[treatment_code] = dict()
                treatment_hospital[treatment_code][hospital_id] = (hospital_obj, p)
            else:
                hospital_obj, p = treatment_hospital[treatment_code][hospital_id]
                p.set_price_amount(price_type.lower(), amount)
                treatment_hospital[treatment_code][hospital_id] = (hospital_obj, p)

        return treatment_hospital
   

if __name__ == '__main__':
    
    driver = Driver()
    
    # driver.categories_dataset = 'data/hcpcs_categories.csv'
    #driver.hospital_dataset = 'data/hospital.csv'
    # driver.prices_dataset = 'data/price.csv'
    # driver.concepts_dataset = 'data/concept.csv'
    # driver.category_description_dataset = 'data/hcpcs_descriptions_2020.csv'

    
    driver.treatment_list = driver.create_treatment_list(driver.concepts_dataset)
    driver.hospital_list = driver.create_hospital_list(driver.hospital_dataset)
    driver.category_list, driver.category_name_set = driver.create_category_list(driver.categories_dataset)
    driver.prices_dict = driver.create_price_dict(driver.prices_dataset)

    city_dict = driver.create_city_dict_of_hopital_list()
    for c in city_dict['Hickory']:
        print(c)


    hospital_index = hospital_index = driver.create_hospital_index(driver.hospital_list)
    treatment_index = treatment_index = driver.create_treatment_index(driver.treatment_list)
    category_index = category_index = driver.create_category_index(driver.category_list)

    
    #create files by category that contain hcpcs, short description, long description separated by spaces. 
    driver.category_dict_list_hcpcs = driver.create_category_files(driver.category_description_dataset, driver.category_name_set) 

    driver.category_treatment_dict = driver.create_category_treatment_dict(driver.category_name_set, driver.categories_dataset, driver.concepts_dataset)
    driver.category_treatment_dict_list = driver.create_category_treatment_list(driver.category_treatment_dict)

    # Output for logging and debugging
    print(driver.category_dict_list_hcpcs['A'][5])
    print(driver.category_treatment_dict['A'][driver.category_dict_list_hcpcs['A'][5]].treatment_name)
    print(driver.category_treatment_dict['A']['A4462'].concept_code)
    print(driver.category_treatment_dict_list['A'][0].concept_code)
    print(hospital_index['1'].name)
    print(treatment_index['43533189'])

    print(driver.create_hospital_treatment_filtered_dict("Winston-Salem", None, None))