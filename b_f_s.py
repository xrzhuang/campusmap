__author__ = 'MaxZhuang'
# import deque
from collections import deque

# define function, parameters passed are start and goal objects
def breadth_first_search(start, goal):

    # set queue to deque
    queue = deque()

    # append the first point
    queue.append(start)

    # create back dictionary and path
    back_dict = {}
    path = []

    # set back pointer, first key in back_dict
    back_pointer = goal
    back_dict[start] = None

    # while loop create back_dict
    while len(queue) > 0:
        location = queue.popleft()
        for adjacent in range(len(location.adjacency_list)):
            if location.adjacency_list[adjacent] not in back_dict:
                new_location = location.adjacency_list[adjacent]
                back_dict[new_location] = location
                queue.append(new_location)

                # when new_location meets goal, back_dict has all required keys (and extra), create direct path
            if new_location == goal:
                while back_pointer != None:
                    path.append(back_pointer)
                    back_pointer = back_dict[back_pointer]

    # return path
    return path