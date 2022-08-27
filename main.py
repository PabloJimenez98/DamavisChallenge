import os
import numpy


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class Snake:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def initialize(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node

    def add_beginning(self, value):
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.head.prev = self.tail

    def delete_from_end(self):
        if self.head is not None:
            if self.head != self.tail:
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.head = self.tail = None

    def check_move(self, new):
        in_list = False
        if self.head is not None:
            temp_node = self.head
            while temp_node:
                if new == temp_node.value:
                    in_list = True
                    break
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next
        return in_list

    def check_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def move(self, direction):
        match direction:
            case 'u':
                return 1
            case 'd':
                return 2
            case 'l':
                return 3
            case 'r':
                return 4


def number_of_available_different_paths(board_n, board_m, snake, depth):
    return 2


def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    snake = Snake()

    f = open(os.path.join(__location__, 'input.txt'))
    lines = f.readlines()

    # Load board
    board_n = int(lines[0][0])
    board_m = int(lines[0][2])

    # Load Snake
    snake_pos = lines[1][:-1].split(';')

    for point in snake_pos:
        if snake.check_empty():
            snake.initialize(point)
        else:
            snake.add_beginning(point)

    depth = lines[2]

    result = number_of_available_different_paths(board_n, board_m, snake, depth)


main()
