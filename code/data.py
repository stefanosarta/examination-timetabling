import networkx as nx  # Import networkx


def init():
    """
    Create dictionary named exam_students and a Graph structure
    using netowrkx package. Theese two can be used accross all the files
    that why we used, globally.

    Just need to call init and theese will be created as empty variables
    waiting for inputs
    """
    global exam_students
    global conflict_graph
    exam_students = {}
    conflict_graph = nx.Graph()

    global optimize_exams
    optimize_exams = {}
