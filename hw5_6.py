#The function should also have an optional keyword-only parameter subnormal with default value False.
#If it is not possible to make such a float, raise a ValueError exception
from re import L
import numpy  as np


def float_parms():
    dictVal = {'sign': 0, 'fraction': 2097152, 'exponent': 128, 'subnormal': False}
    return dictVal

def construct_float(float_parms,float_type):
    #Dict = {'sign': 0, 'fraction': 562949953421312, 'exponent': 1024, 'subnormal': False}

#variable deifinations 
    
    float_parms= float_parms()
    exponent=float_parms['exponent']
    fraction=float_parms['fraction']
    sign=float_parms['sign']

    if (float_type==np.float32):
        if exponent==0:
            subnormal=True

       
        barray_fraction=fraction.to_bytes(length=4,byteorder="big")  #2,4,8
 
        b_s=bin(sign)
  
        if fraction==0:
            b_f=(bin(fraction))[2:] #add 00 format right justfied have if-else 
            b_f=b_f.zfill(22)
            
            b_e=(bin(exponent))[2:]
            b_e=b_e.zfill(1)
            
        else:
            
            b_f=(bin(fraction))[2:] #add 00 format right justfied have if-else 
            b_e=(bin(exponent))[2:]
        add=str(b_s+b_e+"0"+b_f)[2:]

        hex_Value=(hex(int(add,2)))
        #print(hex_Value)
        hex_Value=int(hex_Value,16)
        #(('0x')+fraction))
        m=(hex_Value).to_bytes(4, byteorder='little')
        #print(m)
        m2=int.from_bytes(m,byteorder='big')
        #print(m2)
        y = int.from_bytes(m, byteorder='big', signed=False) #interpret bytes as an unsigned little-endian integer (so far so good)
        #print(y)
        #z = np.float32(y) #attempt to cast as float reinterprets integer value rather than its byte values
        #print(np.float32(y))
        #print(z)
        #print(np.frombuffer(m, count=1,dtype=np.float32)
        array=np.frombuffer(m, count=1,dtype=np.float32) #count is refering to the item 
    #do the breakdown for 1(127-offset) and -1 sign 
        #print(array)
        return array[0]
    if (float_type==np.float16):

        #print("here in 16")
        barray_fraction=fraction.to_bytes(length=2,byteorder="big")  #2,4,8
        #print(barray_fraction)
        b_s=bin(sign)
        #print(b_s)
        #b_e=(bin(exponent))[2:]
        if fraction==0:
            b_f=(bin(fraction))[2:] #add 00 format right justfied have if-else 
            b_f=b_f.zfill(10)
            #print(b_f)
            b_e=(bin(exponent))[2:]
            b_e=b_e.zfill(1)
            #print(b_e)
        else:
            
            b_f=(bin(fraction))[2:] #add 00 format right justfied have if-else 
            #print(b_f.zfill(10))
            b_e=(bin(exponent))[2:]
            #print(b_e.zfill(5))
        add=str(b_s+b_e+"0"+b_f)[2:]
        #print(add)
        

        hex_Value=(hex(int(add,2)))
        #print(hex_Value)
        hex_Value=int(hex_Value,16)
        #(('0x')+fraction))
        m=(hex_Value).to_bytes(4, byteorder='little')
        #print(m)
        array=np.frombuffer(m, count=1,dtype=np.float16) #count is refering to the item 
    #do the breakdown for 1(127-offset) and -1 sign 
        #print(array)
        return array[0]
    if (float_type==np.float64):

        #print("here in 64")
        barray_fraction=fraction.to_bytes(length=8,byteorder="big")  #2,4,8
        #print(barray_fraction)
        b_s=bin(sign)
        #print(b_s)
        #b_e=(bin(exponent))[2:]
        if fraction==0:
            b_f=(bin(fraction))[2:] #add 00 format right justfied have if-else 
            b_f=b_f.zfill(52)
            #print(b_f)
            b_e=(bin(exponent))[2:]
            b_e=b_e.zfill(11)
            #print(b_e)
        else:
            
            b_f=(bin(fraction))[2:] #add 00 format right justfied have if-else 
            #print(b_f)
            b_e=(bin(exponent))[2:]
            #print(b_e)
        add=str(b_s+b_e+"0"+b_f)[2:]
        #print(add)
        

        hex_Value=(hex(int(add,2)))
        #print(hex_Value)
        hex_Value=int(hex_Value,16)
        #(('0x')+fraction))
        m=(hex_Value).to_bytes(16, byteorder='little')
        #print(m)
        array=np.frombuffer(m, count=1,dtype=np.float64) #count is refering to the item 
    #do the breakdown for 1(127-offset) and -1 sign 
        #print(array)
        return array[0]







def main():

    #Dict = {'sign': 0, 'fraction': 562949953421312, 'exponent': 1024, 'subnormal': False}
    
    print(construct_float(float_parms,np.float32))



print(__name__)
if __name__ == '__main__':
    main()