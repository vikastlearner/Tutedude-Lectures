class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Phone: {self.phone}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the phone directory")
        else:
            for contact in cls.phone_directory:
               print(contact.show_contact())

    @classmethod
    def search_contact(cls, name):
        for contact in cls.phone_directory:
            if contact.name.lower() == name.lower():
                return contact.phone
        return "No contacts found in the phone directory"

    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False


n_contacts = int(input("How many contacts do you want to enter?: "))

for i in range(n_contacts):
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print("Invalid phone number. It should be digit and greater than 8")


# c1 = Contact("Vikas", 9923854232)
# c2 = Contact("Varsha", 965020101)
# c3 = Contact("Deepak", 63728299)

# print(Contact.phone_directory)
# print(c1.show_contact())
# print(c2.show_contact())

Contact.show_all_contact()
# print(Contact.search_contact("vikas"))
# print(Contact.search_contact("Anki"))

