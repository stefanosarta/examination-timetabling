import data as es
from solve_problem import cost
from load_problem import load_problem
from solve_problem import solve_problem


def load_solution(filename):
    """                     LOAD SOLUTION
    ---------------------------------------------------------------------------
    1. Reads the filename and creates an empty dictionary.
    2. While reading file line by line it takes the 1st column to exam
    and the 2nd column to period.
    3. It checks if there are more than one exam of the same student in a
    specific period and if not it returns a simple message. It uses extend
    and a newly created list. By comparing length and the unique values of
    this list.
    4. The final dictioanry has the periods as keys and the lessons assigned
    to it as the values. We call cost that was created on solve_problem.py
    to return us the cost.
    ---------------------------------------------------------------------------
    """
    file = open(filename, 'r')
    period_exams = {}
    while (True):
        line = file.readline()
        if (line):
            exam = int(line.split('\t')[0])
            period = int(line.split('\t')[1])
            try:
                allperiodstudents = []
                for e in period_exams[period]:
                    allperiodstudents.extend(es.exam_students[e])
                    if len(allperiodstudents) != len(set(allperiodstudents)):
                        print("Invalid solution! period " + str(period) +
                              " has two exams of the same student.")
                        return()
                period_exams[period].append(exam)
            except KeyError:
                period_exams[period] = [exam]
        else:
            break
    cost(period_exams)


def mass_solve():
    """ Function that uses a simple for and solves all the problems
    Every time it runs init in order to get new fresh dictionary
    and graph. And ofcourse it need to load problem each time and
    then solve it."""
    files = ["car-f-92.stu",
             "car-s-91.stu",
             "ear-f-83.stu",
             "hec-s-92.stu",
             "kfu-s-93.stu",
             "lse-f-91.stu",
             "pur-s-93.stu",
             "rye-s-93.stu",
             "sta-f-83.stu",
             "tre-s-92.stu",
             "uta-s-92.stu",
             "ute-s-92.stu",
             "yor-f-83.stu"]

    for x in range(len(files)):
        es.init()
        load_problem(files[x])
        solve_problem(files[x])
