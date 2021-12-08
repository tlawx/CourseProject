import re, json
from Patient import Patient
from Search import Search
from driver import Driver


def main():

    print("Hello! Welcome to the Search System For Hospital Transparency Data.")
    patient_name = input("Please enter your name: ")

    # additional functionality to filter results based upon city. Need larger dataset first. 
    #patient_city = input("Please enter the city you live in: ")
    #patient_city = re.sub('[^\w\s]'," ",patient_city.lower())

    p = Patient(patient_name)

    continue_searching = 1
    while continue_searching: 
        query = input("What kind of treatment are you looking for today? ") # (For example you could try \"office visit\", \"mri\", \"ct scan\", or \"ambulance\"): ")
        s = Search(query)
        relevant_treatment_objects = s.find_possible_treatments()

        if relevant_treatment_objects != 1:
            print("We found treatments. Now we're checking the hospitals in your city.")
            driver = Driver()
            relevant_treatments_hospitals = driver.create_hospital_treatment_filtered_dict(patient_city, relevant_treatment_objects)
            
            d = driver.create_treatment_dict()
            h = driver.create_hospital_dict()

            print("")
            print("Best Matched Treatments:")
            for treatment, hosp_list in relevant_treatments_hospitals.items():
                print("")
                print("  Treatment Name: ", d[treatment].treatment_name)
                count = 0
                for hosp, tup in hosp_list.items():
                    if count < 5: 
                        print("    Hospital Name: ", tup[0].name)
                        print("      NPI: ", tup[0].npi)
                        print("      Cash Price:", tup[1].cash)
                        print("      Gross Price:", tup[1].gross)
                        print("      Min Price:", tup[1].min)
                        print("      Max Price:", tup[1].max)
                        count = count + 1
                    #print(json.dumps(tup, sort_keys= False , indent = 3, default=str))
            print("")
        var = input("Do you want to find another treatment? (Yes/Y or No/N) ")
        if var.lower() == "yes" or var.lower() == "y": 
            continue_searching = 1
        else:
            continue_searching = 0

if __name__ == "__main__":
    main()
