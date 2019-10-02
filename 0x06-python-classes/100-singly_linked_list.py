#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        stri = ""
        temp = self.__head
        while (temp):
            stri = stri + str(temp.data)
            if (temp.next_node):
                stri = stri + "\n"
            temp = temp.next_node
        return stri

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = Node(value, None)
        else:
            aux1 = self.__head
            aux2 = aux1.next_node
            if (self.__head.data > value):
                self.__head = Node(value, self.__head)
            else:
                while (aux2):
                    if (aux2.data > value):
                        new = Node(value, None)
                        new.next_node = aux2
                        aux1.next_node = new
                        break
                    aux1 = aux1.next_node
                    aux2 = aux2.next_node
                new = Node(value, aux2)
                aux1.next_node = new
