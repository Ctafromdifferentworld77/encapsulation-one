class myClass:
    #private variable
    __privateVar=12
    
    #private method
    
    def __privatemeth(self):
        print("I am inside the private method")
        
    def greetings(self):
        print("good morning")
            
#object
obj1=myClass()
obj1.greetings()
#obj1.__privateMeth()#
