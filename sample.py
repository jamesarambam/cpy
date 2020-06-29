__author__ = 'james'

import cpy as jc
import os
# import auxLib as ax
import sys

# -------------- Problem ----------------

"""
obj : Max
z  =  x1 + 2x2 + 3x3
Constraints:
-x1 + x2 + x3 <= 20    : c1
x1 -  3x2 + x3 <= 30   : c2
Bounds :
0 <= x1 <=40
0 <= x2 <= infinity
0 <= x3 <= infinity
"""

# -------------------------------

# o = ax.getOS()
# if o == "ubuntu":
#     sys.path.append("/opt/ibm/ILOG/CPLEX_Studio125/cplex/python/x86_sles10_4.1")
# if o == "centos":
#     sys.path.append("/home/ajsingh/cplex/cplex/python/x86-64_sles10_4.1")
# if o == "mac":
#     sys.path.append("/Users/james/Applications/IBM/ILOG/CPLEX_Studio1261/cplex/python/2.7/x86-64_osx")
import cplex

# --------------------------------

exp = jc.LinExp()
prob = cplex.Cplex()
prob.objective.set_sense(prob.objective.sense.maximize)

# ----------- Add Variables New Method ----------

exp.addVar(vobj = 1.0, vlb = 0, vub = 40.0, vtype = "C", vname = "x1")
exp.addVar(vobj = 2.0, vlb = 0, vub = cplex.infinity, vtype = "C", vname = "x2")
exp.addVar(vobj = 3.0, vlb = 0, vub = cplex.infinity, vtype = "C", vname = "x3")
var_obj, var_lb, var_ub, var_type, var_name = exp.getVar()
# prob.variables.add(obj = var_obj, lb = var_lb, ub = var_ub, names = var_name)
prob.variables.add(obj = var_obj, lb = var_lb, ub = var_obj, types = var_type, names = var_name)


# --------- Add Constraints ----------------

exp.addTerm(exp.var_dict["x1"], -1)
exp.addTerm(exp.var_dict["x2"], 1)
exp.addTerm(exp.var_dict["x3"], 1)
exp.addLe(20)

exp.addTerm(exp.var_dict["x1"], 1)
exp.addTerm(exp.var_dict["x2"], -3)
exp.addTerm(exp.var_dict["x3"], 1)
exp.addLe(30)

my_rhs,my_sense,const_name,con_expr = exp.getExp()
prob.linear_constraints.add(rhs = my_rhs,senses = my_sense,names = const_name,lin_expr = con_expr)

prob.write("sample.lp")
prob.set_results_stream("sample.log")
prob.solve()

val = prob.solution.get_values()
obj_val = prob.solution.get_objective_value()
print "Objective : ",
print obj_val
print "Variable Values : ",
print val





