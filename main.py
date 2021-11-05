from Patient import Patient
from Utilities import Utilities


def main():
    # TODO: need to deal with spelling mistakes and capitalization

    print("Hello! Welcome to the Search System For Hospital Transparency Data.")
    patient_name = raw_input("Please enter your name: ")
    patient_state = raw_input("Please enter the state you live in (abbreviation): ")

    p = Patient(patient_name, patient_state)

    # need to update after getting all the categories we have
    category = raw_input("What kind of service are you looking for today? "
                         "Please enter one of the following - technology, general service, etc: " )

    query = raw_input("What kind of " + category + " are you looking for? ")

    # call a function that outputs a ranked list of treatments and their hospitals
    u = Utilities()
    u.get_relevant_list(category, query)

if __name__ == "__main__":
    main()
