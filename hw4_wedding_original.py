rom numpy import append
from panel import panel


class Wedding: 
    def __init__(self):
      
      self.linear=[["a"],["ab","ba"]]
    def panel(self,n):
      #n is a number 
      print("i am in panel")
      if n<=len(self.linear):
        return n
      #new val when c comes in 
      else:
        result=[]
        for s in self.linear[0]:
            result.append(s+"cb")  #a+cb=acb
        for s in self.linear[1]:
            result.append(s+"c")  #a+cb=abc,bac
        #above code is only for linear 
        return result

    def shuffle(self, guests):
      #call panel in shuffle 
      w = Wedding()
      m=w.panel(3)
      for i in m:
        print(i)
        
      print(guests[1:]+guests[0])
      print(guests[-1]+guests[:-1])

      #swapping
      print(guests[-1:] + guests[1:-1] + guests[:1])


     
      
    def barriers(self, guests, bars):
      pass
    
        
 




def main():
    w = Wedding()
    w.shuffle("abc")

if __name__ == '__main__':
  main()
