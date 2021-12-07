import re
from Patient import Patient
from Search import Search
from driver import Driver


def main():

    print("Hello! Welcome to the Search System For Hospital Transparency Data.")
    patient_name = input("Please enter your name: ")
    patient_city = input("Please enter the city you live in: ")
    patient_city = re.sub('[^\w\s]'," ",patient_city)

    p = Patient(patient_name, patient_city)

    query = input("What kind of treatment are you looking for today? ")

    s = Search(query)
    relevant_treatment_objects = s.find_possible_treatments()

    driver = Driver()
    relevant_treatment = driver.create_hospital_treatment_filtered_dict(patient_city, relevant_treatment_objects)

if __name__ == "__main__":
    main()
