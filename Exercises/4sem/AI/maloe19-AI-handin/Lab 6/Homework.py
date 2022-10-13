from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result != None:
                    return result
                assignment[var] = None
        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True

def create_south_america_csp():
    #costa_rica, panama, colombia, venezuela, guyana, suriname, guyana_fr, ecuador, peru, brasil, bolivia, paraguay, chile, argentine, uruguay 
    cr,          pan,    co,       v,         g,      s,        gf,        e,       per,  br,     bo,      par,      ch,    a,         u       = 'CR', 'PAN', 'CO', 'V', 'G', 'S', 'GF', 'E', 'PER', 'BR', 'BO', 'PAR', 'CH', 'A', 'U'    
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [cr, pan, co, v, g, s, gf, e, per, br, bo, par, ch, a, u]
    domains = {
        cr: values[:],
        pan: values[:],
        co: values[:],
        v: values[:],
        g: values[:],
        s: values[:],
        gf: values[:],
        e: values[:],
        per: values[:],
        br: values[:],
        bo: values[:],
        par: values[:],
        ch: values[:],
        a: values[:],
        u: values[:]
    }
    neighbours = {
        cr: [pan],
        pan: [cr, co],
        co: [pan, v, e, per, br],
        v: [co, g, br],
        g: [v, s, br],
        s: [g, gf, br],
        gf: [s, br],
        e: [co, per],
        per: [co, e, br, bo, ch],
        br: [co, v, g, s, gf, per, bo, par, a, u],
        bo: [per, br, par, ch, a],
        par: [br, bo, a],
        ch: [per, bo, a],
        a: [br, bo, par, ch, u],
        u: [br, a]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cr: constraint_function,
        pan: constraint_function,
        co: constraint_function,
        v: constraint_function,
        g: constraint_function,
        s: constraint_function,
        gf: constraint_function,
        e: constraint_function,
        per: constraint_function,
        br: constraint_function,
        bo: constraint_function,
        par: constraint_function,
        ch: constraint_function,
        a: constraint_function,
        u: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
