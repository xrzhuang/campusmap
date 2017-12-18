__author__ = 'MaxZhuang'
# import Vertex class to create objects
from vertex import Vertex

# create function, pass in parameter for graph text
def load_graph(graph):

    in_file = open(graph, "r")  # open graph, read
    location_dictionary = {}  # create dictionary

    # read through lines
    for line in in_file:
        line = line.strip()
        information = line.split(";")
        adjacents = information[1].split(",")
        coordinates = information[2].split(",")
        vertex = Vertex(information[0], adjacents, coordinates[0], coordinates[1])  # create objects using parts of each line
        location_dictionary[vertex.name] = vertex  # create it in dictionary with key
    in_file.close()  # close

    # open and go through the lines to create a list of objects, adjacency, for every vertex
    in_file = open(graph, "r")
    for line in in_file:
        # create a list for every object
        adjacency_list = []
        line = line.strip()
        information = line.split(";")
        vertex = location_dictionary[information[0]]

        # add each object searched to into a list, attach list to object, overwrite original adjacency list of strings
        for i in range(len(vertex.adjacency_list)):
            adjacency_list.append(location_dictionary[vertex.adjacency_list[i].strip()])
        vertex.adjacency_list = adjacency_list

    # return the dictionary
    return location_dictionary











