class shop:
    def __init__(self):
        self.load_products()

    def load_products(self):
        self.products = {
            'HOME': {
                'Air Fryer': 3500,
                'Microwave Oven': 7500,
                'Blender': 1800,
                'Electric Kettle': 1200,
                'Dinner Set': 2400,
                'Non-stick Cookware': 2800,
                'Vacuum Cleaner': 6000
            },

            'TOYS': {
                'Lego Set': 1800,
                'Remote Car': 1200,
                'Dollhouse': 3000,
                'Puzzle Game': 600,
                'Building Blocks': 900,
                'Story Books': 450,
                'Coloring Kit': 300
            },
            'BOOKS': {
                'Python Programming': 600,
                'Data Science Handbook': 900,
                'Children’s Encyclopedia': 750,
                'Exam Preparation Guide': 500,
                'Fiction Novel': 400,
                'Biography': 350,
                'Notebook Pack': 150
            },
            'GADGETS': {
                'Smart Bulb': 850,
                'Smart Plug': 1100,
                'Alexa Echo Dot': 4500,
                'Wireless Charger': 1200,
                'Smart Doorbell': 6000,
                'Security Camera': 3800,
                'GPS Tracker': 2000
            },

        }

        self.username = "sumit"
        self.password = 1234
        self.balance = 50000  # Assume
        self.logged_in = False
        self.Totalamount = 0

        self.admin_name = "sumit"
        self.admin_password = 1234
        self.admin_logged_in = False

        self.payment_method = ""
        self.item = ""
        self.price = 0
        self.quantity = 0
        self.total = 0
        self.gst_percent = 0
        self.gst_amount = 0
        self.final_amount = 0
        
        self.upi_pin=1234567890
        self.upi_password=1234

        self.list=[]
        self.prd_count=0


    def admin_login(self):
        admin_name = input("Please enter your admin name: ")
        if admin_name == self.admin_name:
            print(f"Right ADMIN {self.admin_name}!")
            password = int(input("Please enter your password: "))
            if password == self.admin_password:
                print(f"Access Granted!")
                self.admin_logged_in = True

            else:
                print(f"Wrong Password!")
        else:
            print(f"Wrong Username!")

    def user_login(self):
        user = input("Enter the Username :")
        pwd = int(input("Enter the Password :"))
        if user == self.username and pwd == self.password:
            self.logged_in = True
            print("Login Successful")
        else:
            print("Invalid Login")

    def show_products(self):
        if self.logged_in == True or self.admin_logged_in == True:
            count = 1
            for category, items in self.products.items():
             print(f"{count}.{category}")
             count = count + 1
             cout = 1
             for produt, price in items.items():
                print(f"{cout} {produt} - {price}")
                cout = cout + 1
                print()
        else: 
            print("Login First..........................") 
        

    def show_category(self):
        if self.logged_in == True or self.admin_logged_in == True:
            print("--Available Categories--")
            for category in self.products:
                print(f"- {category}")
                print("")
        else:
            print("Login First..................")


    def buy_products(self):
        print("--Available Categories--")
        for cat, items in self.products.items():
            print(f"- {cat}")
        category = input("Enter the Category : ").upper().strip()
        cnt=1
        if category in self.products:
            print("-- Available Products --")
            for items, price in self.products[category].items():
                print(f"{cnt}. {items} - Rs-{price}")
                cnt=cnt+1
                print("-------------------------------")
            self.items = input("Enter the Item you want to add : ").title()
            print(self.products[category][self.items])
            if self.items in self.products[category]:
                self.list.append(self.items)
                self.prd_count=self.prd_count + 1
                self.quantity = int(input("Enter the Quantity : "))

                self.price = self.products[category][self.items]

                self.total = self.price * self.quantity
                if category == "HOME":
                    self.gst_percent = 18
                elif category == "TOYS":
                    self.gst_percent = 12
                elif category == "BOOKS":
                    self.gst_percent = 5
                elif category == "GADGETS":
                    self.gst_percent = 24
                else:
                    self.gst_percent = 0

                self.gst_amount = (self.total * self.gst_percent) / 100
                self.final_amount =self.final_amount + self.total + self.gst_amount
                #
                print(f"Final Amount Of Product Is : {self.final_amount}")
            else:
                print("Product Not Found...")
        else:
            print("Category Not Found...")
    
    def make_payment(self):

        print("Select Payment Method")
        print("1. Phonepe ")
        print("2. Google pay")
        print("3. Credit Card")
        print("4. Cash on Delivery")

        self.choice = input("Enter option number : ")

        if self.choice == "1":
            self.payment_method = "Phonepe"
            pin=int(input("Enter the UPI pin : "))
            if self.upi_pin == pin:
                print("PIN is Correct")
                pas=int(input("Enter the PIN PASSWORD "))
                if self.upi_password == pas:
                    print("-----Correct Pass Code And Thanks For Shopping !!!-----")
                else:
                    print("Wrong PIN")
            else:
                print("Inaccurate PIN A")
        elif self.choice == "2":
            self.payment_method = "Google Pay"
            pin=int(input("Enter the UPI pin : "))
            if self.upi_pin == pin:
                print("PIN is Correct")
                pas=int(input("Enter the PIN PASSWORD "))
                if self.upi_password == pas:
                    print("-----Correct Pass Code And Thanks For Shopping !!!-----")
                else:
                    print("Wrong PIN")
            else:
                print("Inaccurate PIN A")
        elif self.choice == "3":
            self.payment_method = "Credit Card"
            pin=int(input("Enter the UPI pin : "))
            if self.upi_pin == pin:
                print("PIN is Correct")
                pas=int(input("Enter the PIN PASSWORD "))
                if self.upi_password == pas:
                    print("-----Correct Pass Code And Thanks For Shopping !!!-----")
                else:
                    print("Wrong PIN")
            else:
                print("Inaccurate PIN A")
                
        elif self.choice == "4":
            self.payment_method = "Cash on Delivery"
        
        else:

            print("Invalid choice")

            print(f"payment_method is : {self.payment_method}")

    def show_receipt(self):
        print("-------------------------------")
        print("------------RECEIPT------------")
        print(f"ITEMS          : {self.list}")
        print(f"NO OF PRODUCT  : {self.prd_count} ")
        print(f"GST %          : {self.gst_percent} %")
        print(f"AMOUNT         : {self.total}")
        print(f"PAYMENT METHOD : {self.payment_method}")
        print(f"TOTAL AMOUNT   : {self.final_amount}")
        print("-------------------------------")
        
    def home(self):
        while(True):
             print("1. ADMIN LOGIN")
             print("2. USER LOGIN")
             print("3. SHOW CATEGORY")
             print("4. SHOW PRODUCTS")
             print("5. BUY PRODUCTS")
             print("6. PRINT RECEIPT")
             print("7. BALANCE")

             choice = int(input("Enter your Choice Number : "))
             if choice == 1:
                self.admin_login()
             elif choice == 2:
                self.user_login()
             elif choice == 3:
                self.show_category()
                        
             elif choice == 4:
                self.show_products()
             elif choice == 5:
                if self.admin_logged_in == True or self.logged_in == True:
                    self.buy_products()
                    while(True):
                          add=input("Want to add items y/n : ")
                          if add == "y":
                       
                             self.buy_products()
                          else:
                             self.balance=self.balance-self.final_amount
                             self.make_payment()
                             break
                else:
                    print("Login or Admin Login First....................")
                 
             elif choice == 6:
                if self.admin_logged_in == True or self.logged_in == True:
                    self.show_receipt() 
                    self.data.append(self.show_receipt())
                    
             elif choice == 7:
                print(f"Current Balance = {self.balance}")
             

             else:
                print("Login or Admin Login First....................")
       
        
       



p1 = shop()
# p1.admin_login()
# p1.user_login()
# p1.show_category()
# p1.show_products()
# p1.make_payment()
# p1.buy_products()
# p1.show_receipt()
p1.home()

