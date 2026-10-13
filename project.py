from models import Ticket
import sys
def main():
    tasklist = []
    
    option  = None
    while True:
        displayInstructions()
        while True:
            option = int(input("choose ur request from 1 to 5: "))
            if option in [1,2,3,4,5]:
                break
            else:
                print("Incorrect Input")

        if option == 1:
            for task in tasklist:
                print(task)
        if option == 2:
            creator = input("who is creating this request").lower()
            request = input("what do you want to report? ").lower()
            priority = input("how important is it-high/low?").lower()
            task = Ticket(creator,request,priority)
            tasklist.append(task)
            print("Your ticket has been successfully created")
            
        if option == 3:
            for task in tasklist:
                print(f"{task.creator}-{task.request}-{task.priority}")
        if option == 4:
            for i,task in enumerate(tasklist, start=1):
                print(f"{i} {task}")
            num = int(input("choose number to delete?"))
            tasklist.pop(num)
        if option == 5:
            sys.exit()
        

def displayInstructions():
    print("Welcome to Task Driver\n")
    print("1. check task list")
    print("2. create work order")
    print("3. check all request status")
    print("4. delete a request")
    print("5.exit")


if __name__ == "__main__":
    main()