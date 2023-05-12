# Binary search trees are great for searching.

# Best case scenario
# lookup: O(log n)
# insert: O(log n)
# delete: O(log n)
# This occurs when a linked list is balanced. To balanced binary search tree can be implemented using e.g. AVL or Red Black algorithms

# Worst case scenario
# lookup: O(n)
# insert: O(n)
# delete: O(n)
# This occurs when the tree becomes unbalanced and essentially turns into a linked list.
import json


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a node into the binary search tree.
        """
        # insert the first node into the tree
        if self.root == None:
            self.root = Node(value)

        else:
            parent_node = None
            next_node = self.root

            # keep looping until next_node (a child_node of parent_node) is None
            while next_node:
                # parent_node will always be one level less than next_node
                parent_node = next_node

                # if less set next_node equal to left node of parent_node
                if value < next_node.value:
                    next_node = None if not parent_node.left else parent_node.left

                # if greater next_node equal to right node of parent_node
                else:
                    next_node = None if not parent_node.left else parent_node.right

            # set left child node of parent_node if value is less than parent value
            if value < parent_node.value:
                parent_node.left = Node(value)

            # set right child node of parent_node if value is greater than parent value
            else:
                parent_node.right = Node(value)

    def lookup(self, value):
        pass

    def remove(self, value):
        pass


def traverse(node):
    tree = {"value": node.value}
    tree["left"] = None if not node.left else traverse(node.left)
    tree["right"] = None if not node.right else traverse(node.right)
    return tree


def main():
    #        9
    #    4       20
    # 1    6  15    170

    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    json_tree = json.dumps(traverse(tree.root))
    print(json_tree)


if __name__ == "__main__":
    main()
