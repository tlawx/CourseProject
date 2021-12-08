import re, json
from Patient import Patient
from Search import Search
from driver import Driver


def main():

    print("Hello! Welcome to the Search System For Hospital Transparency Data.")
    patient_name = input("Please enter your name: ")
    patient_city = input("Please enter the city you live in: ")
    patient_city = re.sub('[^\w\s]'," ",patient_city)

    p = Patient(patient_name, patient_city)

    continue_searching = 1
    while continue_searching: 
        query = input("What kind of treatment are you looking for today? (For example you could try \"office visit\", \"mri\", \"ct scan\", or \"ambulance\"): ")
        s = Search(query)
        relevant_treatment_objects = s.find_possible_treatments()

        if len(relevant_treatment_objects) == 0:
            break

        driver = Driver()
        relevant_treatments_hospitals = driver.create_hospital_treatment_filtered_dict(patient_city, relevant_treatment_objects)
        
        #print(relevant_treatments_hospitals)
        d = driver.create_treatment_dict()
        #h = driver.create_hospital_dict()
        #for k, v in relevant_treatments_hospitals.items():
         #   print("  ",d[k].concept_code, ": ", d[k].treatment_name)
          #  print("     ", v)

        print(json.dumps(relevant_treatments_hospitals, sort_keys = False, indent = 3, default=str))

        
        var = input("Do you want to find another treatment? (Yes/Y or No/N) ")
        if var.lower() == "yes" or var.lower() == "y": 
            continue_searching = 1
        else:
            continue_searching = 0

if __name__ == "__main__":
    main()
