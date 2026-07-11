tasks = []    # this list holds all the task text

# keep showing the menu until the user chooses to quit
while True: 
  print("")
  print("===== To-Do List =====")
  print("1. View tasks")
  print("2. Add a task")
  print("3. Delete a task")
  print("4. Quit")
  
  option = input("Choose 1-4: ")  # what the user typed, as text

  # -----view-----
  if option == "1":
    if len(tasks) == 0:
      print("Your list is empty.")
    else:
      # go through each task and print it with a number
      for i in range(len(tasks)):
        # i starts at 0, so we add 1 for human-readable numbers
        print(str(i + 1) + ". " + tasks[i])

  # -----add-----
  elif option == "2":
    new_task = input("Enter the task: ")
    tasks.append(new_task)
    print("'" + new_task + "' has been added.")

  # -----delete-----
  elif option == "3":
    if len(tasks) == 0:
      print("Your list is empty. Nothing to delete.")
    else:
      # Show the current list first so the user knows what to choose
      print("Current tasks:")
      for i in range(len(tasks)):
        print(str(i + 1) + ". " + tasks[i])
      
      # Use try/except to catch mistakes if they type letters or invalid numbers
      try:
        choice = int(input("Enter the number of the task to delete: "))
        # Subtract 1 because Python lists start counting at 0
        removed = tasks.pop(choice - 1)
        print("'" + removed + "' has been deleted.")
      except (ValueError, IndexError):
        print("Invalid number. No task was deleted.")

  # -----quit-----
  elif option == "4":
    print("Goodbye!")
    break  # This breaks out of the while loop and ends the program
    
  # -----invalid input handler-----
  else:
    print("Invalid option. Please type a number from 1 to 4.")
