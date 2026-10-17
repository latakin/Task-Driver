class Ticket:
    def __init__(self,creator,request,priority, status="Open"):
        self._creator = creator
        self._request = request
        self._priority = priority
        self._status = status


    
    @property
    def creator(self):
        return self._creator
    
    @property
    def request(self):
        return self._request
    
    @property
    def request(self):
        return self._request
    
    @property
    def status(self):
        return self._status
    
    @property
    def priority(self):
        return self._priority

    def close(self):
        self.status = 'closed'

    def __str__(self):
        return f"{self._creator} has just posted {self._request} with {self._priority} priority "

        