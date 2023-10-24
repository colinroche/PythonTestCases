import random as r

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

    # Function for adding random alphabetic characters in range to Linked List
    def addAlpha(self, length):
        characters = "abcdefghijklmnopqrstuvwxyz"
        i = 0

        while i < length:
            x = r.randrange(0,26)
            self.addNode(characters[x])
            i += 1

    # A utility function to print a given linked list
    def printList(self):
        node = self.head
        values = []

        i = 0
        # set to 29 to stop endless loop
        while node and i < 29:
            # create list which contains the value present in each node
            values.append(node.val)
            node = node.next
            i+=1
        if values != None:
            print("\nElements present in Linked List: ", end="")
            for value in values:
                print(value, end=" -> ")
            print()
        else:
            print("Linked List not created or empty\n")


    # Function to find the number of Nodes in a Linked List
    def getCount(self):
        node = self.head  # Initialise node
        count = 0  # Initialise count

        if node != None:
            # Loop while end of Linked List is not reached
            while node:
                count += 1
                node = node.next
            print("The number of elements in Linked List are:", count)
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

        # check element at set position
        while count < pos:
            node = node.next
            count += 1
        
        # start loop at position
        join = node

        # add all element then revert back to looping position
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

            # if the first time seeing node, insert
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
        print("Loop has been removed from Linked List")
        
    # Function using bubble sort on Linked List
    def bubbleSort(self):
        # initialise variables
        node = self.head
        curr = None
        temp = None
        prev = None
        new_head = None

        if node != None:
            while node != None:
                # set the current node and the temporary node to the Linked list head
                curr = node
                temp = node
                prev = None

                while curr != None:
                    # if the value of the current node is greater then the previous node
                    if curr.next != None and curr.next.val > temp.val:
                        # set the new node values incrementally
                        temp = curr.next
                        prev = curr
                    
                    curr = curr.next

                # set previous node's next equal to the temp node's next
                if prev != None:
                    prev.next = temp.next

                # if the temp node equals the Linked List head, set that node equal to the next
                if temp == node:
                    node = node.next

                # set the temp node's next equal to the new head of Linked List
                temp.next = new_head
                # set the new head value equal to the temp node
                new_head = temp

            # make new head
            self.head = new_head
          
        else:
           print("Empty Linked list")

    def mergeList(self, otherList):
        node_1 = self.head
        node_2 = otherList.head
        merged = LinkedList()

        while node_1 != None:
            merged.addNode(node_1.val)
            node_1 = node_1.next

        while node_2 != None:
            merged.addNode(node_2.val)
            node_2 = node_2.next

        merged.bubbleSort()
        return merged
    
        

# Driver code
rangeLength = 5
i =0

pos = 3

list_1 = LinkedList()
list_1.addAlpha(rangeLength)

list_2 = LinkedList()
list_2.addAlpha(rangeLength)

#list_1.addLoop(pos)
#list_1.removeLoop()
#list_1.getCount()
#list_1.getMid()

list_1.bubbleSort()
list_1.printList()

list_2.bubbleSort()
list_2.printList()

mergedList = list_1.mergeList(list_2)
mergedList.printList()

