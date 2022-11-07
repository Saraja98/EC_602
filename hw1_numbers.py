

def integer_list(number):
    digit_list=[]
    integer_list=[]
    for digit in str(number):
        
        digit_list.append(digit)
    
    integer_list=[int(x) for x in digit_list]       #converts the list from string into integer
    squares = [x*x for x in (integer_list)]         #multiplication 
    m=(sum(squares))
    return m

def integer_list_base(number):
    digit_list=[]
    #integer_list=[]
    for digit in str(number):
        
        digit_list.append(digit)
    #    print(digit_list)
    #print(digit_list)
    #integer_list=[int(x) for x in number]       #converts the list from string into integer
    #squares = [x*x for x in (integer_list)]         #multiplication 
    #m=(sum(squares))
    #print(digit_list)
    return integer_list

def converter_base(m, base):

    m = m[::-1]
    
    result = 0
    #loop over all figures
    for i in range(len(m)):
        #add the contirbution of the i-th figure
        #print(i)
        result += int(m[i])*int(base)**i  #1*2+26*37=964
        
    return result



def converter_heavy(m, base):
    m = m[::-1]
    #print(m)
    #print(m)
    result = 0
    #loop over all figures
    for i in range(len(m)):
        result += m[i]*base**i  #1*2+26*37=964
        
    return result

def digits(num,base):
    num=int(num)
    base=int(base)
    digits = []
    while num > 0:
        digit = num % base #modulas (100%37=26)(2%37=2)
        num = num // base #div value(100//37=2)(2//37=0)
        digits.append(digit)
    return digits

def convertbase(numstr,frombase,tobase):
    number = str(numstr)
    base = str(frombase)
    target_base = str(tobase)
    number = list(number)
    #print(number)
    new_ord = []
    for index, item in enumerate(number, start = 0):
        item_new = ord(item)-ord('0')
        new_ord.append(item_new)

    #print(new_ord)

    #print(converter_base(new_ord,base),type)
    var1 = converter_base(new_ord,base) #raise to power,37
    #print(var1)
    var2=(digits(var1,target_base)) #integer number formation 
    #print(var2,type(var2))
    var3=converter_base(var2,target_base)
    var4 = chr(var3+ord('0'))
    return var4

def heavy(number,base):
        m=digits(number,base)
        var2=converter_heavy(m,base)
        integer_list(var2)
        list_of_sos=[]
        list_of_sos.append(var2)
        for i in range(1,100):
            m=digits(list_of_sos[i-1],base)
            #print(list_of_sos)
            var2=converter_heavy(m,base)

            tmp=integer_list(var2)
            #print(tmp)
            if(tmp not in list_of_sos):
                list_of_sos.append(tmp)
                

            elif (tmp==1):

                return True
           

            else:
                return False 
        #print(list_of_sos)

        
    
#Given an integer, find the sum of its divisors 
def divisorsum(n):
    
    halfn=n//2
    a = range(1,halfn)
    m = [] #list of divisors
    divisor=False
    for index, item in enumerate(a, start=0):
        if n/item == n//item:
            divisor=True
            
            m.append(item)
               
        else:
            pass
    #text=print("+".join(str(i) for i in m) + "=",sum(m))
    total=sum(m)
    text="+".join(str(i) for i in m) + "="+str(total)
    return text
#for 7,19
#


def main():
    
    #print(heavy)
    #print(divisorsum)
    #n=input("Enter the number")
    print(divisorsum(int(20)))
    print(heavy(7,19))
    print(convertbase('1C',37,80))


print(__name__)
if __name__ == '__main__':
    main()
