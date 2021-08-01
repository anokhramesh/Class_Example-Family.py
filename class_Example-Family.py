class Family:  # Created a class name Family

    def __init__(self, name, age, place):  # Adding methods/attributes in to  class
        self.name = name
        self.age = age
        self.place = place

    def show_age(self):  # Function for Show age
        print("Age of ",(self.name)," is " + str(self.age) + " years.")
    def show_name(self):  # Function for Show name
        print("Name of Member is "+ str(self.name))
    def set_partner(self, partner):  # Function for set partner
        self.partner = partner
        partner.partner = self
    def show_place(self):
        print("Place of ", (self.name),"is "+(self.place))

Memb1 = Family("Ramesh", 50,"Mallassery")#Created an object Memb1 and passed two argument -Name  and age
Memb2 = Family("Latha", 45,"Konny") #Created an object Memb2 and passed two argument -Name and age
Memb3 = Family("Mohan", 58,"Kottayam") #Created an object Mebm3 and passed twoed argument -Name and age
Memb4 = Family("Suma", 55,"Thengumcavu") #Created an object Memb4 and passed two argument Name and age

Memb1.set_partner(Memb2)  # Calling set_partner Function and assigning Memb1 is partner of Memb2
Memb3.set_partner(Memb4)  # Calling set_partner Function and assigning  Memb3 is partner of Memb4

Memb1.show_name()# Calling show_age function to show the name of Memb1
Memb2.show_name()# Calling show_age function to show the name of Memb1
Memb3.show_name()# Calling show_age function to show the name of Memb3
Memb4.show_name()# Calling show_age function to show the name of Memb4

Memb1.show_age()# Calling show_age function to show the age of Memb1
Memb2.show_age()# Calling show_age function to show the age of Memb2
Memb3.show_age()# Calling show_age function to show the age of Memb3
Memb4.show_age()# Calling show_age function to show the age of Memb4
Memb1.show_place()# Calling show_place function to show the place of Memb1
Memb2.show_place()# Calling show_place function to show the place of Memb2
Memb3.show_place()# Calling show_place function to show the place of Memb3
Memb4.show_place()# Calling show_place function to show the place of Memb4
Memb1.partner.show_name()  # Calling show_name function to show the name of partner Memb1
Memb2.partner.show_name()  #Calling show_age function to show the age  of partner Memb1
Memb3.partner.show_name()#Calling show_name function to show the name  of partner Memb3
Memb4.partner.show_name()#Calling show_name function to show the name  of partner Memb4