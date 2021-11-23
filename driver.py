from os import stat
import pandas
from CSVParser import CSVParser
from Hospital import Hospital
from Treatment import Treatment
from Category import Category

class Driver:
    def __init__(self):
        self.hospital_list = []
        self.hospital_dataset = ''
        self.prices_dataset = ''
        self.concepts_dataset = ''
        self.categories_dataset = ''
        self.treatment_list = []
        self.category_list = []
        self.category_treatment_dict = []
        self.category_treatment_list = []

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
            hospital_object_list.append(driver.create_hospital_object(h))

        return hospital_object_list

    @staticmethod
    def add_treatment_price_data_to_hospitals(prices_dataset, hospital_index):
        prices_treatments = CSVParser.readfile_to_dict(prices_dataset)

        # for entry in prices_treatments:
        #     # each entry is a dict e.g {'hospital_id': '1', 'concept_id': '2101827', 'price': 'gross', 'amount': '9221'}
        #     if 'hospital_id' in entry.keys():
        #         if entry['hospital_id'] in hospital_index.keys():
        #             hospital = hospital_index[entry['hospital_id']]
        #             hospital.add_new_treatment_by_id(entry['concept_id'])
   
    @staticmethod
    def create_treatment_list(self, treatment_dataset):
        treatments = CSVParser.readfile_to_dict(treatment_dataset)

        treatment_obj_list = []

        for t in treatments:
            treatment_obj_list.append(Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name']))

        self.treatment_list = treatment_obj_list
        return treatment_obj_list

    @staticmethod
    def create_category_list(self, category_dataset):
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

        self.category_list = category_obj_list
        return category_obj_list, category_name_set

    @staticmethod
    def create_category_treatment_list(self, category_treatment_dict):
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

        self.category_treatment_list = category_dict
        return category_dict

    @staticmethod
    def create_category_treatment_dict(self, category_dataset, treatment_dataset):
        """
        Creates a dict of dicts. Category_letters (keys) and treatment_dict (values) with treatment_id (keys) and treatment objects (values)
        """
        categories = CSVParser.readfile_to_dict(category_dataset)
        treatments = CSVParser.readfile_to_dict(treatment_dataset)

        category_dict = {}

        for c in categories:
            category_dict[c['category_letter']] = {}

        for t in treatments:
            current_hcpcs_code = t['concept_code'][:1] 
            if current_hcpcs_code in category_dict: # Only add treatments in established categories
                category_dict[current_hcpcs_code[:1]][t['concept_code']] = Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name'])

        self.category_treatment_dict = category_dict         
        return category_dict

    @staticmethod
    def create_category_files(category_description_dataset, category_letter_set):
        """
        Creates files by category that contain HCPCS, short description, long description
        **Needs a little work because there are spaces in the original descriptions file**
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
                category_dict_list[current_hcpcs_code[:1]].append(line['hcpcs_code'])
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

    @staticmethod
    def create_index_with_given_key(id_field, obj_list):
        """
        Creates a dict with specified key and matching object id as value
        """
        index = {}

        for obj in obj_list:
            index[obj.__dataclass_fields__[id_field]] = obj

        return index


    @staticmethod
    def get_hospital_by_id(hospital_id):
        pass



if __name__ == '__main__':
    
    driver = Driver()
    
    # Add proper path checking and move these values to config 
    driver.categories_dataset = 'data/hcpcs_categories.csv'
    driver.hospital_dataset = 'data/hospital.csv'
    driver.prices_dataset = 'data/price.csv'
    driver.concepts_dataset = 'data/concept.csv'
    driver.category_description_dataset = 'data/hcpcs_descriptions_2020.csv'
    
    treatment_list = driver.create_treatment_list(driver.concepts_dataset)
    hospital_list = driver.create_hospital_list(driver.hospital_dataset)
    category_list, category_name_set = driver.create_category_list(driver.categories_dataset)

    hospital_index = hospital_index = driver.create_hospital_index(hospital_list)
    treatment_index = treatment_index = driver.create_treatment_index(treatment_list)
    category_index = category_index = driver.create_category_index(category_list)
    #driver.add_treatment_price_data_to_hospitals(driver.prices_dataset, hospital_index)

    
    #create files by category that contain hcpcs, short description, long description separated by spaces. 
    category_dict_list_hcpcs = driver.create_category_files(driver.category_description_dataset, category_name_set) 

    category_treatment_dict = driver.create_category_treatment_dict(driver.categories_dataset, driver.concepts_dataset)
    category_treatment_dict_list = driver.create_category_treatment_list(category_treatment_dict)

    # Output for logging and debugging
    print(category_dict_list_hcpcs['A'][5])
    print(category_treatment_dict['A']['2614613'].concept_code)
    print(category_treatment_dict_list['A'][0].concept_code)
    print(hospital_index['1'].name)
    print(treatment_index['43533189'])

