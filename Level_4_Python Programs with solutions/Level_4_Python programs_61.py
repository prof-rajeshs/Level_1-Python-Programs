class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None

    # Add operation
    def add(self, data):
        new_node = Node(data)

        # If queue is empty
        if self.front is None:
            self.front = new_node
        else:
            temp = self.front

            # Go to the bottom/end of the list
            while temp.next:
                temp = temp.next

            temp.next = new_node

        print("Entry added successfully")

    # Remove operation
    def remove(self):
        if self.front is None:
            print("Queue is empty")
        else:
            data = self.front.data
            self.front = self.front.next
            print("Removed entry:", data)

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front

            print("\nQueue (Top to Bottom):")
            while temp:
                print(temp.data)
                temp = temp.next


# Create queue
queue = Queue()


# Menu
while True:
    print("\n----- QUEUE MENU -----")
    print("1. Add")
    print("2. Remove")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the entry to add: ")
        queue.add(data)

    elif choice == 2:
        queue.remove()

    elif choice == 3:
        queue.display()

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice")