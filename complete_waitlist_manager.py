# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    # Step 1: Node Class 
    def __init__(self, name):
        self.name = name
        self.next = None #pointing to the next node


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    #Contains the head(Node)
    def __init__(self):
        self.head = None #setting the head of the linked list, intialized with the value of None
    
    #add_end()
    def add_end(self, name):
        new_node = Node(name) 
        if not self.head: 
            self.head = new_node #indicates a new node
        else: 
            current = self.head
            while current.next: 
                current = current.next #makes the current node the next node
            current.next = new_node #this makes what was next before, now the new node, attaches to the END
        return f"{name} added to the end of the waitlist."
    
    #add_front()
    def add_front(self, name):
        new_node = Node(name) # new node
        new_node.next = self.head #adds to the front, meaning the next should go IN FRONT of what is currently the head
        self.head = new_node #sets the new node as the head
        #no rearranging order required to add to the front
    #remove() method
    def remove(self, name): 
        if not self.head: #if the list were empty or the name is not located
            return f"{name} not found."
        
        if self.head.name == name: #if the name IS found, and moves the head if necessary
          self.head = self.head.next #note: one = assigns a new value
          return f"Removed {name} from the waitlist."
        
        previous = self.head #setting previous/current heads when removing a name
        current = self.head.next

        while current: 
            if current.name == name:
                previous.next = current.next #brings the previous name into the current when removing a name
                return f"Removed {name} from the waitlist." 
            
            previous = current #resetting the locations in the linked list when removing a name
            current = current.next

        return f"{name} not found." 

#prints the whole list, if there is no one waiting, then the list prints that it is empty
    def print_list(self):
        current = self.head
        if not current:
            print("This waitlist is empty!")
        else: 
            while current: 
                print(current.name)
                current = current.next

# LEFT OFF AT STEP 8 ---------------------
def waitlist_generator():
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            print(waitlist.add_end(name))
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            print(waitlist.remove(name)) #returns a message in the method, so it should return one here
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
#Response: Design Memo
#How does the list work?
# My list works by first creating a node class to hold a name. Then, in the linked list class, we are beginning to add methods as to how we can update the list.
# First, we want to establish the head (which should be initialized with a value of None). We then have three methods that are used to update the list. First is add_end, this will take a new node and add it to the END of the list.
# Specifically, it indicates a new node is being created, establishes what the current and current.next nodes are in the list, and then replaces what was the next one, with the current new node. This means it attaches to the END.
# Next is the add_front method. No looping or position changes are made here, as we are simply adding a new name in front of the entire list (at the top). We establish a new node, take the new node that would have been next, and establish it
# as the new HEAD. This will place it at the front of the entire list, no position changes necessary. The last method (remove()) is more complicated, as it requires different instances
# and takes into account the position changes of the list when a name is removed. First, it establishes if the list is empty or if the name was not located - it will return a message if this is the case. 
# Then, it checks if the name IS found, and moves the head if necessary. It assigns the head as the next node once the value required is removed, and returns the message to indicate this was done for the user. 
# The same method also sets previous/curent heads when removing a name - this could come in handy as the name being removed could come from any spot in the list. 
# The 'while' loop will allow these changes to occur, and reassign positions in the list when a name is removed. Positions are re-established, and the name is removed!
# The LinkedList() now prints the list from the head (current) on. If the list is empty, it will print a message to say so. If it's not empty, it prints the list.
# The waitlist generator then pulls everything in from the LinkedList() class, and uses it to implement the users inputs. 

#The HEAD: 
# The head plays the role of the starting point, or intializer. With a value of 'None' the head can act as a place to start the linked list.
# Using the head, we can initialize a list and begin to signify how it should move from one node to the next. You may be able to start with a head that has a value, but the head must exist
# to begin the process of utilizing a linked list for a waitlist scenario. It also comes into play when using certain methods like we had in this assignment. You may have to reassign the head location, or it may need to 
# change depending on the method being utilized. It is a crucial player in linked lists, as it determines the order throughout the whole list in my opinion/understanding. 

#Real-World Scenario: 
# An engineer may need a list like this if they were managing lists of operations, priorities, or creating list managers just like this for a number of scenarios.
# If they need to prioritize operations, create a queue of tasks to do/complete when done, or a check-list, they could use this method to help them possibly. They could call different methods to 
# update the lists, remove tasks, prioritize tasks, de-prioritize tasks, etc. It could benefit efficiency, and organization in the workplace for an individual, or even a team. 
