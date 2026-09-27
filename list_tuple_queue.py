# Super30 Python - Task: List, Tuple and Queue Introduction
# Author: Sagarika Chakraborty

# ==========================================================
# LIST  -  ordered, can be changed, duplicates allowed . #List supports:append(),pop(),extend()
# ==========================================================

#List
#list is a built-in collection in Python used to store multiple values in a single variable.

my_skill= ["AI", "ML", "Python", "SQL", "Data Science"]
print(my_skill)

#append() is used to add one element at the end of a list.
my_skill.append("Deep Learning")
print(my_skill)

#insert() is used to add an element at a specific index and value in a list.
my_skill.insert(2, "NLP")
print(my_skill)

my_skill.remove("SQL")
print(my_skill)

#pop() method removes the element at the specified index. It also returns the removed element.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers.pop(3)
print(f"After removing element at index 3: {numbers}")

#pop() method removes the last element from the list if no index is specified. It also returns the removed element.
numbers.pop()
print(f"After removing last element: {numbers}")

#sort() method sorts the list in ascending order by default. It modifies the original list.
Marks = [ 100, 40,90, 60,40, 20, 10, 80, 70, 30, 50]
Marks.sort()
print(f"After sorting the list: {Marks}")

#reverse() method reverses the order of the list. It modifies the original list.
Marks.reverse()
print(f"After reversing the list: {Marks}")

Marks.sort(reverse=True)
print(f"After sorting the list in descending order: {Marks}")

Marks.sort(reverse=False)
print(f"After sorting the list in ascending order: {Marks}")

#count() method returns the number of occurrences of a specified element in the list.
print(f"Count of 40 in the list: {Marks.count(40)}")

#extend() method is used to add multiple elements to the end of a list. It takes an iterable (like a list, tuple, or set) as an argument and adds each element of that iterable to the end of the list.
Marks.extend([20,50])
print(f"After extending the list: {Marks}") 

#append() vs extend() method:
#append() adds its argument as a single element to the end of a list,
# while extend() iterates over its argument adding each element to the list, extending the list.
L= [3, 4, 5 ]
L.append([140, 170])

print(f"After appending an element: {L}")

L.extend([140, 170])
print(f"After extending the list: {L}")
#count is shown for the list L  index 1 occurence 1
print(f"Count of 4 in the list: {L.count(4)}")
m=[40, 60, 70, 80, 90]
m[3]= 100
print(f"After updating the list: {m}")
m.clear()
print(f"After clearing the list: {m}")
#batch student 



# ==========================================================
# TUPLE  -  ordered, cannot be changed (fixed data), #Tuple is a built-in collection in Python used to store multiple values in a single variable.
# ==========================================================


my_tuple= ("Arpita", "Sagarika", "Rahul", "Rohit", "Riya")
print(my_tuple)
#my_tuple.append("Amit")  # This will raise an AttributeError because tuples are immutable and do not have an append method.
print(my_tuple.count("Sunita"))  # This will return 0 because "Sunita" is not in the tuple.
print(f"Count of Riya in the tuple: {my_tuple.count('Riya')}")  # This will return 1 because "Riya" appears once in the tuple.
print(f"Index of Riya in the tuple: {my_tuple.index('Riya')}")  # This will return the index of "Riya" in the tuple, which is 4.


# ==========================================================
# QUEUE  -  first in, first out (FIFO). Python has no built-in queue type; here a list is used as a queue.
# ==========================================================


customer_queue = ["Arpita", "Sagarika", "Rahul", "Rohit"]
print("\nCustomer queue now :", customer_queue)
print("Who is served first :", customer_queue[0])
print("Index:", customer_queue.index("Arpita"))


task_queue = ["Task1", "Task2", "Task3", "Task4"]
print(f"Initial Queue: {task_queue}")
task_queue.append("Task5")
print(f"After modify:{task_queue}" )
#remove from right/end
remove =task_queue.pop(4)
print(f"modify element: {remove}")
#Task5

task_queue.extend(["Task7", "Task8"])
print(task_queue)


# ==========================================================
# DEQUE:#deque  supports append(), pop(), and extend().
#Deque additionally supports:appendleft(),popleft(),extendleft()

# ==========================================================



#need to convert from list to deque  when need  to remove first element of list
from collections import deque

task_queue = deque(["Task1", "Task2", "Task3", "Task4"])

remove_first = task_queue.popleft()

print(remove_first)



#You use deque when you need a queue where adding/removing from the front and back should be efficient.
queue_items= deque()

result = queue_items.appendleft("AI")
print(result)
queue_items.append("Python")
queue_items.append("LLM")
queue_items.append(".NET")
queue_items.append("React")
print(queue_items)
#deque(['AI', 'Python', 'LLM', '.NET', 'React'])
#append() and appendleft() modify the deque in-place and return None.

queue_items.popleft()
print(queue_items)
#popleft() removes the first/leftmost element.


queue_items.pop()
print(queue_items) 
#remove the Right / End element

#Add multiple items to right
queue_items.extend(["JAVA", "Oracle"])
print(queue_items)



#Add multiple items to left
#extendleft() adds items one by one to the left, so they end up in reverse order: JAVA, Next.js, ...
queue_items.extendleft(["Next.js", "JAVA"])
print(queue_items)
#counting the occurance
print(queue_items.count("JAVA"))




















