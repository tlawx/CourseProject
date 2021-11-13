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
        self.categories_dataset = ''

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
    def create_treatment_list(treatment_dataset):
        treatments = CSVParser.readfile_to_dict(treatment_dataset)

        treatment_obj_list = []

        for t in treatments:
            treatment_obj_list.append(Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name']))

        return treatment_obj_list


    @staticmethod
    def create_category_treatment_dict(category_dataset, treatment_dataset):
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
                category_dict[current_hcpcs_code[:1]][t['concept_id']] = Treatment(t['concept_id'], t['concept_code'], t['vocabulary_id'], t['concept_name'])

        return category_dict

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
    
    treatment_list = driver.create_treatment_list(driver.concepts_dataset)
    hospital_list = driver.create_hospital_list(driver.hospital_dataset)
    
    category_treatment_dict = driver.create_category_treatment_dict(driver.categories_dataset, driver.concepts_dataset)
    
    hospital_index = hospital_index = driver.create_hospital_index(hospital_list)
    treatment_index = treatment_index = driver.create_treatment_index(treatment_list)
    
    #driver.add_treatment_price_data_to_hospitals(driver.prices_dataset, hospital_index)

    # Output for logging and debugging
    print(category_treatment_dict['A']['2614981'])
    print(hospital_index['1'])
    print(treatment_index['43533189'])

