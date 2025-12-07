'''
In this file I worked on creating a basic usecase of Class. 
I started off by naming it helloWorld
Inside I used the constructor Innit and added inputString insde the paranthesis
Then I named the inputString variable inputData.
I made another method/function named printInputData to print the value
I created a new object for the class and the object name is obj1 and i passed the hello World string
I created a nother new object and named in obj2 and passed helloworld obj2
Then for both i did obj1/2.printInputData 

                    Quick Summary:
Code	                             Meaning
__init__	                        Constructor (runs when object is created)
self	                            The object being created
self.inputData = inputString	    Save data inside the object


'''

class helloWorld:
    def __init__(self, inputString):
        self.inputData = inputString
    def printInputData(self):
        print(self.inputData)



obj1 =helloWorld("helloWorld")
obj1.printInputData()
obj2 = helloWorld("helloWorld")
obj2.printInputData()
print(obj1 == obj2)


