import data as es
import networkx as nx
import random


def solve_problem(filename):
    """                     CREATE GREEDY COLOR ALGORITHM
    ---------------------------------------------------------------------------
    1. Run coloring.greedy_color algorithm to the dictionary created by adding
    nodes and edges above. The return of this algorithm is once again a
    dictionary.
    2. This dictionary has the periods assigned for each class. The key
    contains the lesson and the value of each key contains the period
    that was assigned.
    ---------------------------------------------------------------------------
    """
    if len(es.conflict_graph.edges()) == 0:  # Checking if a problem is loaded
        print("No problem to solve!")   # If it is loaded then len must be > 0
        return()

    exams2 = nx.coloring.greedy_color(
        es.conflict_graph, strategy=nx.coloring.strategy_largest_first)

    es.optimize_exams = dict(exams2)
    # es.optimize_exams2 = dict(exams2)
    es.best = dict(exams2)

    """                     EXPORT SOLUTIONS FILE
    ---------------------------------------------------------------------------
    1. We itterate through the period_exams dictionary and export to the file
    two columns. The first column contains the subject and the other one
    contains the period that was assigned into.
    ---------------------------------------------------------------------------
    """

    with open(filename[0:-4]+'.sol', 'w') as f:
        for k, v in exams2.items():
                f.write('{}\t{}\n'.format(k, v))

    """
    In the next itteration of the exams2 dictionary we switch dictionary
    keys and now the period becomes they key and the lessons assigned to it
    the values. It is being saved in the period_exams dictionary.
    """
    period_exams = {}
    for k, v in exams2.items():
        if v not in period_exams:
            period_exams[v] = [k]
        else:
            period_exams[v].append(k)
    cost(period_exams)

def cost(period_exams):
    """
    ---------------------------------------------------------------------------
    1. Using three for loops to parse two dictionaries, period_exams and
    exam_students.
    2. At each run except KeyError is working and it puts keys as long as
    incoming numbers are unique. If key already exists then it appends the
    specific number of aperiod on those keys that are included on buffer list
    of that specific itteration.
    3. Result is a dictionary with keys of each student and values each of
    their sessions that they should join.
    ---------------------------------------------------------------------------
    """

    student_periods = {}

    for aperiod in period_exams:
        for e in period_exams[aperiod]:
            for s in es.exam_students[e]:
                if s not in student_periods:
                    student_periods[s] = [aperiod]
                else:
                    student_periods[s].append(aperiod)

    numofstudents = len(student_periods)

    cost = 0
    d = 0;
    cost_value = [16, 8, 4, 2, 1]
    for s in student_periods:
        mycal = sorted(student_periods[s])
        for (i, eachexam) in enumerate(sorted(mycal)):
            for j in range(i+1, i+6):
                if j < len(mycal):
                    d = mycal[j] - mycal[i]
                    if d > 5:
                        cost += 0
                    else:
                        cost += cost_value[d-1]

    print("-"*15)
    print(f'Total cost of this problem is {cost/numofstudents:.4f}')
    print("-"*15)
    return(cost/numofstudents)
