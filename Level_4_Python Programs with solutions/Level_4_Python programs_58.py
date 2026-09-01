class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add an entry at the end
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
    def insert_before(self, given_id, new_id, new_name):
        new_node = Node(new_id, new_name)

        if self.head is None:
            print("List is empty")
            return

        if self.head.id == given_id:
            new_node.next = self.head
            self.head = new_node
            print("Entry inserted successfully")
            return

        temp = self.head

        while temp.next:
            if temp.next.id == given_id:
                new_node.next = temp.next
                temp.next = new_node
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
                new_node.next = temp.next
                temp.next = new_node
                print("Entry inserted successfully")
                return

            temp = temp.next

        print("ID not found")

    # Delete an entry
    def delete(self, id):
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if self.head.id == id:
            self.head = self.head.next
            print("Entry deleted successfully")
            return

        temp = self.head

        while temp.next:
            if temp.next.id == id:
                temp.next = temp.next.next
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

        print("\nLinked List:")
        while temp:
            print("ID:", temp.id, "Name:", temp.name)
            temp = temp.next


# Create linked list
lst = LinkedList()

# Add 5 sample entries
lst.add(101, "Arun")
lst.add(102, "Bala")
lst.add(103, "Kumar")
lst.add(104, "Ravi")
lst.add(105, "Suresh")


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
            lst.insert_before(given_id, new_id, new_name)

        elif position == "A":
            lst.insert_after(given_id, new_id, new_name)

        else:
            print("Invalid option")

    elif choice == 2:
        id = int(input("Enter ID to delete: "))
        lst.delete(id)

    elif choice == 3:
        lst.display()

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice")