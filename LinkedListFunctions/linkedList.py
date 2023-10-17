class Node(object):

    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add Node to Linked List
    def addNode(self, val=None):
        # Allocating the Node with value
        node = Node(val)

        # Make next of new Node the head
        node.next = self.head

        # Move the head to point at the Node
        self.head = node

    # A utility function to print a given linked list
    def printList(self):
        node = self.head
        values = []

        i = 0
        # set to 29 to stop endless loop
        while node and i < 29:
            values.append(node.val)
            node = node.next
            i+=1
        if values != None:
            print("Elements present in Linked List: ", end="")
            for value in values:
                print(value, end=" ")
            print()
        else:
            print("Linked List not created or empty")


    # Function to find the number of Nodes in a Linked List
    def getCount(self):
        node = self.head  # Initialise node
        count = 0  # Initialise count

        if node != None:
            # Loop while end of Linked List is not reached
            while node:
                count += 1
                node = node.next
            return count
        else:
            print("Linked List is empty")
    
    # Function to get the middle element in the Linked List
    def getMid(self):
        # call getCount() to get number of Nodes in Linked List
        count = self.getCount()
        node = self.head

        # traverse until we get half the number of Nodes present in Linked List
        mid = count // 2
        while mid != 0:
            # node stores the current node
            node = node.next
            mid -= 1
        # node stores the middle node
        print("The middle element in the Linked List is:", node.val)

    # Function to add a loop at specified position in Linked List
    def addLoop(self, pos):
        node = self.head
        count = 1
    
        if node == None:
            print("No Elements present in Linked List")
            exit()

        while count < pos:
            node = node.next
            count += 1
        
        join = node

        while node.next != None:
            node = node.next

        node.next = join

        print("Loop added at position", pos, "in Linked List")

    # Function to detect whether a loop is present or not in Linked List
    def detectLoop(self):
        # method is used to convert iterable to 
        # sequence of iterable elements with distinct elements. 
        s = set()
        node = self.head
        count = 0
        while node:
            # if node present in hash map, seeing for second time, cycle present         
            if node in s:
                print("Loop present in Linked List")
                # return position of loop as well
                return True and count

            # If the first time seeing node, insert
            s.add(node)
            node = node.next
            count += 1
        print("Loop not present in Linked List")
        return False
    
    # Function to remove loop from Linked List
    def removeLoop(self):
        node = self.head
        s = list_1.detectLoop()

        if bool(s) == True:
            count = 1
            # set next node to None when loop starting point encountered
            while node and count < s:
                node = node.next
                count += 1
            node.next = None

# Driver code
list_1 = LinkedList()
'''list_1.addNode("e")
list_1.addNode("d")
list_1.addNode("c")
list_1.addNode("b")
list_1.addNode("a")'''


pos = 3

list_1.addLoop(pos)
list_1.removeLoop()
list_1.printList()
list_1.getCount()