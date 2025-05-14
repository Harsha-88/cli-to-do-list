# step 1
# create a empty list to store all the task
# each task will be in dictionary with two keys name and done
tasks=[]

# step 2
# function to show men to user
def show_menu():
    print("\n======= TO-DO LIST MENU =======")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit the app")
    print("================================")


# Step 3: Function to display the current list of tasks
# function to show all task in to do list 
def view_tasks():
    if len(tasks) == 0:
        print("You have no tasks yet!")
    else:
        print("\nYour Tasks:")
        # loop will go through task one by one 
        for i in range(len(tasks)):
            task = tasks[i]  # Get the task from the list
            # Show a check mark if done, or a cross if not done
            status = "✅ Done" if task["done"] else "❌ Not Done"
            # i+1(show task no),task[name](show task name),[status](shows or not )
            print(f"{i + 1}. {task['name']} --> {status}")

# Step 4: Function to add a new task
def add_task():
    name=input("Enter a task name: ") #used  to ask user 
    task={"name": name,"done":False}
    tasks.append(task) #add task in to do list
    print(f"Task '{name}'added successfully!")



 #step 5:func to mark a task as completed 
def mark_task_complete():
  #show task so user know which no to pick  
    view_tasks()
    number=int(input("Enter the task no to mark as complete"))
    
    #check if no is valid or not 
    #Not less than 1 and Not more than total tasks (len(tasks)). indexing from 0
    if 1<=number<=len(tasks):
        tasks[number-1]["done"]=True # Update the 'done' status to True
        print(f"Task '{tasks[number - 1]['name']}' marked as completed!")
    else:
        print("Invalid task number. Please try again.")




# ❌ Step 6: Function to delete a task
def delete_task():
    view_tasks()  # Show tasks so user can choose one
    number = int(input("Enter the task number to delete: "))

    # Check if the number is valid
    #❗ Remember: although the user sees task 1, 2, 3 —  internally Python uses index 0, 1, 2
    if 1 <= number <= len(tasks):
        removed_task = tasks.pop(number - 1)  # Remove the task from the list bu using pop operation
        print(f"Task '{removed_task['name']}' has been deleted.")
    else:
        print("Invalid task number. Please try again.")





# 🧠 Step 7: The main loop that keeps the program running and “Keep showing the menu again and again, until the user chooses to exit.”
while True:
    show_menu()  # Show menu options
    choice = input("Enter your choice (1-5): ")  # Ask user what they want to do

    # Check what the user entered and call the right function
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thanks for using the To-Do List App. Goodbye!")
        break  # Exit the loop and end the program
    else:
        print("Invalid input. Please enter a number between 1 and 5.")