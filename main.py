import re
import random

# Age Range
min_age = 18
max_age = 65


# Data Validation
def vcard_id_validation(vcard_id):
    return re.fullmatch(r"^\d{8}$", vcard_id)


def person_name_validation(person_name):
    return re.fullmatch(r"^[A-Z][a-z]+$", person_name)


def person_lastname_validation(person_lastname):
    return re.fullmatch(r"^[A-Z][a-z]+$", person_lastname)


def person_age_validation(person_age):
    if re.fullmatch(r"^\d{2}$", person_age):
        return min_age <= int(person_age) <= max_age
    else:
        return False


def person_speciality_validation(person_speciality):
    return re.fullmatch(r"^[A-Z][a-z]+$", person_speciality)


# Show Visiting Card
def show_vcard(vcard_id, person_name, person_lastname, person_age, person_speciality):
    print(f'[VCard #{vcard_id}]\n'
          f'Hello, my name is {person_name} {person_lastname}.\n'
          f'I\'m {person_age}.\n'
          f'My speciality is {person_speciality}.\n')


# Enter Data
def input_data_start():
    vcard_id = random.getrandbits(26)
    # while not vcard_id_validation(vcard_id):
    #     vcard_id = random.getrandbits(26)

    person_name = input("Please, enter your name: ")
    while not person_name_validation(person_name):
        person_name = input("Incorrect input! Please, enter your name (ex:Name): ")

    person_lastname = input("Please, enter your lastname: ")
    while not person_lastname_validation(person_lastname):
        person_lastname = input("Incorrect input! Please, enter your name (ex:Lastname): ")

    person_age = input("Please, enter your age: ")
    while not person_age_validation(person_age):
        person_age = input(f'Incorrect input! Please, enter your age (age range: {min_age} - {max_age}): ')

    person_speciality = input("Please, enter your speciality: ")
    while not person_speciality_validation(person_speciality):
        person_speciality = input("Incorrect input! Please, enter your name (ex:Speciality): ")

    show_vcard(vcard_id, person_name, person_lastname, person_age, person_speciality)


# Main Start
input_data_start()