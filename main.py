from Patient import Patient
from Search import Search
from driver import Driver

def main():

    driver = Driver()
    city_dict = driver.create_city_dict_of_hopital_list()

    print("Hello! Welcome to the Search System For Hospital Transparency Data.")
    patient_name = input("Please enter your name: ")
    patient_city = input("Please enter the city you live in: ")

    p = Patient(patient_name, patient_city)

    # need to update after getting all the categories we have
    category_code = input("What kind of service are you looking for today?\n"
                              "A - Transportation, Medical and Surgical Supplies, Miscellaneous and Experimental\n"
                              "B - Enteral and Parenteral Therapy\n"
                              "C - Temporary Hospital Outpatient Prospective Payment System\n"
                              "D - Dental codes\n"
                              "E - Durable Medical Equipment\n"
                              "G - Temporary Procedures and Professional Services\n"
                              "H - Rehabilitative Services\n"
                              "J - Drugs administered other than oral method, chemotherapy drugs\n"
                              "K - Temporary codes for durable medical equipment regional carriers\n"
                              "L - Orthotic/prosthetic services\n"
                              "M - Medical services\n"
                              "P - Pathology and Laboratory\n"
                              "Q - Temporary codes\n"
                              "R - Diagnostic radiology services\n"
                              "S - Private payer codes\n"
                              "T - State Medicaid agency codes\n"
                              "V - Vision/hearing services\n"
                              "(Please the code correlated with your topic of choice): ")

    category_name = ""
    if category_code == "A":
        category_name = "Transportation, Medical and Surgical Supplies, or Miscellaneous and Experimental"
    elif category_code == "B":
        category_name = "Enteral and Parenteral Therapy"
    elif category_code == "C":
        category_name = "Temporary Hospital Outpatient Prospective Payment System"
    elif category_code == "D":
        category_name = "Dental codes"
    elif category_code == "E":
        category_name = "Durable Medical Equipment"
    elif category_code == "G":
        category_name = "Temporary Procedures and Professional Services"
    elif category_code == "H":
        category_name = "Rehabilitative Services"
    elif category_code == "J":
        category_name = "Drugs administered other than oral method, chemotherapy drugs"
    elif category_code == "K":
        category_name = "Temporary codes for durable medical equipment regional carriers"
    elif category_code == "L":
        category_name = "Orthotic/prosthetic services"
    elif category_code == "M":
        category_name = "Medical services"
    elif category_code == "N":
        category_name = "Pathology and Laboratory"
    elif category_code == "Q":
        category_name = "Temporary codes"
    elif category_code == "R":
        category_name = "Diagnostic radiology services"
    elif category_code == "S":
        category_name = "Private payer codes"
    elif category_code == "T":
        category_name = "State Medicaid agency codes"
    elif category_code == "V":
        category_name = "Vision/hearing services"

    query = input("What kind of " + category_name + " are you looking for? ")

    s = Search(category_code, query)
    s.find_possible_treatments()

if __name__ == "__main__":
    main()
