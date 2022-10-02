import time
import numpy

m = numpy.array([1],dtype= numpy.int16)


start = time.time()
while m[0]>0:
  m[0] += 1

end = time.time()
total_time = (end - start) #in seconds
total_time1=total_time*(2**(-8))*(10**(9))  #nanoseconds
total_time2=total_time*(10**6) #in microseconds
total_time3=total_time*(2**(32)) #in seconds 

total_time4=total_time*(2**(64))
years = total_time4 / 60 / 60 / 24 / 365.25 #in years 

print("measured 8-bit time (nanoseconds):"+ str(total_time1))
print("measured 16-bit time (microseconds):"+ str(total_time2))
#print(total_time)
print("estimated 32-bit time (seconds):"+ str(total_time3))
print("estimated 64-bit time (years):"+str(years))
