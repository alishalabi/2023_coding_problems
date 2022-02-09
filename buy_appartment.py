# INCOMPLETE

"""
From https://www.youtube.com/watch?v=rw4s4M3hFfs

"""

blocks_arr = [
    {"gym": False,
    "school": True,
    "store" : False},

    {"gym": True,
    "school": False,
    "store" : False},

    {"gym": True,
    "school": True,
    "store" : False},

    {"gym": False,
    "school": True,
    "store" : False},

    {"gym": False,
    "school": True,
    "store" : True},
]

reqs_arr = ["gym", "school", "store"]

def best_block(blocks, reqs):
    output = None # Will look like (block index, distance to walk)
    for block in blocks:
        curr_index = blocks.index(block)
        left = curr_index
        right = curr_index
        notSeen = reqs
        current_best = 0
        while len(notSeen) - 1 > 0:
            print(notSeen)
            while left - 1 > 0:
                left = -1
                for item in notSeen:
                    if blocks[left][item] == True:
                        notSeen.remove(item)
                        distance = abs(curr_index - left)
                        if distance > current_best:
                            current_best = distance
            while right + 1 < (len(blocks) - 1):
                right += 1
                for item in notSeen:
                    if blocks[right][item] == True:
                        notSeen.remove(item)
                        distance = abs(curr_index - right)
                        if distance > current_best:
                            current_best = distance
        if output == None or output[1] > current_best:
            output = (curr_index, current_best)
    print(output)

best_block(blocks_arr, reqs_arr)
