import os
import copy
import time


# Basic node in linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


# Circular doubly  linked list
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

    # Initialize with a single element
    # ==> Time complexity : O(1)
    # ==> Space complexity : O(1)
    def initialize(self, value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node

    # Add a single element as the head of the snake
    # ==> Time complexity : O(1)
    # ==> Space complexity : O(1)
    def add_beginning(self, value):
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.head.prev = self.tail

    # Add a single element at the tail of the snake
    # ==> Time complexity : O(1)
    # ==> Space complexity : O(1)
    def add_at_the_end(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.head.prev = self.tail
        self.tail.next = self.head

    # Delete the last element at the tail of the snake
    # ==> Time complexity : O(1)
    # ==> Space complexity : O(1)
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

    # Check if the following movement stays within the limits and if the snake does not collide with itself.
    # ==> Time complexity : O(N)
    # ==> Space complexity : O(1)
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
            if board_n <= new[0] or new[0] < 0:
                return True
            if board_m <= new[1] or new[1] < 0:
                return True
            temp_node = self.head
            while temp_node:
                if new[0] == temp_node.value[0] and new[1] == temp_node.value[1]:
                    in_list = True
                    break
                if temp_node == self.tail.prev:
                    break
                temp_node = temp_node.next
        return in_list

    # Check if the snake has no elements
    # ==> Time complexity : O(1)
    # ==> Space complexity : O(1)
    def check_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Move the snake in the indicated direction. To do this, remove the element at the tail of the list
    #   and add a new one in the head to simulate the snake's movement.
    # ==> Time complexity : delete_from_end (O(1)) + add_beginning (O(1)) = O(1)
    # ==> Space complexity : delete_from_end (O(1)) + add_beginning (O(1)) = O(1)
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


# Recursive function that calculates all possible snake movements in a limited number of turns.
# It uses a tree structure in which each level is a turn and each branch is the possible movements.
# ==> Time complexity : function_cost (C(2n)) * recursive_calls (C(m)) = C(2nm) = O(nm)
# ==> Space complexity : function_cost (C(n)) * recursive_calls (C(m)) = C(nm) = O(nm)
def rec_solv(board_n, board_m, snake, depth, act, sol):
    for move in ['u', 'd', 'l', 'r']:
        if not snake.check_move(move, board_n, board_m):
            sv = copy.deepcopy(snake)
            snake.move(move)
            if act == depth - 1:
                sol[0] = sol[0] + 1
            else:
                rec_solv(board_n, board_m, snake, depth, act + 1, sol)
            snake = sv


def number_of_available_different_paths(board_n, board_m, snake, depth):
    sol = [0]
    rec_solv(board_n, board_m, copy.deepcopy(snake), depth, 0, sol)
    return sol[0]


# Main function
# Test examples times: Test 1 : 0.0010008811950683594 seconds
#                      Test 2 : 0.0010004043579101562 seconds
#                      Test 3 : 0.006005525588989258 seconds
def main():
    # Env variables
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    start_time = time.time()

    # Create the snake
    snake = Snake()

    # Read input file
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

    # Load depth
    depth = int(lines[2])

    # Get and print the results
    result = number_of_available_different_paths(board_n, board_m, snake, depth)
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))


main()
