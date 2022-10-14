
p1 = [1,2,3,6,2]
p2 = [7,48,64,78]

class Polynomial():
    def __init__(self,polynomial):
        self.polynomial = polynomial
        
        self.terms=[]
        N = len(polynomial)
        for i, val in enumerate(polynomial):
            #print(i,val)
            if val !=0:
                self.terms.append( (N-i-1, val) )
        poly_dict=(dict(self.terms))
        self.terms_dict=poly_dict
        #self.terms_dict=poly_dict
        #return self.terms_dict
        print(self.terms_dict,"saraja")
      
    def add(self,second_object):
        return {k: self.terms_dict.get(k, 0) + second_object.terms_dict.get(k, 0) for k in set(self.terms_dict) | set(second_object.terms_dict)}

        
    
polynomial1 = Polynomial(p1) 

polynomial2 = Polynomial(p2)  
z1 = polynomial1.add(polynomial2)



print(z1)

