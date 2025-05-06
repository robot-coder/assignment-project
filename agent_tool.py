# agent_tool.py

class SimpleTree:
    """
    A simple binary tree implementation that allows for insertion and traversal.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Insert a new value into the binary tree.
        """
        if value < self.value:
            if self.left is None:
                self.left = SimpleTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = SimpleTree(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        """
        Perform inorder traversal of the binary tree and return the values in a list.
        """
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements


def read_file(file_path):
    """
    Read content from a file and return it.
    """
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    """
    Write content to a file.
    """
    with open(file_path, 'w') as file:
        file.write(content)


# Demonstration of using the SimpleTree
if __name__ == '__main__':
    tree = SimpleTree(10)
    numbers = [5, 15, 3, 7, 12, 18]
    for number in numbers:
        tree.insert(number)
    print("Inorder Traversal of the Tree:", tree.inorder_traversal())
