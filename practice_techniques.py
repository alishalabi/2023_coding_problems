##############

## Practice compare two times as string

def compare_time(time1, time2):
    hours1, minutes1 = time1.split(":")
    hours2, minutes2 = time2.split(":")
    converted1 = int(hours1) * 60 + int(minutes1)
    converted2 = int(hours2) * 60 + int(minutes2)

    if converted1 > converted2:
        return 1
    elif converted1 < converted2:
        return -1
    else:
        return 0

# print(compare_time("18:00", "19:30"))

##############

## Practice finding if substring present

def check_in(string, substring):
    if substring in string:
        print(True)
    else:
        print(False)

# check_in("hello world", "hellod")


def substring_dict(string, substring):
    all_substrings = set()
    for i in range(len(string)):
        for j in range(i+1,(len(string) + 1)):
            new_substring = string[i:j]
            all_substrings.add(new_substring)
    if substring in all_substrings:
        print(True)
    else:
        print(False)

# substring_dict("helloworld", "world")
# substring_dict("helloworld", "happy")

##############

## Practice using Tries

class Prefix_node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Prefix:
    def __init__(self):
        self.head = Prefix_node()
    def add_word(self, word):
        curr = self.head
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Prefix_node()
            curr = curr.children[letter]
        curr.isWord = True

    def starts_with(self, prefix):
        curr = self.head
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True

# prefix_tree = Prefix()
# prefix_tree.add_word("beetle")
# print(prefix_tree.head.children["b"].children)
# print(prefix_tree.starts_with("bee"))
# print(prefix_tree.starts_with("ape"))



##############

## Practice using Linked Lists
class LL_node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_node(self, value):
        node = LL_node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def print_LL(self):
        curr = self.head
        while curr != None:
            print(curr.value)
            curr = curr.next
    def reverse_LL(self):
        previous = None
        curr = self.head
        while curr != None:
            temporary_next = curr.next
            curr.next = previous
            previous = curr
            curr = temporary_next
        self.head = previous
        self.print_LL()

#
# LL = LinkedList()
# LL.add_node("a")
# LL.add_node("b")
# LL.add_node("c")
# LL.add_node("d")
# LL.reverse_LL()



##############

# Practice DFS (matrix)

sample_dfs_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["1", "0", "1", "1", "1"]
] # Should have 4 island

"""
Pseudo code:

def _dfs(grid, col, row):
    set first item to "seen", in this case turn to "0"
    get all directions we can traverse
    iterate all directions
    ensure each direction is on grid
    if cell is "1", run dfs on that cell (recursion)



def find_islands(grid):
    instantiate islands
    check grid at each row column
    if is "1", increment islands, dfs on that cell
    after checking all cells once, return islands

"""


def _dfs(grid, row, column):
    grid[row][column] = "0"
    directions = [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]
    for r, c in directions:
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[row]) and grid[r][c] == "1":
            _dfs(grid, r, c)


def find_islands(grid):
    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "1":
                _dfs(grid, r, c)
                islands += 1

    print(islands)

# find_islands(sample_dfs_grid)

##############

# Practice missing item in array

array1 = ["a", "b", "c", "d"]
array2 = ["b", "a", "d"]

def find_missing(array1, array2):
    long_arr = None
    short_arr = None
    reference = set()
    if len(array1) < len(array2):
        long_arr = array1
        short_arr = array2
    else:
        long_arr = array2
        short_arr = array1
    for item in long_arr:
        # Check if in reference if not unique
        reference.add(item)

    for item in short_arr:
        print(item)
        if item not in reference:
            return item

# print(find_missing(array1, array2))



##############


##############
