# Mini-Project: Contact Management System

import sys
from termcolor import colored
import re

contacts = {}


def add_new_contact():
    first_name = str(input("Enter contact's first name: ")).title()
    last_name = str(input("Enter contact's last name: ")).title()
    phone_number = input("Enter contact's phone number 1-###-###-####: ")
    email = input("Enter contact's email address: ")
    category = str(input("Enter the category or categories of contact (Family - Friend - Work): ")).title()
    custom_field = input("Enter new contact label(e.g., birthday, anniversary, address): ").title()
    custom_field_info = input(f"Enter information for {custom_field}: ").title()
    contact_notes = input("Enter extra notes about contact: ").title()
    if re.match(r"^(1-)?\d{3}-\d{3}-\d{4}$", phone_number) and re.match(r"[^@]+@[^@]+\.[^@]+", email):
        contacts[f"{first_name} {last_name}"] = {"First Name": first_name, "Last Name": last_name, "Phone Number": phone_number, "Email": email, "Category": category, custom_field: custom_field_info, "Notes": contact_notes}
        print(f"{first_name} {last_name} with phone number: {phone_number} added to contacts. \nAdditional Details: {email}, {category}, {custom_field}: {custom_field_info}, {contact_notes}")
    else:
        print("Invalid entry of phone number or email address. Please try again.")
        

def edit_existing_contact():
    key_to_edit = ""
    first_name_to_edit = input("Enter the first name of the contact you are editing: ").title()
    last_name_to_edit = input("Enter the last name of the contact you are editing: ").title()
    for key, data in contacts.items():
        if first_name_to_edit and last_name_to_edit in data.values():
            key_to_edit = key

    try:
        if key_to_edit:
            first_name = str(input("Enter contact's new first name: ")).title()
            last_name = str(input("Enter contact's new last name: ")).title()
            phone_number = input("Enter contact's new phone number 1-###-###-####: ")
            email = input("Enter contact's new email address: ")
            category = str(input("Enter the new category or categories of contact (Family - Friend - Work): ")).title()
            custom_field = input("Enter new contact label(e.g., birthday, anniversary, address): ").title()
            custom_field_info = input(f"Enter new information for {custom_field}: ").title()
            contact_notes = input("Enter new notes about contact: ").title()
            if first_name:
                contacts[key_to_edit]["First Name"] = first_name
            if last_name:
                contacts[key_to_edit]["Last Name"] = last_name
            if phone_number:
                contacts[key_to_edit]["Phone Number"] = phone_number
            if email:
                contacts[key_to_edit]["Email"] = email
            if category:
                contacts[key_to_edit]["Category"] = category
            if custom_field:
                contacts[key_to_edit][custom_field] = custom_field
            if custom_field_info:
                contacts[key_to_edit][custom_field_info] = custom_field_info
            if contact_notes:
                contacts[key_to_edit]["Notes"] = contact_notes
        else:
            print("Contact not found. Please try again.")

    except Exception as e:
        print(f"An upexpected error {e} occurred. Please try again.")
    finally:
        print("😊")
            

def delete_contact():
    key_to_delete = ""
    first_name_to_delete = input("Enter the first name of the contact you are deleting: ").title()
    last_name_to_delete = input("Enter the last name of the contact you are deleting: ").title()
    try:
        for key, data in contacts.items():
            if first_name_to_delete and last_name_to_delete in data.values():
                key_to_delete = key
        if key_to_delete:
            del contacts[key_to_delete]
            print("Contact has been deleted.")
    except Exception as e:
        print(f"An upexpected error {e} occurred. Please try again.")
    

def search_for_contact():
    try:
        global contacts
        while True:
            for i in contacts:
                print(colored("\nSearch for Contact By:", "white", attrs=["bold"]))
                print(colored("1.", "light_blue", attrs=["bold"]), end=" ")
                print(colored("First and Last Name", "grey"))
                print(colored("2.", "light_blue", attrs=["bold"]), end=" ")
                print(colored("Phone Number", "grey"))
                print(colored("3.", "light_blue", attrs=["bold"]), end=" ")
                print(colored("Email", "grey"))
                print(colored("4.", "light_blue", attrs=["bold"]), end=" ")
                print(colored("Category", "grey"))
                print(colored("5.", "light_blue", attrs=["bold"]), end=" ")
                print(colored("Notes", "grey"))
                print(colored("6.", "light_blue", attrs=["bold"]), end=" ")
                print(colored("Exit", "grey"))
                choice = input("Enter your choice: ")

                if choice == "1":
                    contact = input("Enter the first and last name of the contact you are searching for: ").title()
                    if contact in contacts:
                        print(colored(f"\nContact: {contact}", "light_blue", attrs=["bold"]))
                        print(" ")
                        for key, value in contacts[contact].items():
                            print(colored(key+":", attrs=["bold"]))
                            print(colored(value, "grey"))
                            print(" ")
                    else:
                        print("Contact was not found. Please try again.")
                elif choice == "2":
                    number = input("Enter the phone number of the contact you are searching for: ")
                    for contact in contacts:
                        print(contact)
                        if contact["Phone Number"] == number:
                            print(contacts[contact])
                elif choice == "3":
                    contacts[i]["Email"] = input("Enter the email of the contact you are searching for: ")
                    if i in contacts:
                        print(colored(f"\nPhone Number: {i}", "light_blue", attrs=["bold"]))
                        print(" ")                    
                        for key, value in contacts[i].items():
                            print(colored(key+":", attrs=["bold"]))
                            print(colored(value, "grey"))
                            print(" ")
                    else:
                        print("Contact was not found. Please try again.")
                elif choice == "4":
                    contacts[i][f"Category"] = input("Enter the category or categories of the contact you are searching for(Family - Friend - Work): ").title()
                    if i in contacts:
                        print(colored(f"\nPhone Number: {i}", "light_blue", attrs=["bold"]))
                        print(" ")
                        for key, value in contacts[i].items():
                            print(colored(key+":", attrs=["bold"]))
                            print(colored(value, "grey"))
                            print(" ")
                    else:
                        print("Contact was not found. Please try again.")
                elif choice == "5":
                    contacts[i][f"Notes"] = input("Enter the notes of the contact you are searching for: ").title()
                    if i in contacts:
                        print(colored(f"\nPhone Number: {i}", "light_blue", attrs=["bold"]))
                        print(" ")
                        for key, value in contacts[i].items():
                            print(colored(key+":", attrs=["bold"]))
                            print(colored(value, "grey"))
                            print(" ")
                    else:
                        print("Contact was not found. Please try again.")
                elif choice == "6":
                    main()
                else:
                    print("Invalid choice. Please try again.")
    except ValueError:
        print("Please use only numbers in this format for phone number: 1-###-###-####")
    except Exception as e:
        print("An unexpected error occured. Please try again.")
    finally:
        print("😊")


def display_contacts():
    global contacts
    contacts = dict(sorted(contacts.items(), key=lambda item: item[1]["Last Name"]))
    if len(contacts) >= 1:
        print(colored("\nAlphabetical Order of Contacts:", "white", attrs=["bold"]))
        for i in contacts:
            print(colored(f"\nPhone Number: {i}", "light_blue", attrs=["bold"]))
            print(" ")
            for key, value in contacts[i].items():
                print(colored(key+":", attrs=["bold"]))
                print(colored(value, "grey"))
                print(" ")
            print("-----------------")
    else:
        print("The contact list is empty.")

def export_contacts(contacts):
    with open("contacts.txt", "a") as f:
        for key, nested in contacts.items():
            print(key, file=f)
            for subkey, value in nested.items():
                print("  {}: {}".format(subkey, value), file=f)
            print(file=f)
        print("Successfully exported contact to contacts file.")
            

def import_contacts(contacts):
    with open("contacts.txt", "r") as f:
        current_name = None
        for line in f:
            line = line.strip()
            if not line:
                continue
            if ":" not in line:
                first_name, last_name = line.split()
                current_name = (first_name, last_name)
                contacts[current_name] = {}
            else:
                key, value = line.split(": ")
                contacts[current_name][key] = value
    print(contacts)
    print("Successfully imported contacts file to contacts.")

def backup_or_restore_contacts(contacts):
    while True:
        for i in contacts:
            print(colored("\nBackup or Restore Contacts:", "white", attrs=["bold"]))
            print(colored("1.", "light_blue", attrs=["bold"]), end=" ")
            print(colored("Backup Contacts", "grey"))
            print(colored("2.", "light_blue", attrs=["bold"]), end=" ")
            print(colored("Restore Contacts", "grey"))
            print(colored("3.", "light_blue", attrs=["bold"]), end=" ")
            print(colored("Exit", "grey"))
            choice = input("Enter your choice: ")

            if choice == "1":
                with open("backup.txt", "a") as f:
                    for key, nested in contacts.items():
                        print(key, file=f)
                        for subkey, value in nested.items():
                            print("  {}: {}".format(subkey, value), file=f)
                        print(file=f)
                print("Successfully backed up contacts to backup file.")
            elif choice == "2":
                with open("backup.txt", "r") as f:
                    current_name = None
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        if ":" not in line:
                            first_name, last_name = line.split()
                            current_name = (first_name, last_name)
                            contacts[current_name] = {}
                        else:
                            key, value = line.split(": ")
                            contacts[current_name][key] = value
                print(contacts)
                print("Successfully restored contacts from backup file.")
            elif choice == "3":
                main()
            else:
                print("Invalid choice. Please try again.")
        if not contacts:
            print("The contact list is empty.")
            main()

def main():
    while True:
        print("\nWelcome to the", end=" ")
        print(colored(" Contact Management System!\n", "light_blue", attrs=["bold"]), end=" ")
        print(colored("\nMenu:", "white", attrs=["bold"]))
        print(colored("1.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Add a New Contact", "grey"))
        print(colored("2.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Edit an Existing Contact", "grey"))
        print(colored("3.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Delete a Contact", "grey"))
        print(colored("4.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Search for a Contact", "grey"))
        print(colored("5.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Display All Contactst", "grey"))
        print(colored("6.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Export Contacts to a Text File", "grey"))
        print(colored("7.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Import Contacts from a Text File", "grey"))
        print(colored("8.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Backup or Restore Contacts", "grey"))
        print(colored("9.", "light_blue", attrs=["bold"]), end=" ")
        print(colored("Quit\n", "grey"))
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_contact()
        elif choice == "2":
            edit_existing_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_for_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            export_contacts(contacts)
        elif choice == "7":
            import_contacts(contacts)
        elif choice == "8":
            backup_or_restore_contacts(contacts)
        elif choice == "9":
            print(colored("\nExiting Contact Management System... \n👋 TTFN! 👋\n", "light_blue", attrs=["bold"]))
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()