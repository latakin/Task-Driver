from models import Ticket
import sys
def main():
    tasklist = []
    
    option  = None
    while True:
        displayInstructions()
        while True:
            option = getResponse()
            if option in [1,2,3,4,5]:
                break
            else:
                print("Incorrect Input")

        if option == 1:
            displaytask(tasklist)
            
        if option == 2:
            creator = input("who is creating this request? ").lower()
            request = input("what do you want to report? ").lower()
            priority = input("how important is it-high/low? ").lower()
            task = Ticket(creator,request,priority)
            tasklist.append(task)
            print(" ")
            print("Your ticket has been successfully created")
            
        if option == 3:
            for task in tasklist:
                print(f"{task.creator} - {task.request} - {task.priority} - {task.status}")
        
        if option == 4:
            print("Here are the available work orders: \n")
            displaytask(tasklist)
            if len(tasklist) == 0:
                break
            num = int(input("choose number to close ?"))
            if num in range(len(tasklist)):
                report = input("what did you do?")
            if tasklist[num + 1].status == "Open":
                tasklist[num + 1].status = "Closed"
                print(report)
                print("Request closed")
            else:
                print("work order is already closed")

        if option == 5:
            displaytask(tasklist)
            num = int(input("choose number to delete?"))
            tasklist.pop(num - 1)
        if option == 6:
            sys.exit()
        

def displayInstructions():
    print(" ")
    print("Welcome to Task Driver\n")
    print("1. check task list")
    print("2. create work order")
    print("3. check all request status")
    print("4. Close a request")
    print("5. delete a request")
    print("6.exit\n")
    print(" ")

def displaytask(tasklist):
    if len(tasklist) > 0:
        for i,task in enumerate(tasklist, start=1):
            print(f"{i} {task}")

    else:
        print("No work order at the moment\n")
        print(" ")
        
def getResponse():
    try:
        option = int(input("choose ur request from 1 to 5: "))
        return option
    except ValueError:
        print("Incorrect Input")


if __name__ == "__main__":
    main()