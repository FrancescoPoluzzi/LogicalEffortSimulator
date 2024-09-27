import numpy as np

class Inv():    

    def __init__(self,gamma=1):   #metodo costruttore
        self._gamma=gamma
    def p():
        return 1
    def g():
        return 1
    def h(self,cl):
        return cl/self._cin
    def cin(self):
        return 3*self.gamma

class Nand():    

    def __init__(self,gamma=1):   #metodo costruttore
        self._gamma=gamma

    def p():
        return 2
    def g():
        return 4/3
    def h(self,cl):
        return cl/self._cin
    def cin(self):
        return 4*self.gamma

class Nor():   

    def __init__(self,gamma=1):   #metodo costruttore
        self._gamma=gamma

    def p():
        return 2
    def g():
        return 5/3
    def h(self,cl):
        return cl/self._cin
    def cin(self):
        return 5*self.gamma
    
class Circuit():
    def __init__(self,gates,branches,cl,cin):   #metodo costruttore    
        self._gates=gates
        self._cl=cl
        self._cin=cin
        self._branches=branches  #list of nuber of branches

    def delay_min(self):
        p_sum=0
        for i in range (len(self.gates)):
            p_sum=p_sum+self.gates[i].p()

        return p_sum+(len(self.gates)*self.f_hat())
    
    def logical_effort(self):
        p,g,h=np.zeros(len(self.gates))
        delay=0
        for level,gate in enumerate(self.gates):
            p[level]=gate.p()
            g[level]=gate.g()
            h[level]=gate.h()
            delay=delay+(gate.p+gate.g*gate.h)
        return delay
    
    def B(self):
        B=1
        for b in self.branches:
            B=b*B
        return B
    
    def G(self):
        G=1
        for g in self.gates:
            G=g.g()*G
        return G

    def H(self):
        H=1
        for i, gate in enumerate(self.gates):
            H=gate.h( cl = self.gates[i+1].cin ) * H
        return H

    
    def f_hat(self):
        return (self.G()*self.H()*self.B())**(1/len(self.gates)) 

    def optimum_sizes(self):
        gammas=np.zeros(len(self.gates))
        gamma1=self.gates[i].gamma
        g_prod=1
        for i in range (len(self.gates)):
            if (i==0) :
                gammas[i]=gamma1
            else :
                g_prod=g_prod*self.gates[1].g()
                gammas[i]=(self.f_hat**i)*gamma1/g_prod
        return gammas
    
    def resize(self,gammas):
        for i, gate in enumerate (self.gates):
            gate.gamma=gammas[i]
