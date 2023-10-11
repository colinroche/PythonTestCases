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
    
    # Function to find the number of Nodes in a Linked List
    def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        if temp != None:
            # Loop while end of Linked List is not reached
            while (temp):
                count += 1
                temp = temp.next
            return count
        else:
            print("Linked list is empty")
            exit()
    
    # Function to get the middle element in the Linked List
    def getMid(self):
        # call getCount() to get number of Nodes in Linked List
        count = self.getCount()
        temp = self.head

        # traverse until we get half the number of Nodes present in Linked List
        mid = count // 2
        while mid != 0:
            # temp stores the current node
            temp = temp.next
            mid -= 1
        # temp stores the middle node
        print(temp.val)

# Driver code
list_1 = LinkedList()
list_1.addNode("a")
list_1.addNode("b")
list_1.addNode("c")
list_1.addNode("d")
list_1.addNode("e")

list_1.getMid()


