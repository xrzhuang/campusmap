__author__ = 'MaxZhuang'
# import functions from cs1lib, load_graph, and b_f_s
from cs1lib import *
from load_graph import load_graph
from b_f_s import breadth_first_search

# constants
X_MAP = 0
Y_MAP = 0
NO_COLOR = 0
COLOR = 1
SLEEP_TIME = .2
MAP_WIDTH = 1012
MAP_LENGTH = 811


# main plotting function
def map_plot():
    # create a vertex dictionary from load_graph function
    vertex_dict = load_graph("dartmouth_graph.txt")

    # initialize start_search variable
    start_search = None

    # loop when window isn't closed
    while not window_closed():

        # load map
        img = load_image("dartmouth_map.png")
        draw_image(img, X_MAP, Y_MAP)

        # initialize goal_search
        goal_search = None

        # for loop to draw vertices and edges on map
        for key in vertex_dict:
            vertex_dict[key].draw_vertex(NO_COLOR, COLOR, COLOR)
            vertex_dict[key].edges(NO_COLOR, COLOR, COLOR)

        # if statement when mouse is clocked
        if mouse_down():
            down_x = mouse_x()
            down_y = mouse_y()

            # for loop to find vertex clicked on, set start_search
            for key in vertex_dict:
                if vertex_dict[key].mouse_on(down_x, down_y) == True:
                    start_search = vertex_dict[key]

        # find the hovering vertex, set goal_search
        elif start_search != None:
            for key in vertex_dict:
                if vertex_dict[key].mouse_on(mouse_x(), mouse_y()) == True:
                    if start_search != vertex_dict[key]:
                        goal_search = vertex_dict[key]

        # if start_search, goal_search is set, draw the vertex
        if start_search != None:
            start_search.draw_vertex(COLOR, NO_COLOR, COLOR)
        if goal_search != None:
            goal_search.draw_vertex(COLOR, NO_COLOR, COLOR)

        # if a path is asked to be found, start and goal are set, use bfs, draw and color path
        if start_search != None and goal_search!= None:
            path = breadth_first_search(start_search, goal_search)
            for i in range(len(path) - 1):  # - 1 necessary so you don't ask to draw out of index within loop below
                path[i].connect_vertices(path[i+1], COLOR, NO_COLOR, COLOR)
                path[i].draw_vertex(COLOR, NO_COLOR, COLOR)

        # graphics
        request_redraw()
        sleep(SLEEP_TIME)

# start
start_graphics(map_plot, "Map of Dartmouth", MAP_WIDTH, MAP_LENGTH)