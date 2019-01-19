import requests
from DataStructures.Queue import Queue
from DataStructures.Stack import Stack

class Palindrome:
    def __init__(self):
        self.magicitems =[]
        self.palindrones = []

    def getMagicItems(self):
        try:
            session = requests.Session()
            response = session.get('http://labouseur.com/courses/algorithms/magicitems.txt')
            if response.status_code != 200:
                raise ValueError(f'ERROR: issue retriving data, status code for request: {response.status_code}')

            for item in response.text.splitlines():
                self.magicitems.append(item)

        except:
            raise ValueError('Request to retrieve magic items failed!')

    
    def stackChars(self, item):
        s = Stack()
        for char in list(item):
            s.push(char)
        return s
        
    def queueChars(self, item):
        q = Queue()
        for char in list(item):
            q.enqueue(char)
        return q

    def checkForPalindrone(self):
        
        for item in self.magicitems:
            match = False
            stacked_item = self.stackChars(item)
            queued_item = self.queueChars(item)
            
            for i in range(len(item)):
                s_char = stacked_item.pop()
                q_char = queued_item.dequeue()
                if s_char == q_char:
                    match = True
                else:
                    match = False

            if match:
                self.palindrones.append(item)





if __name__ == "__main__":
   palindrome = Palindrome()
   palindrome.getMagicItems()
   palindrome.checkForPalindrone()
   print(palindrome.palindrones)