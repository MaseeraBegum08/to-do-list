def main():             #creating a function
    tasks = []      #creating an empty list

    while True:
        print("\n===== To-Do List =====")           #list of actions to do
        print("1. Add Task")                        #to add a task to list
        print("2. Show Tasks")                      # to show the task
        print("3. Mark Task as Done")               # to mark it as done
        print("4. Exit")                             # to exit the iteration

        choice = input("Enter your choice: ")       #making a choice

        if choice == '1':                       # if selection is "1" block of code executes
            print()                                         # to print the choice
            n_tasks = int(input("How may task you want to add: "))      #to add how many task the user wants to enter
            
            for i in range(n_tasks):#use of for loop to add the specified number of task
                task = input("Enter the task: ")#ask the user to enter the descrption of the task
                tasks.append({"task": task, "done": False})# the user enters a description, and we add that task to our tasks list along with a status of “Not Done.”
                print("Task added!")#confirm tthat the task has been added

        elif choice == '2':#check if the user chose 2 option
            print("\nTasks:")#print the header for the task list
            for index, task in enumerate(tasks):#loop through each task displaying its index,descrption and status
                status = "Done" if task["done"] else "Not Done"##set the status based on whether the task is done or not
                print(f"{index + 1}. {task['task']} - {status}")#print the task with its number,descrption and status

        elif choice == '3':#check if the user chose option 3 to mark a task as done
            task_index = int(input("Enter the task number to mark as done: ")) - 1#prompt the user for the task number to mark as done and adjust for 0based indexing
            if 0 <= task_index < len(tasks):#check if the entered index is within the valid range of tasks
                tasks[task_index]["done"] = True#mark the task as done by setting"done" to true
                print("Task marked as done!")#confirm that the task has been marked as done
            else:
                print("Invalid task number.")#print an error if the task number is invalid 

        elif choice == '4':#check if the user chose option 4 to exit the program
            print("Exiting the To-Do List.")#printing a statement indicating that the program is existing
            break#break the loop to end the program

        else:#handle any invalid input from the user
            print("Invalid choice. Please try again.")#print an error message if the choice is not one of th options
#check if this script is being run directly(not imported)
if __name__ == "__main__":
    main()#call  the main function to start the program
    