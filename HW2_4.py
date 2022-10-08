import numpy as np
#max double: e = 2046, i = 52
#smallest double: e=1, i = 52
double_i_range = range(1,53)
maxdouble_bias_value = ((2**11)//2)-1 # = 1023
mindouble_bias_value = maxdouble_bias_value - (maxdouble_bias_value -1) #=1

#max single (largest normal): e = 254, i = 23
#smallest single: #e = 1, i = 23 
single_i_range = range(1,24)
maxsingle_bias_value = ((2**8)//2)-1 # = 127
minsingle_bias_value = maxsingle_bias_value - (maxsingle_bias_value -1) #=1

def largest_double():
    exponent_double1 = 2**maxdouble_bias_value
    fraction1 = 2**-(max(double_i_range))
    a=exponent_double1 * (2-fraction1)
    return (np.float64(a))

def smallest_double():
    exponent_double2 = 2**(mindouble_bias_value - maxdouble_bias_value)
    fraction2 = 2**-(max(double_i_range))
    b=exponent_double2 * fraction2
    return (np.float64(b))

def largest_single():
    exponent_single1 = 2**maxsingle_bias_value
    fraction3 = 2**-(max(single_i_range))
    c=exponent_single1 * (2-fraction3)
    return (np.float32(c))

def smallest_single():
    exponent_single2 = 2**(minsingle_bias_value - maxsingle_bias_value)
    fraction4 = 2**-(max(single_i_range))
    d=exponent_single2 * fraction4
    return (np.float32(d))

largest_double()
smallest_double()
largest_single()
smallest_single()
