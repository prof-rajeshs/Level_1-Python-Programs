class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Add entry at the end
    def add(self, id, name):
        new_node = Node(id, name)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # Insert before a given ID
    def insert_before(self, given_id, new_id, new_name):
        temp = self.head

        while temp:
            if temp.id == given_id:
                new_node = Node(new_id, new_name)

                new_node.next = temp
                new_node.prev = temp.prev

                if temp.prev:
                    temp.prev.next = new_node
                else:
                    self.head = new_node

                temp.prev = new_node

                print("Entry inserted successfully")
                return

            temp = temp.next

        print("ID not found")

    # Insert after a given ID
    def insert_after(self, given_id, new_id, new_name):
        temp = self.head

        while temp:
            if temp.id == given_id:
                new_node = Node(new_id, new_name)

                new_node.prev = temp
                new_node.next = temp.next

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node

                print("Entry inserted successfully")
                return

            temp = temp.next

        print("ID not found")

    # Delete an entry
    def delete(self, id):
        temp = self.head

        while temp:
            if temp.id == id:

                # If deleting the first node
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                # If deleting a node other than last
                if temp.next:
                    temp.next.prev = temp.prev

                print("Entry deleted successfully")
                return

            temp = temp.next

        print("ID not found")

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("\nDoubly Linked List:")
        while temp:
            print("ID:", temp.id, "Name:", temp.name)
            temp = temp.next


# Create doubly linked list
dll = DoublyLinkedList()

# Add 5 sample entries
dll.add(101, "Arun")
dll.add(102, "Bala")
dll.add(103, "Kumar")
dll.add(104, "Ravi")
dll.add(105, "Suresh")


# Menu
while True:
    print("\n----- MENU -----")
    print("1. Insert Entry")
    print("2. Delete Entry")
    print("3. Display List")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_id = int(input("Enter new ID: "))
        new_name = input("Enter name: ")

        given_id = int(input("Enter the ID before/after which to insert: "))
        position = input("Insert Before or After? (B/A): ").upper()

        if position == "B":
            dll.insert_before(given_id, new_id, new_name)

        elif position == "A":
            dll.insert_after(given_id, new_id, new_name)

        else:
            print("Invalid option")

    elif choice == 2:
        id = int(input("Enter ID to delete: "))
        dll.delete(id)

    elif choice == 3:
        dll.display()

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice")