#datatypes
#numbers
firstNumber=1

secondNumber=2
anyNumber=12000


#boolean
true_boolean=True
false_boolean=False

#Float
decimalNumber = 11.80

#String

myName="Deepak"

print(firstNumber, secondNumber, anyNumber, true_boolean, false_boolean, decimalNumber, myName)

#list
list_of_numbers=[1,3,4,5]
print('the list is ', list_of_numbers)
print('index at 3', list_of_numbers[3])
#append function

#tuples
tuple_numbers=(2,5,6,7)
print('index at 3', tuple_numbers[3])
#dict

dict_example={'key1':'value1',
'key2': 'value2'}

print('dict is ', dict_example['key2'])

#% is used for formatting
for key in dict_example:
    print("%s --> %s" %(key, dict_example[key]))
# % is for formatting

for key, value in dict_example.items():
						print("%s --> %s" %(key, dict_example[key]))


#set
#frozenset
