#Aldrinerd's Phone Manager (No Error Handling!)
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def modify(self, new_brand, new_model):
        self.brand = new_brand
        self.model = new_model
    def __str__(self):
        return f"{self.brand}, {self.model}"
def print_menu():
    print("Welcome to phone manager! \n1. Add Phone\n2. Delete Phone\n3. Edit Phone\n4. Show all phones\n5. Exit")
def add_phone(brand, model):
    list_of_phone.append(Phone(brand, model))
    print("\n"*25 +"Phone added successfully!")
def delete_phone():
    print_list()
    choice = int(input("Enter phone index: "))
    del list_of_phone[choice-1]
    print("\n"*25 +"Phone removed successfully!")
    return
def modify_phone(index, brand, model):
    list_of_phone[index-1].modify(brand, model)
    print("\n"*25 +"Phone modified successfully!")
    return
def print_list():
    i = 0
    print("List of phones:")
    for phone in list_of_phone:
        print(f"{i+1}. {phone}")
        i+=1
list_of_phone = []
while True:
    print_menu()
    choice = input("Enter Choice: ")
    if choice == "1":
        add_phone(input("Enter phone brand: "), input("Enter phone model: "))
    elif choice == "2":
        delete_phone()
    elif choice == "3":
        print_list()
        modify_phone(int(input("Enter phone index: ")), input("Enter new brand name: "), input("Enter new brand model: "))
    elif choice == "4":
        print_list()
    elif choice == "5":
        break
    else: print("Invalid Input!")
