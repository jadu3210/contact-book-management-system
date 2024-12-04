from save_contact import save_contacts, add_contact, load_contacts, view_contacts
from update_contacts import update_contact, delete_contact, search_contact


def main():
     all_contacts = load_contacts()
     while True:
         print("\n Welcome to Contact Book Management System")
         print("\nOptions:")
         print("1. Add Contact")
         print("2. View Contacts")
         print("3. Search Contact")
         print("4. Update Contact")
         print("5. Delete Contact")
         print("0. Exit")
         choice = input("Choose an option (0-5): ")
         if choice == '1':
            all_contacts = add_contact(all_contacts)
         elif choice == '2':
            view_contacts(all_contacts)
         elif choice == '3':
            search_contact(all_contacts)
         elif choice == '4':
            all_contacts = update_contact(all_contacts)
         elif choice == '5':
            all_contacts = delete_contact(all_contacts)
         elif choice == '0':
            save_contacts(all_contacts)
            print('Thanks for using Contact Book Management System')
            break
         else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()