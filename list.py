from exceptions import *


class LinkedList:
    head = None
    length = 0

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node


    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

        return element


    def out(self, arg=None):
        try:
            if arg is not None:
                raise UnexpectedArgument()
            elif not self.head:
                raise EmptyList()
            node = self.head
                
            while node.next_node:
                print(node.element)
                node = node.next_node
            print(node.element)
        except (EmptyList, UnexpectedArgument) as error:
            print(f'При выводе: {error.message}')


    def insert(self, element, index):
        try:
            if index < 0:
                raise IndexIsNegative()
            i = 0
            node = self.head
            prev_node = self.head

            if index == 0:
                new_node = self.Node(element, next_node=self.head)
                self.head = new_node
            else:    
                while i < index:
                    prev_node = node
                    if node is None:
                        raise IndexOutOfRange(index)
                    node = node.next_node
                    i += 1
                prev_node.next_node = self.Node(element, next_node=node)  

            return element 
        except (IndexOutOfRange, IndexIsNegative) as error:
            print(f'При вставке: {error.message}')


    def get(self, index=None):
        try:
            if index == None:
                raise MissingIndex()
            elif index < 0:
                raise IndexIsNegative()
            i = 0
            node = self.head
            while i < index:
                node = node.next_node
                i += 1
                if node is None:
                    raise IndexOutOfRange(index)
            print(node.element)    
            return node.element
        except (MissingIndex, IndexOutOfRange, IndexIsNegative) as error:
            print(f'При получении: {error.message}')


    def delete(self, index=None):
        try:
            if index == None:
                raise MissingIndex()
            if index < 0:
                raise IndexIsNegative()
            elif index == 0:
                self.head = self.head.next_node
                
            node = self.head
            i = 0
            prev_node = node

            while i < index:
                prev_node = node
                node = node.next_node
                i += 1
            if not node:
                raise IndexOutOfRange(index)
            prev_node.next_node = node.next_node
            element = node.element   

            return element
        except (MissingIndex, IndexOutOfRange, IndexIsNegative) as error:
            print(f'При удалении: {error.message}')
                

    def get_length(self):
        if not self.head:
            return 0
        i = 1
        node = self.head

        while node.next_node:
            i += 1
            node = node.next_node

        print(f'Длина списка: {i}')
        return i
       
    
def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.insert(22, 6)
    linked_list.get(-5)
    linked_list.delete()
    linked_list.out()
if __name__ == '__main__':
    main()    