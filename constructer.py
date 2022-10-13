p1 = [1,2,3,6,2]
p2 = [7,48,64,78]

class Polynomial:
    def __init__(self, polynomial):
        self.polynomial = polynomial
        self.terms=[]
        N = len(polynomial)
        for i, val in enumerate(polynomial):
            #print(i,val)
            if val !=0:
                self.terms.append( (N-i-1, val) )

        dict_of_poly=(dict(self.terms))
        print(dict_of_poly)
    def copy(self):
        return Polynomial(self.terms.copy())

    def __add__(self, other):
        result = self.copy()

        for e, c in self.terms.items():
            result[e] = self.get(e, 0) + c

        return result


    #def __add__(self):
    #    print(self.terms)
    #    print(p1+p2)

    #    print("i am in add")
        
    
        





polynomial1 = Polynomial(p1) 
polynomial2 = Polynomial(p2)   
