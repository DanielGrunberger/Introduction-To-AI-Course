
import CSProblem
import copy


def solve(n):
    CSProblem.present(backtrack(CSProblem.create(n)))


def backtrack(p):
    var = next_var(p, MRV=True)  # MRV-Most constrained variable or Minimum Remaining Values
    if var == None:
        return p
    dom = sorted_domain(p, var, LCV=True)  # LCV-least constraining value
    for i in dom:
        bu = copy.deepcopy(p)
        CSProblem.assign_val(bu, var, i)
        propagate_constraints(bu, var)  #
        bu = backtrack(bu)
        if CSProblem.is_solved(bu):
            return bu
    return p


def sorted_domain(p, var, LCV=True):
    if LCV == False:
        return CSProblem.domain(p, var)

    # your code here
    dom = CSProblem.domain(p, var)  # list of the var domains
    help = dict.fromkeys(dom, 0)  # dictionary for the domains, the value for each domain will be the number of restrictions on the rest of the domains
    for i in dom:  # for each domain
        for j in CSProblem.get_list_of_free_vars(p):  # for all the other free vars
            if (var != j):  # if it is not the same col(var)
                for k in CSProblem.domain(p, j):  # for each domain in j
                    if not (CSProblem.is_consistent(p, var, j, i, k)):# if var=i and j=k is not consistent with all constraints
                        help[i] += 1#add one to the value of restrictions of the domain i

    sorted_d = dict(sorted(help.items(), key=lambda item: item[1]))#sort the dictionary according to the value, to find the domain with the minimum number of restrictions.
    return sorted_d.keys()#return the keys of the dictionary after the sorting(keys=domains).


def num_of_del_vals(l):
    # l=[problem, the variable, the val. assigned to the var.]
    # returns the num. of vals. erased from vars domains after assigning x to v
    count = 0
    for inf_v in CSProblem.list_of_influenced_vars(l[0], l[1]):
        for i in CSProblem.domain(l[0], inf_v):
            if not CSProblem.is_consistent(l[0], l[1], inf_v, l[2], i):
                count += 1
    return count


def next_var(p, MRV=True):
    # p is the problem
    # MRV - Minimum Remained Values
    # Returns next var. to assign
    # If MRV=True uses MRV heuristics
    # If MRV=False returns first non-assigned var.
    if MRV == False:
        v = CSProblem.get_list_of_free_vars(p)
        if v == []:
            return None
        else:
            return v[0]

    # your code here
    v = CSProblem.get_list_of_free_vars(p)  # The list of the free vars.
    if v == []:#if the list of free vats is empty.
        return None
    len_dom = dict.fromkeys(v, 0)  # dictionary of the length of the domain for the free vars.(keys=vars)
    for i in v:  # for each var calculate the length of the domain.
        len_dom[i] += (CSProblem.domain_size(p, i))#add to the dictionary the length of the domain for eacg var(i).
    return(min(len_dom, key=len_dom.get))#return the key with the minimum length of domain=the var with the maximum constraints.



def propagate_constraints(p, v):
    for i in CSProblem.list_of_influenced_vars(p, v):
        for x in CSProblem.domain(p, i):
            if not CSProblem.is_consistent(p, i, v, x, CSProblem.get_val(p, v)):
                CSProblem.erase_from_domain(p, i, x)


solve(100)
