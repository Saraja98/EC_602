from cmath import inf
from decimal import Subnormal
from sys import byteorder
import numpy 

def breakdown_float(value):
    
    if isinstance(value,numpy.float32)==True:
        f = numpy.float32(value)
        barray = f.tobytes()
        m2=(int.from_bytes(barray,byteorder='little'))
        barray=(m2.to_bytes(length=4,byteorder="big"))
        m=barray.hex()
        Subnormal=False
        x=int(m,16)
        #for exponent 
        exponent=((x& 0x7f800000)>>23)
        #for manitssa
        mantissa=((  x&0x7fffff))
        sign = x >> 31
        Subnormal=False
        if exponent==0:
            Subnormal=True

    if isinstance(value,numpy.float64)==True:
        f = numpy.float64(value)
        barray = f.tobytes()
        m2=int.from_bytes(barray,byteorder='little')
        barray=m2.to_bytes(length=16,byteorder="big")
        m=barray.hex()
        Subnormal=False
        x=int(m,16)
        exponent=((x &  0x7ff0000000000000)>>52)
        #for manitssa
        mantissa=((x   & 0x007ffff_ffff_ffff_ff))
        sign = x >> 63
        Subnormal=False
        if exponent==0:
            Subnormal=True
    if isinstance(value,numpy.float16)==True:
        f = numpy.float16(value)
        barray = f.tobytes()
        m2=int.from_bytes(barray,byteorder='little')
        barray=m2.to_bytes(length=16,byteorder="big")
        m=barray.hex()
        Subnormal=False
        x=int(m,16)
        exponent=((x &  0x7C00)>>10)
        #for manitssa
        mantissa=((x   & 0x007fff))
        
        sign = x >> 15
        print(sign)
        Subnormal=False
        if exponent==0:
            Subnormal=True
        
        

    Dict = {'sign': sign, 'fraction': mantissa, 'exponent': exponent, 'subnormal': Subnormal}
    return Dict
   


def main():
    m = numpy.float16(2.5)
    print(breakdown_float(m))



print(__name__)
if __name__ == '__main__':
    main()