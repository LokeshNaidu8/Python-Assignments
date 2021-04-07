class Food:
    hotelName = "Lew's Restaurant"

    def __init__(self, id=0, name=None, type='veg', price=0):
        self.__id = id
        self.name = name
        self.type = type
        self.price = price
        self.foods = []

    def __str__(self):
        return '----------------------------\n{}, {}, {}, {}'.format(self.__id, self.name, self.type, self.price)

    def getId(self):  # Fetching food's private id'
        return self.__id

    def addFood(self):  # Adding New Food
        print('\n------------You have entered Add Food section --------------\n')
        again = 'y'
        while (again == 'y'):
            try:
                id = int(input("Enter id for your food :"))
                name = input("Enter the food name : ").lower()
                type = int(input("Enter the type of food----Enter the corresponding number \n1:Veg\n2:NonVeg  "))
                if (type == 1):
                    type = 'veg'
                elif (type == 2):
                    type = 'nonveg'
                price = int(input("Enter price of your food : "))
                f = Food(id, name, type, price)  # adding new food
                self.foods.append(f)
                again = 'n'
            except:
                print("\n@#$@#$@$#----------You have Entered wrong input----------@#$Q$%#$2\n")
                again = input('Want to continue with adding new food\nSay y/n : ').lower()

    def showAllFoods(self):  # Listing all the foods
        print("\n------ :) ---------Food Menu--------- (: --------")
        for i in self.foods:
            print(i)

    def showFoodById(self):  # Show food by id
        print('\n--------You have entered show food by ID section-------\n')
        try:
            id = int(input("Enter food id to View particular food : "))
            for i in self.foods:
                if (id == i.getId()):
                    print('\n------(: We got the food which has id', id, ':)------')
                    print("Id:", i.getId(), "\nName:", i.name, "\nType: ", i.type, "\nPrice: ", i.price)
                    break
            else:
                print("\n----------Food Not Found with id ", id, "----------\n")
        except:
            print("\n@#$@#$@$#----------You have Entered wrong input----------@#$Q$%#$2\n")

    def showFoodByName(self):  # Show food by name
        print('\n--------You have entered show food by NAME section-------\n')
        try:
            print("Caution: See to it that you're entering correct name.....\n")
            name = input("Enter food name to check whether food is present in Menu or not: ").lower()
            for i in self.foods:
                if (name == i.name):
                    print("\n", name, " is found in Menu list with")
                    print("Id: ", i.getId(), "\nName: ", i.name, "\nType: ", i.type, "\nPrice: ", i.price)
                    break
            else:
                print("\n----------Food Not Found with id ", id, "----------\n")

        except:
            print("\n@#$@#$@$#----------Invalid Input----------@#$Q$%#$2\n")

    def showFoodByType(self):  # Show food by type
        print("---------You have entered to filter out the food by Veg or Non-veg section---------")
        try:
            t = int(input("Enter the corresponding number to filter out foods by its type \n1: Veg items\n2: Non-veg items: "))
            if (t == 1):
                print("\n---------------(:You have choosed to print all VEG Foods in Menu :)------------------\n")
                for i in self.foods:
                    if (i.type == 'veg'):
                        print("-------------------\nId: ", i.getId(), "\nName: ", i.name, "\nPrice: ", i.price)
            elif (t == 2):
                print("\n---------------(:You have choosed to print all NON-VEG Foods in Menu :)------------------\n")

                for i in self.foods:
                    if (i.type == 'nonveg'):
                        print("-------------------\nId: ", i.getId(), "\nName: ", i.name, "\nPrice: ", i.price)

        except:
            print("\n@#$@#$@$#----------Invalid Input----------@#$Q$%#$2\n")

    def sortFoodByName(self):  # Sorting with the name
        print("\n-------------Sorting Food by NAME -------------\n")
        l = []
        for i in self.foods:
            l.append(i.name)
        l.sort()
        for i in l:
            for j in self.foods:
                if (i == j.name):
                    # t=(j.name,j.type,j.price)
                    print("---------\nFoodName: ", j.name, "\nType: ", j.type, "\nPrice: ", j.price)

    def sortFoodByPrice(self):
        print("\n----------------Sorting food by price-----------------\n")
        sor = int(input(
            "Enter the corresponding number to sort the food items by PRICE:\n1: Price Low to High\n2: Price High to Low :"))
        if (sor == 1):
            print(
                "\n-----------------------Here are the list of Foods sorted by Price LOW to HIGH-----------------------")
            l = []
            for i in self.foods:
                l.append(i.price)
            l.sort()
            for i in l:
                for j in self.foods:
                    if (i == j.price):
                        print("---------\nFoodName: ", j.name, "\nType: ", j.type, "\nPrice: ", j.price)
        elif (sor == 2):
            print(
                "\n-----------------------Here are the list of Foods sorted by Price HIGH to LOW -----------------------")

            l = []
            for i in self.foods:
                l.append(i.price)
            l.sort(reverse=True)
            for i in l:
                for j in self.foods:
                    if (i == j.price):
                        print("---------\nFoodName: ", j.name, "\nType: ", j.type, "\nPrice: ", j.price)

    def delItem(self):
        print("\n(-_-)----------------------Deleting single Food Item section------------------------(-_-)\n")
        print("Displaying foods that you want to delete......\n")
        for i in self.foods:
            print(i)
        try:
            foodID = int(input("\nPlease enter Food ID to delete that product: "))
            for i in self.foods:
                if (foodID == i.getId()):
                    ind = self.foods.index(i)
                    print("------------------", i.name, "is deleted---------------\n")
                    self.foods.pop(ind)
                    break
            else:
                print("\n(-_-)-----------Id Not Found----------(-_-)\n")
        except:
            print("\n@#$@#$@$#----------Invalid Input----------@#$Q$%#$2\n")

    def updateFood(self):
        print("\n---------------Updating Food section------------------\n")
        print("Displaying food that you want to update.......")
        for i in self.foods:
            print(i)
        id = int(input("\nEnter the Food ID to update that particular item : "))
        for i in self.foods:
            if (id == i.getId()):
                print("\n------------- You have chosen ", i.name, "for updating ---------------")
                what = int(input("\nEnter what you want to update : \n1: Food Name\n2: Food Type\n3: Price"))

                if (what == 1):
                    newName = input("\nEnter New Name for your food : ")
                    i.name = newName
                    print("\nFood name is updated to ", newName)
                    break

                elif (what == 2):
                    foodty = int(input("\nEnter corresponding number to change your Food type :\n1: Veg\n2: Non-veg"))
                    if (foodty == 1):
                        foodty = 'veg'
                    else:
                        foodty = 'nonveg'

                    i.type = foodty
                    print("(:-----", i.name, " type is updated to ", foodty, "------:)")
                    break
                elif (what == 3):
                    newPrice = int(input("\nEnter Amount to update your price: "))
                    i.price = newPrice
                    print("\n(:----------Price is updated to ", newPrice, " ------------:)")


        else:
            print("\n(-_-)-------------No such id found-------------------(-_-)\n")


'''---------------------------------------------------------------------------------------------'''
print('\n-_-_-_-_-_-_-_-_-_-_ WELCOME TO ',Food.hotelName,' -_-_-_-_-_-_-_-_-_-_')
print("\n(: Make sure to enlarge the result window for Better Experience.........")
'''---------------------------------------------------------------------------------------------'''


def QUE():
    print("\nOperations that you can perform in our Restaurant:\n"
          "\t1: Adding New Food Item\n"
          "\t2: Updating Existing Food item\n"
          "\t3: Deleting Food Item\n"
          "\t4: Show All The Foods\n"
          "\t5: Show Food by Id\n"
          "\t6: Show Food by Name\n"
          "\t7: Show Food by Type\n"
          "\t8: Sort Food by Name\n"
          "\t9: Sort Food by Price\n"
          "\t10: EXIT ")
