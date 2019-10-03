class Stationery:
    
    def __init__(self, name, size, color, quantity, action):
        self.name = name
        self.size = size
        self.color = color
        self.quantity = quantity
        self.action = action
        
    def work(self):
        print("The {} {} is {}".format(self.color, self.name, self.action))
        