#Student Learning profile

#String : string is used to store text
student_name= "Sagarika"
print("Student name:",student_name )

#List : List stores multiple values .List is ordered , mutable and allows the duplicate values
learning_topics= ["Python", "Ai", "SQL", "Ai"]
learning_topics[1]= "React.js"
print("learning topics:", learning_topics )

#Tuple : Tuple is ordered and immutable
location= (
     "Bangalore",
     "India"
    
)

print("Location:", location)

#Dictionary : A disctionary stores data as key value pairs

student_details= {
    "name": "Sagarika",
    "batch":"Ai Engineering",
    "Goal": "Want to be a AI Engineer"
}
print("Student Details:",student_details )

#SET : Set stores  the unique values
unique_values= {
    "Python",
    "Communication",
    "Problem Solving",
    "Communication"
    
}

print("Unique Values:", unique_values)

#Queue : A list is used here to represent a simple task queue

task_queue= [
    "Learning Python",
    "Complete Assignment",
    "Record Video"
    
]

print("Task Queue: ", task_queue)
print("First Task:",task_queue[0] )