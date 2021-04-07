from Food import *

if (__name__) == '__main__':

    f = Food(1, 'pork', 'nonveg', 599)  # Adding pre-menu to Restaurant for Testing purpose
    g = Food(2, 'parota', 'nonveg', 97)
    h = Food(3, 'chicken_biriyani', 'nonveg', 300)
    i = Food(4, 'rice_plough', 'veg', 179)
    j = Food(5, 'manchurian', 'veg', 38)
    f.foods.append(f)
    f.foods.append(g)
    f.foods.append(h)
    f.foods.append(i)
    f.foods.append(j)

    question = 0
    while (question != 10):
        QUE()
        question = int(input("\t"))
        if (question == 1):
            f.addFood()
        elif (question == 2):
            f.updateFood()
        elif (question == 3):
            f.delItem()
        elif (question == 4):
            f.showAllFoods()
        elif (question == 5):
            f.showFoodById()
        elif (question == 6):
            f.showFoodByName()
        elif (question == 7):
            f.showFoodByType()
        elif (question == 8):
            f.sortFoodByName()
        elif (question == 9):
            f.sortFoodByPrice()
        elif(question==10):
            print("\n(:.........Bye-Bye\n\t\t\tAnd \n\t\t\tThanks for Reviewing My Code Sir.......:)")
            quit()
        else:
            print("\n(-_-)------------Invalid input------------(-_-)\n")

