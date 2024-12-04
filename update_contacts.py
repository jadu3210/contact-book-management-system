from save_contact import add_contact, save_contacts, load_contacts



def update_contact(all_contacts):
     number = input("Enter the Phone Number of the contact to update: ")
     contact_found = False
     for contact in all_contacts:
         if contact['number'] == number:
             contact_found = True
             print(f"Current details: Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}, Address: {contact['address']}")
             name = input("Enter new name (leave blank to keep current): ")
             email = input("Enter new email (leave blank to keep current): ")
             new_number = input("Enter new Phone Number (leave blank to keep current): ")
             address = input("Enter new Address (leave blank to keep current): ")
             if name:
                 contact['name'] = name
             if email:
                 contact['email'] = email
             if new_number:
                 contact['number'] = new_number
             if address:
                 contact['address'] = address
                 print('Contact updated successfully')
                 break
     if not contact_found:
        print('No contact found with that Phone Number')
     save_contacts(all_contacts)
     return all_contacts
         
def delete_contact(all_contacts):
     number = input("Enter the Phone Number of the contact to update: ")
     contact_found = False
     for contact in all_contacts:
         if contact['number'] == number:
             contact_found = True
             print(f"Current details: Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}, Address: {contact['address']}")
             all_contacts.remove(contact)
             print('Contact deleted successfully')
             break
     if not contact_found:
        print('No contact found with that Phone Number')
     save_contacts(all_contacts)
     return all_contacts

def search_contact(all_contacts):
     number = input("Enter the Phone Number of the contact to update: ")
     contact_found = False
     for contact in all_contacts:
         if contact['number'] == number:
             contact_found = True
             print(f"Search Contact details: Name: {contact['name']}, Email: {contact['email']}, Number: {contact['number']}, Address: {contact['address']}")
             break
     if not contact_found:
        print('No contact found with that Phone Number')
         