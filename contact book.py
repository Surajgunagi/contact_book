import json
import os

CONTACTS_FILE = "contacts.json"


# ---------------------- Load Contacts ----------------------
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}   # empty dict if no file


# ---------------------- Save Contacts ----------------------
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("Contacts saved successfully!")


# ---------------------- Add Contact ----------------------
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {"phone": phone, "email": email}
    print("Contact added!")


# ---------------------- Update Contact ----------------------
def update_contact(contacts):
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return

    print("Leave blank if you don't want to update.")

    phone = input("New phone (optional): ").strip()
    email = input("New email (optional): ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email

    print("Contact updated!")


# ---------------------- Delete Contact ----------------------
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")


# ---------------------- Search Contact ----------------------
def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("---- Contact Found ----")
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
        print("------------------------")
    else:
        print("Contact not found!")


# ---------------------- Main Program ----------------------
def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Save & Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            update_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            break
        else:
            print("Invalid choice! Try again.")


# Run Program
if __name__ == "__main__":
    main()



