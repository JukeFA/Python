# my_phonebook = {'Roger':3886, 'Scott':2088}
# my_phonebook['Christian'] = 3646
# my_phonebook['Jared'] = 4333

# print (my_phonebook)

# print (my_phonebook['Christian'])

# print (my_phonebook['Paul'])

ingredient_list = []

def recipe():
    again = 'y'


    while again =='y':
        ingredient = input('Enter ingredient: ')
        amount = input('Enter amount needed: ')

        ingredient_list[ingredient] = amount
        print('Do you want to add another ingredient?')
        again = input('y = yes, anything else = no: ')
        print()

    print('Here are the ingredients you entered.')
    for name in ingredient_list:
        print(ingredient)

recipe()