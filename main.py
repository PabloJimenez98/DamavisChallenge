import os
import copy


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

    def add_at_the_end(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.head.prev = self.tail
        self.tail.next = self.head

    def delete_from_end(self):
        if self.head is None:
            return
        elif self.head.next is self.tail.next:
            self.head = self.tail = None
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    def check_move(self, direction, board_n, board_m):
        match direction:
            case 'l':
                new = [self.head.value[0] - 1, self.head.value[1]]
            case 'r':
                new = [self.head.value[0] + 1, self.head.value[1]]
            case 'u':
                new = [self.head.value[0], self.head.value[1] - 1]
            case 'd':
                new = [self.head.value[0], self.head.value[1] + 1]

        in_list = False
        if self.head is not None:
            temp_node = self.head
            while temp_node:
                if board_n <= new[0] or new[0] < 0:
                    in_list = True
                    break
                if board_m <= new[1] or new[1] < 0:
                    in_list = True
                    break
                if new[0] == temp_node.value[0] and new[1] == temp_node.value[1]:
                    in_list = True
                    break
                if temp_node == self.tail.prev:
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
            case 'l':
                self.delete_from_end()
                self.add_beginning(
                    [self.head.value[0] - 1, self.head.value[1]])
            case 'r':
                self.delete_from_end()
                self.add_beginning(
                    [self.head.value[0] + 1, self.head.value[1]])
            case 'u':
                self.delete_from_end()
                self.add_beginning(
                    [self.head.value[0], self.head.value[1] - 1])
            case 'd':
                self.delete_from_end()
                self.add_beginning(
                    [self.head.value[0], self.head.value[1] + 1])


def rec_solv(board_n, board_m, snake, depth, act, sol):
    for move in ['u', 'd', 'l', 'r']:
        if not snake.check_move(move, board_n, board_m):
            sv = copy.deepcopy(snake)
            snake.move(move)
            if act == depth - 1:
                sol[0] = sol[0] + 1
            else:
                rec_solv(board_n, board_m, copy.deepcopy(snake), depth, act + 1, sol)
            snake = sv


def number_of_available_different_paths(board_n, board_m, snake, depth):
    sol = [0]
    rec_solv(board_n, board_m, copy.deepcopy(snake), depth, 0, sol)
    return sol[0]


def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    snake = Snake()

    f = open(os.path.join(__location__, 'input.txt'))
    lines = f.readlines()

    # Load board
    board_n = int(lines[0].split(',')[0])
    board_m = int(lines[0].split(',')[1])

    # Load Snake
    snake_pos = lines[1][:-1].split(';')

    for point in snake_pos:
        pnt = point.split(',')
        pnt = [int(numeric_string) for numeric_string in pnt]
        if snake.check_empty():
            snake.initialize(pnt)
        else:
            snake.add_at_the_end(pnt)

    depth = int(lines[2])

    result = number_of_available_different_paths(board_n, board_m, snake, depth)
    print(result)


main()
