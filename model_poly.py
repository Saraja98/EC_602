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
    def subtract(self,second_object):
        print(self.terms_dict)
        return {key: self.terms_dict[key] - second_object.terms_dict.get(key, 0) for key in self.terms_dict}
    def eval(self,x):
        #print("i am in eval")
        p=self.terms_dict
        
        
        x_raised = []
        for key in p:
            pow = x**key
            x_raised.append(pow)
        
        coeff_list = list(p.values())
        #print(coeff_list)
        res = list(zip(coeff_list, x_raised))
        #print(res)
        term_list = []
        for elem in res:
            term_mult = elem[0]*elem[1]
            term_list.append(term_mult)
        #print(term_list)
        return sum(term_list)
    def deriv(self):
        p=self.terms_dict.items()
        result = result = {(key-1): num * key for key, num in p if num * key!=0}
        return result


        


    
