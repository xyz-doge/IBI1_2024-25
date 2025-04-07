#   Create a class for patients, representing the 'Patient Information Template'
class patients:
#   Create an 'initialization function' that is automatically called when creating a patient object    
    def __init__(self, name, age, date, history):
#   Save various patient information        
        self.name = name
        self.age = age
        self.date = date
        self.history = history
#   A method called show() is defined to display patient information
    def show(self):
        print(self.name, self.age, self.date, self.history)
#   Give an example        
p = patients("Li Muxuan", 19, "2025-04-01", "too smart")
p.show()