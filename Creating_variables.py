name = "Steve"
country = "United States"

age = 25
satisfied = True

hourly_wage = 20
daily_wage = hourly_wage * 8

print("I am " + str(age) + "years old.")
print("I make " + str(daily_wage) + "dollars per day.")




grocery_list = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]

print(grocery_list)
grocery_list.append("coffee")
grocery_list.remove("Jelly")



info_dict = {"name": "watson", "age": "10", "hobbies": ["sleeping", "barking"], 
"wake-up": {"Sunday": "10am", "Monday": "8am", "Tuesday": "8"}}

print(info_dict["age"])
print(info_dict["name"])
print(info_dict)