class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        print("Entry pushed successfully")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            data = self.top.data
            self.top = self.top.next
            print("Popped entry:", data)

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top

            print("\nStack (Top to Bottom):")
            while temp:
                print(temp.data)
                temp = temp.next


# Create stack
stack = Stack()


# Menu
while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the entry to push: ")
        stack.push(data)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice")