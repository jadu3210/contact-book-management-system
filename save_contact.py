

import csv
def add_contact(all_contacts):
     name = input("Enter the name of the contact: ")
     email = input("Enter the email of the contact: ")
     number = input("Enter the Phone Number of the contact: ")
     address = input("Enter the Address of the contact: ")
     for contact in all_contacts:
         if contact['number'] == number:
             print(f"Phone number {number} already exists. Can't add to contacts")
             return all_contacts
     contact = {
                'name': name,
                'email': email,
                'number': number,
                'address': address 
                }
     all_contacts.append(contact)
     print('Contact added successfully')
     return all_contacts
         
def save_contacts(all_contacts):
     with open('all_contacts.csv', mode="w", newline='') as fp:
         writer = csv.writer(fp)
         for contact in all_contacts:
             writer.writerow([contact['name'], contact['email'], contact['number'], contact['address']])

def load_contacts():
     all_contacts = []
     try:
         with open('all_contacts.csv', mode="r", newline='') as fp:
             reader = csv.reader(fp)
             for row in reader:
                 contact = { 'name': row[0], 'email': row[1], 'number': row[2], 'address': row[3] }
                 all_contacts.append(contact)
     except FileNotFoundError:
         pass
     return all_contacts
     
def view_contacts(all_contacts):
    if all_contacts:
        for contact in all_contacts:
             print(f"Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}, Address: {contact['address']}")
    else:
        print('No contacts found.')
