import data as es
import random
from load_solution import load_solution
from solve_problem import cost
import numpy

"""
In this function we optimize the result that we got from the NetowrkX
package. We itterate through the solution and make some small changes at each
run. Theese chamges have to do with changing the potition by one or two. And
also giving some total random exam potition on a random lesson. Theese can be
combined on whatever level we want.

We can choose to make small changes each run or bigger ones.

Each possible solution is checked by load_problem function and if its correct
we check if its better or worse than the one we already have. If is better then
its being saved as the best. If its not then the last known best is loaded
again and we keep making changes on that one.

We take care of periods and exams limit of each problem. We do it manually

"""


def optimize_problem():
    first_solution = 195

    max1 = max(es.optimize_exams.values())
    min1 = min(es.optimize_exams.values())
    for k in range(0, 1000000):  # Run for long time before manually stop it
        numberList = [-1, 1, -2, 2, -3, 3]  # number of changing a potition.
        # it picks randomly
        numberList4 = [1, -1]
        numberList2 = [1, 2, 3, 4, 5, 6, 7, 8, ]
        numberList3 = [-1, -2, -3, -4, -5, -6, -7, -8]

        # Range here differs for each problem

        for i, v in es.optimize_exams.items():
            # The next 2 lines can be put outside loop separetely for different
            # kind of swaping values
            option10, option11, option12 = random.sample(range(0, 32), 3)
            option1, option2, option3, option4, option5 = random.sample(range(1, 543), 5)

            if v < max1-2 and v > min1+2:
                es.optimize_exams[i] = v+random.choice(numberList)
                # es.optimize_exams[option2] = v+random.choice(numberList)
                # es.optimize_exams[option3] = v+random.choice(numberList)
                es.optimize_exams[option1] = option10
                # es.optimize_exams[option4] = option11
                # es.optimize_exams[option5] = option12
                es.optimize_exams[option4] = v+random.choice(numberList4)

            if v > max1-2:  # making sure we dont go over max nodes
                es.optimize_exams[i] = v+random.choice(numberList3)
                # es.optimize_exams[option1] = option10
            if v < min1+2:  # making sure we dont go down of 0
                es.optimize_exams[i] = v+random.choice(numberList2)
                # es.optimize_exams[option4] = option11

            period_exams = {}
            for k, v in es.optimize_exams.items():
                if v not in period_exams:
                    period_exams[v] = [k]
                else:
                    period_exams[v].append(k)

            with open('car-f-92.sol2', 'w') as f:
                for k, v in es.optimize_exams.items():
                    f.write('{}\t{}\n'.format(k, v))

            b = load_solution('car-f-92.sol2')
            if b != 1:
                a = cost(period_exams)
                # print(a)
                if a < first_solution:
                    first_solution = a
                    # print("BETTER")
                    print("BETTER!")
                    print(first_solution)
                    # print("inputed")
                    # print(option1)
                    # print(option3+i)
                    es.best = es.optimize_exams
                    # keys =  list(es.best.keys())
                    # random.shuffle(keys)
                    # [(key, es.best[key]) for key in keys]
                    with open('car-f-92.sol', 'w') as f:
                        for key in period_exams:
                            for items in period_exams[key]:
                                f.write('{}\t{}\n'.format(items, key))
                    a1 = list(es.best.items())
                    numpy.random.shuffle(a1)
                    es.best = dict(a1)
                else:
                    es.optimize_exams = es.best
                    a1 = list(es.optimize_exams.items())
                    numpy.random.shuffle(a1)
                    es.optimize_exams = dict(a1)
                    # print("else")
                    # print("inputed")
                    # print(option1)
                    # print(option3+i)
            else:
                # print("1")
                es.optimize_exams = es.best
                a1 = list(es.optimize_exams.items())
                numpy.random.shuffle(a1)
                es.optimize_exams = dict(a1)
                # keys =  list(es.optimize_exams.keys())
                # random.shuffle(keys)
                # [(key, es.optimize_exams[key]) for key in keys]
    print("FINAL")
    print(first_solution)
