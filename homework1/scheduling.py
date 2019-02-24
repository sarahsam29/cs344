"""
The goal of this program is to return a schedule such that no professors and rooms and time slots conflict
Inspired by the Zebra problem

@author: ss63
@date: February 23, 2019
@purpose: for CS 344

"""
from csp import min_conflicts, \
    CSP, \
    parse_neighbors

def Schedule():
    courses = ['cs108','cs112','cs212','cs262','cs344']
    professors = ['Schuurman','Adams', 'Plantinga','VanderLinden']
    class_time = ['9MWF','1030MWF','1130MWF', '1230TH']
    rooms = ['SB328', 'NH253']
    #instead of following the zebra and making these constraints, I defined the pre-conditions in a dictionary.
    pre_condition = {'cs108':'Schuurman', 'cs112':'Adams', 'cs212':'Plantinga', 'cs262':'Vanderlinden','cs344':'Vanderlinden'}
    variables = courses

    #
    domain = {}
    for c in courses:
        domain[c] = []
        for p in professors:
            for t in class_time:
                for r in rooms:
                    domain[c].append([p, t, r])

    #assign each class to be a neighbour of all the other classes
    neighbours = parse_neighbors("""cs108: cs112;
                cs108: cs212; cs108: cs262; cs108: cs344;
                cs112: cs212; cs112: cs262; cs112: cs344;
                cs212: cs262; cs212: cs344; cs262: cs344""", variables)

    #3 things need to be true to get a non-conflicting schedule
    def constraints(course1, val1, course2, val2):
        #return false if time and professor of two courses are the same
        if val1[1] == val2[1] and val1[0] == val2[0]:
            return False

        #return false if time and room of two courses are the same
        if val1[1] == val2[1] and val1[2] == val2[2]:
            return False

        # check that the pre_conditions are still being met.
        #This is currently causing this program to return "none" (aka no schedules)... have to look into it.
        if (pre_condition[course1] != val1[0]) or (pre_condition[course2] != val2[0]):
            return False
        return True
    return CSP(variables, domain, neighbours, constraints)

#intialize the problem and print the solution
p = Schedule()
solution = min_conflicts(p)
print(solution)
