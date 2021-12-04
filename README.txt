
Class Documentation:

The Dog class has different variables that the object takes in as parameters and stores as variables. The object takes the name, breed, and color of the dog to store these arguments as instance variables. The Dog class also has multiple methods to get and set the instance variables and also a few more methods to interact with the dog object. 

The class variables in the Dog class are age, number of legs, weight, count, and alive:

The variable age is set to 1, and every time the dog has 1 interactions, the age goes up one
The variable number of legs is always set to 4
The variable weight is set to 100 default, but weight can go up 10 by feeding the dog, and can go down by walking the dog. The weight of the dog determines a lot of the interaction with the dog.
The variable count is set to 0 at default and goes up by one every time you play fetch with the dog. You can reset the count by having the dog sleep
The variable alive is to see whether your dog is still alive. If he is 13 or older he will die

The instance variables are name, breed, and color

The variable name is just the name of the dog.
The variable breed is the breed of the dog.
The variable color is the color of the dog. 

The get/set methods are get_name, get_breed, get_color, set_name, set_breed, and set_color:

The get_name method takes in only the self argument and returns the name variable of the object
The get_breed method takes in the self argument and returns the breed variable of the object
The get_color takes in the self argument and returns the color variable
The set_name takes in the self argument and a string name argument and does not return anything but changes the variable name 
The set_breed argument takes in the arguments self and breed and changes the variable breed to whatever is entered in the argument
The set_color method takes in self and a string color argument and changes the variable color to whatever is entered into the color argument

The other methods are to interact with the Dog object including feed_dog, walk_dog, playing_fetch, sleep_time:

The feed_dog method takes in the arguments self and amount. The amount argument is the amount of weight that the dog will gain if he is fed, and this amount should be an integer. The weight is added first, and then the appropriate statement is printed based off of the weight. 

The walk_dog method takes in the argument self. The walk_dog method reduces the weight of the Dog by 15. The appropriate print statement is then printed based on the dog's weight.

The playing_fetch method takes in the argument self. The method first increases the count variable by one. Then the method checks if the count variable is below 3. If the variable is below 3, then the dog plays fetch and prints a statement. If the variable is 3 or above, the statement that is printed is that the dog is too tired to play fetch.

The sleep_time method takes in the argument of self. The method clears the count variable to 0 and prints a statement that the dog is ready to go. 

Demo Program Documentation:
The Demo program essentially tests the 3 main interactive methods of the program. It is meant to display how the dog's state will change based on its weight, if it is well rested, or based on its age. The dog will be unhealthy if it is too fat or skinny, will not play fetch if it is too tired, and will be dead if it is too old.

Running the demo program is simple, as there are not many arguments to enter for most methods. For the feeding the dog method, you could enter whatever integer you would like for the dog to increase in weight. 


