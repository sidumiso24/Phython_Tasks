#task_manager.py
#written by: Sidumiso Debbie Mabaso
#date: 25 March 2020
#function: This program manages tasks assigned to each member of the team and the registration of new users

#defining in 'reg_user' function
def reg_user():

    #displaying message to the user
    print("User Registration: ")

    #space or new empty line
    print()

    #if 'userName' is equal to 'admin' then the following:
    if userName == "admin":

        #opening 'user.txt' text file in a variable called 'userFile'
        userFile = open("user.txt", "r")

        #asks user for input
        newUser = input("Please enter a username: ")

        #space or new empty line
        print()

        #boolean called 'correct' as False 
        correct = False
    
        #a for loop that reads in the 'userFile' text file
        for line in userFile:

            #stripping 'line' in a variable called 'line1'
            line1 = line.strip()

            #splitting the comma and the space in 'line1' in a variable called detail
            detail = line1.split(", ")

            #if 'newUser' is not equal to 'detail[0]' then boolean 'correct' is False, else the boolean 'correct' is True
            if newUser != detail[0]:

                correct = False

            else:

                correct = True

            #a while loop is 'correct' the following executes
            while correct:

                #displaying a valid message to the user
                print("The username you've entered already exists. Please enter a different username.")

                #space or new empty line
                print()

                #opening 'user.txt' text file in a variable called 'userFile'
                userFile = open("user.txt", "r")

                #asks user for input
                newUser = input("Please enter a username: ")

                #space or new empty line
                print()

                #boolean called 'correct' as False 
                correct = False
                
                #a for loop that reads in the 'userFile' text file
                for line in userFile:

                    #stripping 'line' in a variable called 'line1'
                    line1 = line.strip()

                    #splitting the comma and the space in 'line1' in a variable called detail
                    detail = line1.split(", ")

                    #if 'newUser' is not equal to 'detail[0]' then boolean 'correct' is False, else the boolean 'correct' is True
                    if newUser != detail[0]:

                        correct = False

                    else:

                        correct = True

                        #a break that terminates the loop
                        break

                #closing the 'userFile' text file
                userFile.close()

        #opening the 'user.txt' file and appending to it into the variable called 'userFileRegist'
        userFileRegist = open("user.txt","a")

        #asks the user for inputs
        newPassword = input("Please enter a password: ")
        passConfirm = input("Please confirm the password: ")

        #if confirmed password is equal to the new password then writes into the 'user.txt' file
        if passConfirm == newPassword:
            userFileRegist.writelines(f"\n{newUser}, {newPassword}")

            #displays message to user informing user that a new user has been registered
            print("User registered.")

            
        else:
            #if input from user does not match the password, displays a this output from user
            print("The password confirmed does not match the password.")

            #space or new empty line
            print()

            #while password confirmed is not equal to the new password, a while loop for user to re-enter information
            while passConfirm != newPassword:

                #asks user for inputs
                newPassword = input("Please enter a password: ")
                passConfirm = input("Please confirm the password: ")
                    
                #if confirmed password is equal to the new password then writes into the 'user.txt' file
                if passConfirm == newPassword:
                    userFileRegist.writelines(f"\n{newUser}, {newPassword}")

                    #displays message to user informing user that a new user has been registered
                    print("User registered.")

        #closing the 'userFileRegist' variable which closes the text file
        userFileRegist.close()

    else:

        #displaying message to user who's username is not 'admin'
        print("Only the admin can is allowed to register users. Please choose another option.")


#defining 'add_task' function
def add_task():

    #opening the 'tasks.txt' file into a variable called 'taskFile' and appending to it
    taskFile = open("tasks.txt", "a")

    #asks inputs from the user
    assignUser = input("Please enter the username of the person the task is assigned to: ")
    taskTitle = input("Please enter the title of the task: ")
    taskDescipt = input("Task description: ")
    dueDate = input("Task's due date (in the form of day, month, year (YYYY-MM-DD): ")
    currentDate = input("Current date (in the form of day, month, year (YYYY-MM-DD): ")
    completeTask = "No"

    #writing the inputs from the user into the task file
    taskFile.writelines(f"\n{assignUser}, {taskTitle}, {taskDescipt}, {dueDate}, {currentDate}, {completeTask} ")

    #displaying message to the user to inform that the the task has been added into the task file
    print("Done!")

    #closing the task file
    taskFile.close()


#defining 'view_all' function
def view_all():

    #opening the 'tasks.txt' file again and reading in the text file
    taskFile1 = open("tasks.txt", "r")

    #a for loop to read in the text file
    for lines in taskFile1:

        #converting the text file into a list and splitting the comma
        task = lines.split(", ")

        #indexing task zero till the end of each line which is up until task five
        name = task[0]
        title = task[1]
        description = task[2]
        dateDue = task[3]
        date = task[4]
        completeness = task[5]

        #displaying the output to the user
        print(f"Task assigned to: {name}\n Task title: {title}\n Task description: {description}\n Task due date: {dateDue}\n Current date: {date}\n Task completion: {completeness}")

    #closing the task file
    taskFile1.close()


#defining the 'view_mine' function
def view_mine():

    #opening the 'tasks.txt' file againg in a variable called 'taskFile2'
    taskFile2 = open("tasks.txt", "r+")

    #reading lines in 'taskFile2' in a variable called 'taskLines'
    taskLines = taskFile2.readlines()

    #displaying message to the user
    print("The following tasks assigned to you are as follows: ")

    #space or new empty line
    print()

    #a for loop that displays the user's tasks
    for number, line in enumerate(range(len(taskLines)), start = 0):

        #splitting the comma and space in 'taskLines' in a variable called 'taskLine'
        taskLine = taskLines[line].split(", ")

        #if 'userName' is equal to "taskLine[0]" then the output is displayed to the user
        if userName == taskLine[0]:

            print(f"Task {number}\n Task assigned to: {taskLine[0]}\n Task title: {taskLine[1]}\n Task description: {taskLine[2]}\n Task's due date: {taskLine[3]}\n Current date: {taskLine[4]}\n Task completion: {taskLine[5]}")

    #closing the task file
    taskFile2.close()

    #a boolean called 'taskEdit' is initialised to False
    taskEdit = False

    #a while loop, while 'taskEdit' is equal to False the following executes
    while taskEdit == False:

        #asks the user for input
        numTask = int(input("Please enter the task number (e.g. 1) to edit the task or '-1' to view the main menu: "))

        #if 'numTask' is equal to '-1' then 'taskEdit' is euqal to True
        if numTask == -1:

            taskEdit = True

        else:
            #opening 'tasks.txt' text file in a variable called 'taskFile3'
            taskFile3 = open("tasks.txt", "r")

            #an empty list
            aList = []

            #reading and splitting lines in 'taskFile3' text file in a variable called 'aList'
            aList = taskFile3.read().splitlines()

            #spliting the comma and space in 'aList' in a variable called 'aListItem'
            aListItem = aList[numTask].split(", ")

            #asks for the user's input
            taskComplete = input("\n Do you wish to mark this task as complete or do you wish to edit? \n Please enter 'c' - complete or 'e' - edit: ")

            #if user enters 'c', then the following executes
            if taskComplete.lower() == "c":

                #'aListItem' initialised to 'Yes' to show the completeness of the task
                aListItem[5] = "Yes"

                #joining the comma and space with 'aListItem' into a variable called 'aListJoin' then initialised into 'aList'
                aListJoin = ", ".join(aListItem)
                aList[numTask] = aListJoin

                #opening  'tasks.txt' text file in a variable called 'taskFile4'
                taskFile4 = open("tasks.txt", "w")

                # for loop that reads in 'aList', the following executes
                for item in aList:

                    #'item' written into 'taskFile4' text file
                    taskFile4.write(f"{item}\n")

                #closing 'taskFile4' text file
                taskFile4.close()

                #displaying output to the user
                print(f"\n Task {numTask} is marked as complete.")

                #boolean ''taskEdit' is True
                taskEdit = True

            #an elif statement if 'taskComplete' is equal to 'e' then the following executes
            elif taskComplete.lower() == "e":

                #if 'aListItem' is equal to 'Yes', then a valid message is displayed to the user
                if aListItem == "Yes":

                    print(f"\nTask {numTask} has been completed therefore you cannot edit it. \n")

                else:
                    
                    #asks for user's input
                    editTask = input("Please enter 'u' to edit the username the task is assigned to or 'd' to edit the task's due date: ")

                    #if 'editTask' is equal to 'u' the following executes
                    if editTask.lower() == "u":
                        
                        #asks for user's input
                        changeUsername = input("\n Please enter the new username: ")

                        #creating a list called 'aListItem' which contains 'changeUsername', comma and space joined in the list called 'aListJoin' and then added to a new list called 'aList'
                        aListItem[0] = changeUsername
                        aListJoin = ", ".join(aListItem)
                        aList[numTask] = aListJoin

                        #opening 'task.txt' text file in a variable called 'taskFile5'
                        taskFile5 = open("tasks.txt", "w")

                        #a for loop for 'item' in 'aList' that writes in 'taskFile5' text file
                        for item in aList:

                            taskFile5.write(f"{item}\n")

                        #closing the 'taskFile5' text file
                        taskFile5.close()

                        #displaying the output to the user
                        print(f"Task {numTask} has been edited. The task has now been assigned to {changeUsername}\n")

                    #else if 'editTask' is equal to 'd' the following executes
                    elif editTask.lower() == "d":

                        #asks input from user
                        modifyDate = input("Please enter a new due date in the form of (YYYY-MM-DD): ")

                        #creating a list called 'aListItem' which contains 'changeUsername', comma and space joined in the list called 'aListJoin' and then added to a new list called 'aList'
                        aListItem[4] = modifyDate
                        aListJoin = ", ".join(aListItem)
                        aList[numTask] = aListJoin

                        #opening the 'tasks.txt' text file in a variable called 'taskFile6'
                        taskFile6 = open("tasks.txt", "w")

                        #a for loop for 'value' in 'aList' which writes in 'taskFile6' text file
                        for value in aList:

                            taskFile6.write(f"{value}\n")

                        #closing the 'taskFile6' text file
                        taskFile6.close()

                        #displaying output to the user
                        print(f"\n Due date for Task {numTask} has been changed. The new due date for the task is {modifyDate}.")

                        break

            #closing 'taskFile3' text file
            taskFile3.close()

#defining the 'statistics' function
def statistics():

    #displaying message to the user
    print("Statistics: ")

    choice = input ("\nPlease enter what you want to see 'users overview' or 'tasks overview'(enter 'u' or 't'):  ")
    # when admin chooses 'users overview', we create a list to store all the lines in the file users_overview.txt.
    # then the reports read from the text file is printed to the user in a user friendly manner.
    if choice.lower() == "u":
        user_overview = open ('user_overview.txt', 'r')
        user_overview_list = user_overview.read().splitlines()
        user_overview.close()
        for line1 in user_overview_list:
            print(line1)      

    # similarly, when the user chooses tasks overview, we create a list containing all the necessary details from the text file and we print the details in a user friendly manner.      
    elif choice.lower() == "t":
        task_overview = open('task_overview.txt', 'r')
        task_overview_list = task_overview.read().splitlines()
        task_overview.close()
        for line in task_overview_list:
            print(line)

#defining a function called 'reports'
def reports():

    #importing date and time
    import datetime
    from datetime import date

    #opening 'tasks.txt' in a variable called 'taskFile8'
    taskFile8 = open("tasks.txt", "r")

    #reading and splitting 'taskFile8' in a variable called 'countTaskList' into a list
    countTaskList = taskFile8.read().splitlines()

    #closing the 'taskFile8' text file
    taskFile8.close()

    #length of 'coutTaskList' in a variable 'lengthOfList'
    lengthOfList = len(countTaskList)

    #counters to be used to count the complete tasks (yesCount), incomplete tasks (noCount) and the tasks overdue (overDue)
    yesCount = 0
    noCount = 0
    overDue = 0

    #storing the current date in a variable called 'today'
    today = date.today()

    #a for loop tht reads in the 'countTaskList' list and executes the following
    for line in countTaskList:

        #if 'Yes' in 'line', 1 is added to the 'yesCount', else 1 is added in 'noCount'
        if "Yes" in line:
            yesCount += 1

        else:
            noCount += 1

    #a for loop that reads in 'counterTaskList' and executes the following
    for value in countTaskList:

        #splitting the comma and space in 'value' in a variable 'dueDate'
        dueDate = value.split(", ")[4]

        #using indexing from 'dueDate' to give values in the following variables: 'month', 'year' and 'day'
        month = dueDate[5:7]
        year = dueDate[0:4]
        day = dueDate[8::]

        #casting the due date in the date format
        digitDueDate = date(int(year), int(month), int(day))

        #if 'digitDueDate' is less than 'today' and there's 'No' in 'value' then 1 is added to the counter 'overDue'
        if digitDueDate < today and "No" in value:
            overDue += 1

    #calculating the percentage of incomplete tasks in a variable called 'incompletePercentage'
    incompletePercentage = (noCount / lengthOfList) * 100

    #calculating the percentage of overdue tasks in a variable called 'overduePercentage'
    overduePercentage = (yesCount / lengthOfList) * 100

    #opening 'task_overview.txt' text file in a variable called 'taskOverview' and writing in it, the closing the 'taskOverview' text file
    taskOverview = open("task_overview.txt", "w")
    taskOverview.write(f"The Total Number of Tasks: {lengthOfList}\n The Total Number of Completed Tasks: {yesCount}\n The Total Number of Uncompleted Tasks: {noCount}\n The Total Number of Uncompleted and Overdue Tasks: {overDue}\n The Percentage of Tasks Uncomplete: {incompletePercentage:.2f}%\n The Percentage of Tasks Overdue: {overduePercentage:.2f}%")
    taskOverview.close()

    #opening the 'user_overview.txt' text file in a variable called 'userOverview'
    userOverview = open("user_overview.txt", "w")
    outLine = ""

    #opening 'user.txt' text file in a variable called 'userFile2' then reading and splitting lines in a variable called 'userList'
    userFile2 = open("user.txt", "r")
    userList = userFile2.read().splitlines()

    #finding the length of 'userList' in a variable called 'lengthUserList' and closing the 'userFile2' text file
    lengthUserList = len(userList)
    userFile2.close()

    #opening 'tasks.txt' text file in a variable called 'taskFile9' then reading and splitting lines in a variable called 'taskFile9'
    taskFile9 = open("task.txt", "r")
    taskList = taskFile9.read().splitlines()

    #finding the length of 'taskList' in a variable called 'lengthTaskList' and closing the 'taskFile9' text file
    lengthTaskList = len(taskList)
    taskFile9.close()

    #counters for the number of tasks (taskCount), for the number of complete tasks (taskCompleteCount), for the number of incomplete tasks (taskIncompleteCount) and for the number of overdue tasks (taskOverdueCount)
    taskCount = 0
    taskCompleteCount = 0
    taskIncompleteCount = 0
    taskOverdueCount = 0 

    #declaring empty lists which will store the usernames (usernames) and the user tasks (taskUsers)
    usernames = []
    taskUsers = []

    #a for loop in 'userList' in which it appends into 'usernames' and also write in 'userOverview' text file
    for line in userList:
        usernames.append(line.split(", ")[0])
        userOverview.write(f"The total number of users: {lengthUserList} and total number of tasks {lengthTaskList}\n")

    #a for loop that reads in the list 'usernames' and executes the following
    for username in usernames:

        #a for loop with the range from zero to the length of 'taskList' list
        for task in range(0, len(taskList)):

            #splitting the comma and space in 'task' in a variable 'dueDate1'
            dueDate1 = taskList[task].split(", ")[4]

            #using indexing from 'dueDate' to give values in the following variables: 'month1', 'year1' and 'day1'
            month1 = dueDate1[5:7]
            year1 = dueDate1[0:4]
            day1 = dueDate1[8::]

            #casting the due date in the date format
            digitDueDate1 = date(int(year1), int(month1), int(day1))

            #storing the current date in a variable called 'today1'
            today1 = date.today()

            #if 'username' is in 'taskList[task]' then 1 is added in 'taskCount'
            if f"{username}" in f"{taskList[task]}":
                taskCount += 1

            #if 'username' is in 'taskList[task]' and 'Yes' in 'taskList[task]' then 1 is added to 'taskCompleteCount'
            if f"{username}" in f"{taskList[task]}" and "Yes" in  f"{taskList[task]}":
                taskCompleteCount += 1

            #if 'username' is in 'taskList[task]' and 'No' in 'taskList[task]' then 1 is added to 'taskIncompleteCount'
            if f"{username}" in f"{taskList[task]}" and "No" in  f"{taskList[task]}":
                taskIncompleteCount += 1

            #if 'username' is in 'taskList[task]' and 'No' in 'taskList[task]' and 'digitDueDate' is less than 'today1' then 1 is added to 'taskOverdueCount'
            if f"{username}" in f"{taskList[task]}" and "No" in  f"{taskList[task]}" and digitDueDate1 < today1:
                taskOverdueCount += 1

        #appending 'username' in 'taskUsers'
        taskUsers.append(username)

        #appending 'taskCount' in 'taskUsers', then calculating the tasks percentage in a variable called 'taskUserPercentage'
        taskUsers.append(taskCount)
        taskUserPercentage = round((taskCount / lengthTaskList) * 100, 2)

        #appending 'taskCompleteCount' in 'taskUsers', then calculating the tasks completion percentage in a variable called 'taskCompletePercentage'
        taskUsers.append(taskCompleteCount)
        taskCompletePercentage = round((taskCompleteCount / lengthTaskList) * 100, 2)

        #appending 'taskIncompleteCount' in 'taskUsers', then calculating the tasks incompletion percentage in a variable called 'taskIncompletePercentage'
        taskUsers.append(taskIncompleteCount)
        taskIncompletePercentage = round((taskIncompleteCount / lengthTaskList) * 100, 2)

        #appending 'taskOverdueCount' in 'taskUsers', then calculating the tasks percentage in a variable called 'taskOverduePercentage'
        taskUsers.append(taskOverdueCount)
        taskOverduePercentage = round((taskOverdueCount / lengthTaskList) * 100, 2)

        #declaring a variable called 'outLine' with a string
        outLine = username + " " + "has" + " " + "tasks," + " " + str(taskUserPercentage) + "%" + " " + "of tasks," + " " + str(taskCompletePercentage) + "%" + " " + "tasks completed" + ", " + str(taskIncompletePercentage) + "%" + " " + "incomplete tasks" + ", " + str(taskOverduePercentage) + "%" + " " + "tasks overdue." + "\n" 

        #writing 'outLine' in the 'userOverview' text file
        userOverview.write(outLine)

        #resetting the counters for proper calculations
        taskCount = 0
        taskCompleteCount = 0
        taskIncompleteCount = 0
        taskOverdueCount = 0

    #closing the 'userOverview' text file
    userOverview.close()               

#opening the 'user.txt' in a variable called 'userFile3'
userFile3 = open("user.txt", "r")

#displaying welcome message to the user
print("***** WELCOME TO TASK MANAGER *****")

#space or new empty line
print()

#displaying a line
print("_" * 134)

#space or new empty line
print()

#displaying a login message to the user
print("Login Details: ")

#space or new empty line
print()

#boolean for the login as True
login = True

#asks user for input
userName = input("Please enter your username: ")
password = input("Please enter your password: ")

#opening 'user.txt' text file in a variable called 'userFile'
userFile = open("user.txt", "r+")

#a fool loop that helps execute the login process
for singleUser in userFile:

    #splitting the coma in 'singleUser' in a variable called 'loginUser'
    loginUser = singleUser.split(", ")

    #replacing the '\n' with nothing in 'loginUser[1]' in a variable called 'userPassword'
    userPassword = loginUser[1].replace("\n", "")

    #if 'userName' is equal to 'loginUser[0]' and the password is equal to 'userPassword' then login is False therefore user logs in and the loop terminates
    if userName == loginUser[0] and password == userPassword:
        login = False
        break

#while login is True, user is unsuccessful in logging in
while login:

    #space or new empty line
    print()

    #displaying message to user
    print("Wrong information. Please try again.")

    #space or new empty line
    print()

    #asks user for input
    userName = input("Please enter your username: ")
    password = input("Please enter your password: ")

    #opening 'user.txt' text file in a variable called 'userFile'
    userFile = open("user.txt", "r+")

    #a fool loop that helps execute the login process
    for singleUser in userFile:

        #splitting the coma in 'singleUser' in a variable called 'loginUser'
        loginUser = singleUser.split(", ")

        #replacing the '\n' with nothing in 'loginUser[1]' in a variable called 'userPassword'
        userPassword = loginUser[1].replace("\n", "")

    #if 'userName' is equal to 'loginUser[0]' and the password is equal to 'userPassword' then login is False therefore user logs in and the loop terminates
        if userName == loginUser[0] and password == userPassword:
            login = False
            break

#closing the 'userFile' text file
userFile.close()

#space or new empty line
print()

#diplaying a double line
print("=" * 134)

#space or new empty line
print()

while userName != "admin":

    #displaying the admin menu to the user
    userMenu = input("Please select one of the following options: \n r - register user \n a - add task \n va - view all tasks \n vm - view my tasks \n e - exit \n: ")

    #space or new empty line
    print()

    #if the user enters 'r' (to register a user), then it displays as follows:
    if userMenu.lower() == "r":

        #space or new empty line
        print()

        #dsiplaying a line of stars
        print("*" * 134)

        #space or new empty line
        print()

        #calling on the 'reg_user' function
        reg_user()
    

    #if the users enters 'r' (add task), required the following inputs from user:
    if userMenu.lower() == "a":

        #space or new empty line
        print()

        #dsiplaying a line of kappies
        print("^" * 134)

        #space or new empty line
        print()

        #calling on 'add_task' function
        add_task()


    #if the user enters 'va', the following executes
    if userMenu.lower() == "va":

        #space or new empty line
        print()

        #dsiplaying a line of dashes
        print("- " * 72)

        #space or new empty line
        print()

        #calling on 'view_all' function
        view_all()


    #if the user enters 'vm' (view my tasks), the following executes:
    if userMenu.lower() == "vm":

        #space or new empty line
        print()

        #displaying a line of colons
        print(": " * 72)

        #space or new empty line
        print()

        #calling on the 'view_mine' function
        view_mine()


    #if statement if the user wishes to exit the program
    if userMenu.lower() == "e":

        #space or new empty line
        print()

        #dsiplaying a line of full stops
        print(". " * 72)

        #space or new empty line
        print()

        #displaying a message to the user
        print("You have exited the program, please log in to access it again. Thank you!")

        #exits the program
        exit()

        break

#space or new empty line
print()

#dsiplaying a line of stars
print("*" * 134)

#space or new empty line
print()
 
#a while loop, while 'userName' is equal to 'admin', the following executes
while userName == "admin":

    #displaying 'adminMenu' to the user
    adminMenu = input("Please select one of the following options: \n r - register user \n a - add task \n va - view all tasks \n vm - view my tasks \n gr - generate reports \n ds - display statistics \n e - exit \n : ")

    #if the user enters 'r' (to register a user), then it displays as follows:
    if adminMenu.lower() == "r":

        #space or new empty line
        print()

        #dsiplaying a line of stars
        print("*" * 134)

        #space or new empty line
        print()

        #calling upon 'reg_user' function
        reg_user()

    #if the users enters 'r' (add task), required the following inputs from user:
    if adminMenu.lower() == "a":

        #space or new empty line
        print()

        #displaying a line of kappies
        print("^" * 134)

        #space or new empty line
        print()

        #calling on 'add_task' function
        add_task()

    #if the user enters 'va', the following executes
    if adminMenu.lower() == "va":

        #space or new empty line
        print()

        #dsiplaying a line of dashes
        print("- " * 72)

        #space or new empty line
        print()

        #calling on 'view_all' function
        view_all()

    #if the user enters 'vm' (view my tasks), the following executes:
    if adminMenu.lower() == "vm":

        #space or new empty line
        print()

        #displaying a line of colons
        print(": " * 72)

        #space or new empty line
        print()

        #calling upon the 'view_mine' function 
        view_mine()

    if adminMenu.lower() == "gr":

        #space or new empty line
        print()

        #displaying a line of colons
        print(": " * 72)

        #space or new empty line
        print()

        #calling on 'reports' function
        reports()

        print("Reports are displayed in the ''task_overview.txt' text file and 'user_overview.txt' text file. Please open the mentioned text files to view the reports.")


    #if user enters 'ds' the following executes:
    if adminMenu.lower() == "ds":

        #space or new empty line
        print()

        #displaying a line of stars
        print("*" * 134)

        #space or new empty line
        print()

        #asks for user's input
        generateSatistics = input("To view the statistics, please enter 'gr' in order to generate the statistics: ")

        #if the user enters 'gr', then 'reports' function executes
        if generateSatistics.lower() == "gr":
            reports()

        #displaying message to the user
        print("The reports have been generated. \n")

        #calling on the 'statistics' function 
        statistics()

    #if statement if the user wishes to exit the program
    if adminMenu.lower() == "e":

        #space or new empty line
        print()

        #dsiplaying a line of full stops
        print(". " * 72)

        #space or new empty line
        print()

        #displaying a message to the user
        print("You have exited the program, please log in to access it again. Thank you!")

        #exits the program
        exit()

        break 

#closing 'userFile3' text file
userFile3.close()