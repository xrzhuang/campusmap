__author__ = 'MaxZhuang'
from collections import deque

queue = deque()


def breadth_first_search(start, goal):
   queue.append(start)
   back_dict = {}
   path = []
   back_pointer = goal
   back_dict[start] = None
   while len(queue) > 0:
       location = queue.popleft()
       for adjacent in range(len(location.adjacency_list)):
           if location.adjacency_list[adjacent] not in back_dict:
               new_location = location.adjacency_list[adjacent]
               back_dict[new_location] = location
               queue.append(new_location)
               if new_location == goal:
                   while back_dict[back_pointer] != None:
                       path.append(back_pointer)
                       back_pointer = back_dict[back_pointer]
            return path





