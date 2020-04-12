#length of list
list1 = range(2, 20, 3)
list1_len=len(list1)
print(list1_len)

#callling specific elemts
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4=(employees[4])
print(len(employees))
print(employees[6])

#calling elementspt 2
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))

last_element=shopping_list[-1]

element5=shopping_list[5]
print(last_element)
print(element5)
#slicing lists
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
#2nd index number is not included
beginning = suitcase[0:4]
print(beginning)

middle = suitcase[2:4]

#can omit first or second number depending on beginning or end
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[-2:]
#counting lists
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes= votes.count('Jake')

print(jake_votes)


#sorting lists
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
sorted_addresses=addresses.sort()
print(sorted_addresses)
print(addresses)
### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
sorted_names=names.sort()
print(names)

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
#sorts alphabetically
sorted_cities = cities.sort()
print(sorted_cities)
print(cities)

#using sorted function(better way): result is alpabetical
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted=sorted(games)
print(games)
print(games_sorted)