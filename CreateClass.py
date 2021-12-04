#Srikar Rani
#10.1 Create your own class
#I have created a Dog class that has a few variables and methods that could allow you to interact with the dog
class Dog:
    #These defined variables are the class variables that do not change per instance of the class
    age = 1
    number_of_legs = 4
    weight = 100
    count = 0
    alive = True
    #The init functions constructs the dog and assigns it the three variables
    def __init__(self,name,breed,color):
        self._name = name
        self._breed = breed
        self._color = color
        

    #This method gets the name of the dog 
    def get_name(self):
        return self._name
    #This method gets the breed of the dog
    def get_breed(self):
        return self._breed
    #This method gets the color of the dogs
    def get_color(self):
        return self._color
    #This method sets the name of the dog, giving you the ability to change it after 
    def set_name(self,name):
        self._name = name
    #This method allows you to set the breed after initializing
    def set_breed(self,breed):
        self._breed = breed
    #This method allows you to set a color after initializing
    def set_color(self,color):
        self._color = color
    #This method gives you the ability to feed your dog, increasing his weight by the integer number amount of food
    def feed_dog(self, amount):
        if Dog.age >= 13 :
            Dog.alive = False
        if (Dog.alive):
            Dog.age += 1
            Dog.weight += amount
            if Dog.weight <= 130:
                print(self._name + " is very happy and ready to run around!")
            elif Dog.weight > 130 and Dog.weight < 160:
                print(self._name + " is looking a little unhealthy. Maybe do not feed him as much.")
            else:
                print(self._name + " is looking too big, you should take him to the doctor")
        else:
            print("Your dog is dead")
    #This method allows you to walk the dog, reducing his weight
    def walk_dog(self):
        if Dog.age >= 13 :
            Dog.alive = False
        if (Dog.alive):
            Dog.age += 1
            Dog.weight -= 15
            if  Dog.weight > 80  and Dog.weight <= 130:
                print(self._name + " is doing amazing! He is very athletic!")
            elif Dog.weight > 130 and Dog.weight < 160:
                print(self._name + " is starting to get back in shape, continue to walk him!") 
            elif Dog.weight >= 160: 
                print(self._name + " should continue walking for his health, but this is a good start!")
            else:
                print("Maybe you should feed " + self._name + " more, he is getting too skinny. Also stop waling him for now.")
        else:
            print("Your dog is dead")

    #This method allows you to play fetch with the dog, yet he will get tired if you do too much fetching
    def playing_fetch(self):
        if Dog.age >= 13 :
            Dog.alive = False
        if (Dog.alive):
            Dog.age += 1
            Dog.count += 1
            if Dog.count < 3:
                print("Wow! " + self._name + " is having so much fun playing fetch!")
            else:
                print("Thats enough, " + self._name + " is tired.")
        else:
            print("Your dog is dead")

    #This method resets the count for playing fetch with the dog
    def sleep_time(self):
        if Dog.age >= 13 :
            Dog.alive = False
        if Dog.alive:
            Dog.age += 1
            Dog.count = 0
            print("Dog is well rested and ready to play fetch again")
        else:
            print("Your dog is dead")


def main():
    #First you initialize the object 
    dog1 = Dog("Bolt","Pitbull","Blue")
    #To run playing fetch you don't have to enter any arguments
    dog1.playing_fetch()
    #To feed the dog you have to enter how much weight you want him to gain
    dog1.feed_dog(10)
    dog1.feed_dog(15)
    dog1.feed_dog(5)
    dog1.feed_dog(10)
    #After this much feeding the dog will be overweight
    #Walking the dog also takes no arguments
    dog1.walk_dog()
    dog1.walk_dog()
    dog1.walk_dog()
    dog1.walk_dog()
    dog1.walk_dog()
    #The dog is back in shape after all this walking
    #Playing fetch and sleep time do not take in any arguments
    dog1.playing_fetch()
    dog1.playing_fetch()
    dog1.playing_fetch()
    #The dog is tired of playing fetch
    dog1.sleep_time()
    #The sleep rejuvinated the dog and he is ready to play again
    dog1.playing_fetch()
    #The dog successfully played again
    

if __name__ == "__main__":
    main()



