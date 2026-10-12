class Ticket:
    def __init__(self,creator,request,priority):
        self.creator = creator
        self.request = request
        self.priority = priority
        self.status = "Open"

    
    
    def close(self):
       self.status = 'closed'

    def __str__(self):
        return f"{self.creator} has just posted {self.request} with {self.priority} priority "

        