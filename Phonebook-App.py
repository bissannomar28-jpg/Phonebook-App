import json
try:
    with open("phonebook.json", "r", encoding="utf-8") as file:
        phone_book = json.load(file)
except FileNotFoundError:
    phone_book = {"1111111111" :"Amal" ,"2222222222": "Mohammed",

"3333333333": "Khadijah",

"4444444444": "Abdullah",

"5555555555": "Rawan",

"6666666666": "Faisal",

"7777777777": "Layla"}

user_number = input("enter your phone number:")

if len(user_number)!= 10 or not user_number.isdigit():

 print("This is invalid number")

elif user_number in phone_book:

 print(phone_book[user_number])

else:

 print("Sorry, the number is not found")

search_name = input("enter name to search:")

for num , name in phone_book.items():

 if name == search_name:

  print("phone number is :" , num)

new_name = input("enter new name :")

new_number = input("enter new number :")

phone_book[new_number] = new_name
with open("phonebook.json", "w", encoding="utf-8") as file:
 json.dump(phone_book, file, ensure_ascii=False, indent=4)


