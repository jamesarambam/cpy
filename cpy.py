"""
Author = James Arambam
Dated = 31 Dec 2014

"""


# -------------- Cplex Libraries --------

class LinExp:

   global constr, var_id_dict, var_id_count

   constr = 0
   var_id_dict = {}
   var_id_count = -1

   def __init__(self):

        self.Exp = []
        self.var = []
        self.coeff = []
        self.sense = []
        self.rhs = []
        self.name = []
        self.var_dict = {}
        self.var_count = -1
        self.vName = []
        self.vObj = []
        self.vLb = []
        self.vUb = []
        self.vType = []

   def addVar(self, **var):

       self.var_count += 1
       self.var_dict[str(var.get("vname"))] = self.var_count
       self.vObj.append(var.get("vobj"))
       self.vName.append(var.get("vname"))
       self.vLb.append(var.get("vlb"))
       self.vUb.append(var.get("vub"))
       self.vType.append(var.get("vtype"))

   def getVar(self):
       return self.vObj, self.vLb, self.vUb, self.vType, self.vName

   def addTerm(self,var_id,coeff):

       global var_id_dict, var_id_count
       self.var.append(var_id)
       self.coeff.append(coeff)
       if len(self.var) != len(set(self.var)):
           self.var.pop()
           self.coeff.pop()
           self.coeff[var_id_dict[var_id]] = self.coeff[var_id_dict[var_id]] + coeff
       else:
           var_id_count += 1
           var_id_dict[var_id] = var_id_count

   def addLe(self,rb):

       global constr
       constr += 1
       name = "c"+str(constr)
       self.Exp.append([self.var,self.coeff])
       self.var = []
       self.coeff = []
       self.sense.append("L")
       self.rhs.append(rb)
       self.name.append(name)

   def addGe(self,rb):

       global constr
       constr += 1
       name = "c"+str(constr)
       self.Exp.append([self.var,self.coeff])
       self.sense.append("G")
       self.rhs.append(rb)
       self.name.append(name)
       self.var = []
       self.coeff = []

   def addEq(self,rb):

       global constr
       constr += 1
       name = "c"+str(constr)
       self.Exp.append([self.var,self.coeff])
       self.sense.append("E")
       self.rhs.append(rb)
       self.name.append(name)
       self.var = []
       self.coeff = []

   def getExp(self):
       return self.rhs,self.sense,self.name,self.Exp

   def sol(self, val):

       temp = {}
       keys = self.var_dict.keys()
       for v in keys:
           temp[v] = val[self.var_dict[v]]
       return temp

   def printSol(self, val):

       keys = self.var_dict.keys()
       for v in keys:
           print v, ":", val[self.var_dict[v]]

#-----------------------------------------

