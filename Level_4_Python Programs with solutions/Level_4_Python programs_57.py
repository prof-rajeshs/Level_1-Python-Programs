class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add sample entries
    def add(self, id, name):
        new_node = Node(id, name)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Insert before a given ID
    def insert_before(self, id, new_id, new_name):
        new_node = Node(new_id, new_name)

        if self.head is None:
            print("List is empty")
            return

        if self.head.id == id:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            if temp.next.id == id:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("ID not found")

    # Insert after a given ID
    def insert_after(self, id, new_id, new_name):
        temp = self.head

        while temp:
            if temp.id == id:
                new_node = Node(new_id, new_name)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("ID not found")

    # Display list
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        print("\nLinked List:")
        while temp:
            print("ID:", temp.id, "Name:", temp.name)
            temp = temp.next


# Create linked list
lst = LinkedList()

# Sample 5 entries
lst.add(101, "Arun")
lst.add(102, "Bala")
lst.add(103, "Kumar")
lst.add(104, "Ravi")
lst.add(105, "Suresh")


# Menu
while True:
    print("\n--- MENU ---")
    print("1. Insert Entry")
    print("2. Display List")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_id = int(input("Enter new ID: "))
        new_name = input("Enter name: ")

        position = input("Insert before or after? (B/A): ").upper()
        given_id = int(input("Enter the ID: "))

        if position == "B":
            lst.insert_before(given_id, new_id, new_name)
        elif position == "A":
            lst.insert_after(given_id, new_id, new_name)
        else:
            print("Invalid choice")

    elif choice == 2:
        lst.display()

    elif choice == 3:
        print("Program exited.")
        break

    else:
        print("Invalid choice")