# Super30 Python - Task: Dictionary and Set
# Author: Sagarika Chakraborty


# ---------- DICTIONARY 1 : Student ----------


Student ={
   "Name": "Arpita",
    "Age": 22,
    "City": "Bangalore",
    "Course": "Python"
}
    
print ("Student:" , Student )
print("Name:", Student["Name"])
print("Age:", Student["Age"])
print("City:", Student["City"])
print("Course:", Student["Course"])


    
# ---------- DICTIONARY 2 : Employee ----------
#keys()
#"Returns a view object containing all the keys of the dictionary."
#values()
#Returns a view object containing all the values of the dictionary.
#items()
#Returns a view object containing all the key-value pairs of the dictionary,
# each pair as a tuple in a list.
#.get() 
#"Returns the value of the specified key. If the key does not exist, it returns the default value."

employee = {
    "emp_id": 101,
    "name": "Ram",
    "role": "Engineer",
   
}
print ("Employee:", employee)
print("Employee Role:", employee["role"])
print(employee.get("salary", "not available"))

employee["email"] = "ram12@gmail.com"
print("Employee Email:", employee["email"] )
print ("After update:", employee)

print ("Keys:", list(employee.keys()))
print ("Values:", list(employee.values()))

print ("items:", list(employee.items()))
# returns list of tuples. Using list it is accessed by Index.

#A Dictionary is accessed by key, not by index.
print("items of Dict:", employee.items())

print("Every pair")
for key,value in employee.items():
    print("Key:", key, "Value:", value)


# ---------- SET 1 : Skills ----------
skills = {"Python", "Java", "C++", "SQL"}
print("Skills:", skills)
# ---------- SET 2 : Cities ----------
cities = {"Bangalore", "Chennai", "Hyderabad", "Pune"}
print("Cities:", cities)
# ---------- SET 1 : Additional Skills working with SET ----------
skills.add("AI");
print("After adding AI:", skills)

cities.remove("Pune");
print("After removing Pune:", cities)

# ---------- SET 1 : Uniqueness of SET ----------
#Set is a built-in collection type in Python that stores unique elements.
# If duplicate values are added, the set automatically keeps only one occurrence
attendance = {"Rahul", "Sagarika", "Rahul", "Amit", "Rahul"}
print("Attendance:", attendance)


