from models import Ticket
import sys
from datetime import datetime
from storage import savefile, getfile
import csv

def main():
    tasklist = []
    getfile("work_order.csv", tasklist)
    option  = None
    while True:
        displayInstructions()
        while True:
            option = getResponse()
            if option in [1,2,3,4,5,6]:
                break
            else:
                print("Incorrect Input")

        if option == 1:
            displaytask(tasklist)
        if option == 2:
            creator, request, priority = getInput()
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task = Ticket(creator,request,priority)
            tasklist.append({"creator": task.creator, "request": task.request, "priority": task.priority, "date": date, "status": task.status})
            savefile(tasklist, "work_order.csv")
            print(" ")
            print("Your ticket has been successfully created")
            
        if option == 3:
            checkstatus(tasklist)
        
        if option == 4:
            if len(tasklist) > 0:
                print("Here are the available work orders: \n")
                displaytask(tasklist)  
                close_request(tasklist)
            else:
                print("\nNo work order at the moment")
                continue

        if option == 5:
            displaytask(tasklist)
            delete_request(tasklist)
            
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

def getInput():
    creator = input("who is creating this request? ").lower()
    request = input("what do you want to report? ").lower()
    priority = input("how important is it-high/low? ").lower()
    return creator, request, priority

def displaytask(tasklist):
    print("\nHERE ARE THE CURRENT TASK IN TASK DRIVER")
    if len(tasklist) > 0:
        for i,task in enumerate(tasklist, start=1):
            print(f"{i} {task["creator"]} posted {task["request"]} with {task["priority"]} priority on {task["date"]}, and the status is {task["status"]}")

    else:
        print("No work order at the moment\n")
        print(" ")
        
def getResponse():
    try:
        option = int(input("choose ur request from 1 to 6: "))
        return option
    except ValueError:
        print("Incorrect Input")

def checkstatus(tasklist):
    for task in tasklist:
        print(f"{task["request"]} is {task["status"]}")

def close_request(tasklist):
    num = int(input("choose number to close ?"))
    if 1 <= num <= len(tasklist):
        if tasklist[num - 1]["status"] == "Closed":
            print("work order is already closed")
            
        else:
            report = input("what did you do?")
            tasklist[num - 1]["status"] = "Closed"
            savefile(tasklist,"work_order.csv")
            print(report)
            print("Request closed")


def delete_request(tasklist):
    if len(tasklist) > 0 :
        num = int(input("choose number to delete?"))
        print(num)
        if num > 0 and num <= len(tasklist):
            tasklist.pop(num - 1)
            savefile(tasklist, "work_order.csv")
            print("\n Request Deleted")
        else:
            print("Incorrect Input")


if __name__ == "__main__":
    main()