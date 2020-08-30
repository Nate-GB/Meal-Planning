import random

#prints into the command line 7 meals for the week

mealsForTheWeek = []
mealList = ['Creamy Pasta', 'Tacos', 'Burgers','Frozen Asian Chicken','Chicken Adobo','Frozen Pizza','Udon Stir-Fry','Eat Out','Quiche','Yogurt','Congee','Pancakes','Grilled Cheese', 'Omellete', 'Omellete Rice']


while len(mealsForTheWeek) < 7:
    mealDecider = int(random.randint(0, (len(mealList)-1)))
    if mealList[mealDecider] not in mealsForTheWeek:
        mealsForTheWeek.append(mealList[mealDecider])
        if 'Frozen Asian Chicken' in mealsForTheWeek:
           if 'Fried Rice' not in mealsForTheWeek:
                mealsForTheWeek[mealsForTheWeek.index('Frozen Asian Chicken')] = 'Fried Rice'
                mealsForTheWeek.append('Frozen Asian Chicken')
           else:
                if 'Fried Rice' not in mealsForTheWeek:
                        mealsForTheWeek[mealsForTheWeek.index('Frozen Asian Chicken')] = 'Fried Rice'
                        mealsForTheWeek.append('Frozen Asian Chicken')
        if 'Chicken Adobo' in mealsForTheWeek:
            if 'Fried Rice' not in mealsForTheWeek:
                mealsForTheWeek[mealsForTheWeek.index('Chicken Adobo')] = 'Fried Rice'
                mealsForTheWeek.append('Chicken Adobo')
            else:
                if 'Fried Rice' not in mealsForTheWeek:
                    mealsForTheWeek[mealsForTheWeek.index('Chicken Adobo')] = 'Fried Rice'
        
print(mealsForTheWeek)