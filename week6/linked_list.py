class Node:
    
    def __init__(self, value):
        self.value = value
        self.next_element = None
        
    #Cycles through the linked list and prints out each value
    def display(self):
        while self != None:
            print(self.value)
            self = self.next_element
        
#Creates a list of programming languages
lang1 = Node('Python')
lang2 = Node('Java')
lang3 = Node('JavaScript')
lang4 = Node('C++')

#Links them together
lang1.next_element = lang2
lang2.next_element = lang3
lang3.next_element = lang4

#By displaying lang1, this creates a chain which prints all of the nodes
lang1.display()