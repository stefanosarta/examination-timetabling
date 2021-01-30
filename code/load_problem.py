import data as es
from collections import defaultdict


def load_problem(filename):
    es.init()
    collisions = 0

    """                    READ STU FILE & CONVERT
    ---------------------------------------------------------------------------
    1. Parse the file reading each line and save output to a list of lists
    named exams. Each list[i] of the list contains the rows of the file

    2. Create a dictionary using the list of lists with enumerate and start
    the counting from number 1 using start=1. Name of the newly created
    dictionary is buffer. Basically exams[0] becomes the 1st value of the
    dictionary having key 1, exams[1] becomes the 2nd value of the dictionary
    having key 2 etc. Key 1,2,3 means the student number and the value of the
    list has the lessons.

    3. Using defaultdict and two itterations we create a new dictionary. This
    dictionary contains swapped keys and now they key becomes each lesson
    and the list, becomes the students that have picked it.
    ---------------------------------------------------------------------------
    """

    exams = [[int(s) for s in line.split()]
             for line in open(filename).readlines()]  # Read each line

    buffer = dict(enumerate(exams, start=1))

    students = len(buffer)  # length of buffer.Meaning total number of students

    d = defaultdict(list)
    for k, v in buffer.items():  # iterate over key/value tuples.
        for sub in v:  # get each subject in the set/value
            d[sub].append(k)  # add the students to a list and
            # and make each subject a key

    es.exam_students = dict(d)

    num_of_exams = len(es.exam_students)  # Total number of exams
    count2 = sum(map(len, es.exam_students.values()))  # Count the total

    """                         CREATE NODES AND EDGES
    ---------------------------------------------------------------------------
    1. Itterate through buffer and for each key add a node to the Graph
    initiated. Basically each buffer key becomes a single node.

    2. Similarly, itterate with a double for the same dictionary, count
    collisions and create connections, meaning the edges. Output is a
    dictionary that contains lessons and students that has selected it.

    3. By using commands print(conflict_graph.nodes()) &
    print(conflict_graph.edges()) we can see the nodes and edges.
    ---------------------------------------------------------------------------
    """
    for i in es.exam_students:
        es.conflict_graph.add_node(i)

    for i in es.exam_students:
        for j in es.exam_students:
            if i == j:
                collisions += 1
            else:
                if set(es.exam_students[i]) & set(es.exam_students[j]):
                    collisions += 1
                    es.conflict_graph.add_edge(i, j)

    # print(es.conflict_graph.nodes())
    # print(es.conflict_graph.edges())
    print("*"*15)
    print(f'Density is {collisions/num_of_exams**2:.2f}')
    print("*"*15)
    print(f'There are {num_of_exams} exams')
    print("*"*15)
    print(f'There are {students} students')
    print("*"*15)
    print(f'There are {count2} entries')
    print("")
