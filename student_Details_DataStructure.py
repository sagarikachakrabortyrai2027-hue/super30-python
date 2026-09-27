# My Student Profile - Python Data Structures
from collections import deque

# String - text inside quotes
student_name = "Sagarika"
print("String:", student_name)
print("Type:", type(student_name))
print()

# List - ordered, changeable, allows duplicates, uses [ ]
learning_topics = ["Python", "SQL", "Git", "GitHub"]
learning_topics.append("Machine Learning")      # add at the end
print("List:", learning_topics)
print("First topic:", learning_topics[0])
print("Type:", type(learning_topics))
print()

# Tuple - ordered, cannot be changed after creation, uses ( )
location = ("Sarjapur", "Bangalore", "India")
print("Tuple:", location)
print("City:", location[0])
print("Type:", type(location))
print()

# Dictionary - key: value pairs, uses { }
student_details = {
    "name": "Sagarika",
    "current_role": "Technical Lead Developer",
    "experience_years": "6+",
    "goal": "AI Engineer"
}
student_details["course"] = "Python for AI"     # add a new key
print("Dictionary:", student_details)
print("Goal:", student_details["goal"])
print("Type:", type(student_details))
print()

# Set - unordered, no duplicates, uses { }
unique_skills = {"C#", "SQL", "Python", "Communication", "Python"}
unique_skills.add("Git")
print("Set:", unique_skills)                    # "Python" appears only once
print("Knows SQL?", "SQL" in unique_skills)
print("Type:", type(unique_skills))
print()

# Queue - First In, First Out (FIFO)
task_queue = deque(["Learn Python basics", "Complete assignment", "Record video"])
task_queue.append("Upload to YouTube")          # join at the back
print("Queue:", list(task_queue))

done = task_queue.popleft()                     # leave from the front
print("Finished:", done)
print("Remaining tasks:", list(task_queue))
print("Next task:", task_queue[0])
