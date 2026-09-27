# My Student Profile - Variables and Basic Data Types

# str (string) - text, written inside quotes
name = "Rashmika"
city = "Bangalore"
course = "Python Programming"
current_role = ".NET Developer"
learning_goal = "Build AI applications with Python"

# int (integer) - whole numbers, no decimal point
age = 28
experience_years = 5
graduation_year = 2019

# float - numbers with a decimal point
height = 5.4
attendance_percentage = 92.5

# bool (boolean) - only True or False
is_student = True
is_working = True

# Print each value
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)
print("Current role:", current_role)
print("Experience (years):", experience_years)
print("Graduation year:", graduation_year)
print("Height:", height)
print("Attendance %:", attendance_percentage)
print("Learning goal:", learning_goal)
print("Is student:", is_student)
print("Is working:", is_working)

print()

# type() tells us the data type of a variable
print("Data types")
print("name ->", type(name))
print("age ->", type(age))
print("height ->", type(height))
print("is_student ->", type(is_student))

print()

# Variables can change: reassign a new value
experience_years = experience_years + 1
print("Experience next year:", experience_years)
