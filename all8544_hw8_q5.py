class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None
            self.left_num = 0
            self.right_num = 0

        def num_children(self):
            count = 0
            if self.left:
                count += 1
            if self.right:
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
            self.left_num = None
            self.right_num = None

    def __init__(self):
        self.root = None
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def __getitem__(self, key):
        node = self.find_node(key)
        if node is None:
            raise KeyError(str(key) + " not found")
        return node.item.value

    def find_node(self, key):
        cursor = self.root
        while cursor:
            if cursor.item.key == key:
                return cursor
            elif cursor.item.key > key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        return None

    def __setitem__(self, key, value):
        node = self.find_node(key)
        if node is not None:
            node.item.value = value
        else:
            self.insert(key, value)

    def insert(self, key, value):
        new_item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)
        if self.is_empty():
            self.root = new_node
            self.n = 1
        else:
            parent = None
            cursor = self.root
            while cursor:
                parent = cursor
                if key < cursor.item.key:
                    cursor.left_num += 1
                    cursor = cursor.left
                else:
                    cursor.right_num += 1
                    cursor = cursor.right
            if key < parent.item.key:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.n += 1

    def __delitem__(self, key):
        node = self.find_node(key)
        if node is None:
            raise KeyError(str(key) + " not found")
        self.delete_node(node)

    def delete_node(self, node_to_delete):
        item = node_to_delete.item
        num_children = node_to_delete.num_children()

        if node_to_delete is self.root:
            if num_children == 0:
                self.root = None
                node_to_delete.disconnect()
                self.n -= 1
            elif num_children == 1:
                if self.root.left:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.n -= 1
            else:
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete_node(max_of_left)

        else:
            if num_children == 0:
                parent = node_to_delete.parent
                if node_to_delete is parent.left:
                    parent.left = None
                    parent.left_num = 0
                else:
                    parent.right = None
                    parent.right_num = 0
                node_to_delete.disconnect()
                self.n -= 1
            elif num_children == 1:
                parent = node_to_delete.parent
                if node_to_delete.left:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                if node_to_delete is parent.left:
                    parent.left = child
                    parent.left_num -= 1
                else:
                    parent.right = child
                    parent.right_num -= 1
                child.parent = parent

                node_to_delete.disconnect()
                self.n -= 1
            else:
                max_in_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_in_left.item
                self.delete_node(max_in_left)

        return item

    def subtree_max(self, subtree_root):
        cursor = subtree_root
        while cursor.right:
            cursor = cursor.right
        return cursor

    def inorder(self):
        def subtree_inorder(root):
            if root is None:
                return
            yield from subtree_inorder(root.left)
            yield root
            yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key

    def get_ith_smallest(self, i):
        if self.is_empty():
            raise Exception("Tree is empty")
        elif not 1 <= i <= self.n:
            raise IndexError()

        curr = self.root
        while curr:
            left_size = curr.left_num
            if i == left_size + 1:
                return curr.item.key
            elif i <= left_size:
                curr = curr.left
            else:
                i -= left_size + 1
                curr = curr.right

        raise IndexError()
