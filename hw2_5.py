from decimal import Subnormal
import numpy 

def breakdown_float(value):
    
    if isinstance(value,numpy.float32)==True:
        f = numpy.float32(value)
        barray = f.tobytes()
        print(barray)
        int_val = int.from_bytes(barray, "little")
        print(int_val)
        m=barray.hex()
        #print(bin(int(m)))
        print(m)
        #t=bin(int_val)[2::]
        num_string = str(m)
        # store the size of the number
        size = len(num_string)
        # use slicing to reverse 
        reversed_num = num_string[size::-1]
        print("reversr num:",reversed_num)
        #reversed_num_removed=reversed_num[1:]
        #reversed_num_add=reversed_num+reversed_num_removed
        #output reversed number
        number=reversed_num[1:]+reversed_num[0]
        #reversed_num_removed=reversed_num[1:]
        #number=(reversed_num_removed+add_number)
        print(number)
        Subnormal=False
        x=int(number,16)
        print(x)
        #for exponent 
        exponent=((x& 0x7f800000)>>23)
        print(exponent)
        #for manitssa
        
        mantissa=((  x&0x7fffff))
        
        sign = x >> 31
    
        Subnormal=False
        if exponent==0:
            Subnormal=True

    if isinstance(value,numpy.float64)==True:
            #print("here")
    
        f = numpy.float64(value)
        barray = f.tobytes()
        # Converting to int
        int_val = int.from_bytes(barray, "little")
        m=(barray.hex())
        t=bin(int_val)[2::]
        #c='{:<064}'.format(t)
        num_string = str(m)
        # store the size of the number
        size = len(num_string)
        # use slicing to reverse 
        reversed_num = num_string[size::-1]
        reversed_num_removed=reversed_num[1:]
        reversed_num_add=reversed_num+reversed_num_removed
        #output reversed number
        for number in reversed_num:
            m=number[0]
        add_number=m
        reversed_num_removed=reversed_num[1:]
        number=(reversed_num_removed+m)
        #for exponent 
        x=int(number,16)
        print(x)
        exponent=((x &  0x7ff0000000000000)>>52)
        print(exponent)
        #for manitssa
        x=int(number,16)
        mantissa=((x   & 0x007ffff_ffff_ffff_ff))
        print("here")
        sign = x >> 63
        print(sign)
        Subnormal=False
        if exponent==0:
            Subnormal=True
    if isinstance(value,numpy.float16)==True:
        print("here 16")
    
        f = numpy.float16(value)
        barray = f.tobytes()
        # Converting to int
        int_val = int.from_bytes(barray, "big")
        m=(barray.hex())
        t=bin(int_val)[2::]
        #c='{:<064}'.format(t)
        num_string = str(m)
        # store the size of the number
        size = len(num_string)
        # use slicing to reverse 
        reversed_num = num_string[size::-1]
        reversed_num_removed=reversed_num[1:]
        reversed_num_add=reversed_num+reversed_num_removed
        #output reversed number
        for number in reversed_num:
            m=number[0]
        add_number=m
        reversed_num_removed=reversed_num[1:]
        number=(reversed_num_removed+m)
        #for exponent 
        x=int(number,16)
        print(x)
        exponent=((x &  0x7C00)>>10)
        #for manitssa
        x=int(number,16)
        mantissa=((x   & 0x007fff))
        
        sign = x >> 15
        print(sign)
        Subnormal=False
        if exponent==0:
            Subnormal=True
        
        

    Dict = {'sign': sign, 'fraction': mantissa, 'exponent': exponent, 'subnormal': Subnormal}
    return Dict
   


def main():
    m = numpy.float32(-1)
    print(breakdown_float(m))



print(__name__)
if __name__ == '__main__':
    main()