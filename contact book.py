def search(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("---- Contact Found ----")
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
        print("------------------------")
    else:
        print("Contact not found!")
