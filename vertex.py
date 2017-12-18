__author__ = 'MaxZhuang'
# import cs1lib
from cs1lib import *

# constants
VERTEX_SIZE = 6
EDGE_SIZE = 3

# create class for vertices
class Vertex:

    # constructor
    def __init__(self, name, adjacency_list, x, y):  # pass parameters
        # create instance variables
        self.name = name
        self.adjacency_list = adjacency_list
        self.x = int(x)
        self.y = int(y)

    # return string
    def __str__(self):
        final_string = self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: "
        # need to create string of names from list of objects (adjacency_list)
        adjacency_list_string = ""  # start string with nothing
        for i in range(len(self.adjacency_list)-1):  # no comma for last adjacent
            adjacency_list_string = adjacency_list_string + str(self.adjacency_list[i].name)+ ", "
        adjacency_list_string = adjacency_list_string + str(self.adjacency_list[len(self.adjacency_list)-1].name)
        return final_string + adjacency_list_string  # add the last two string pieces and return

    # draw vertex method
    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_SIZE)

    # connect vertices method, draws line between two vertices
    def connect_vertices(self, VERTEX2, r, g, b):
        set_stroke_width(EDGE_SIZE)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, VERTEX2.x, VERTEX2.y)

    # method that draws all lines between adjacent vertices and vertex
    def edges(self, r, g, b):
        for i in range(len(self.adjacency_list)):
            self.connect_vertices(self.adjacency_list[i], r, g, b)

    # method that returns True if mouse is within smallest square around vertex, False if otherwise
    def mouse_on(self, x, y):
        if self.x - VERTEX_SIZE < x <= self.x + VERTEX_SIZE and self.y - VERTEX_SIZE < y <= self.y + VERTEX_SIZE:
            return True
        else:
            return False










