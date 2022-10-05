#float16
max_i= 10
e_range = range(15,46)
list_of_var1 = []
for item in e_range:
    var1 = item-int(15)
    list_of_var1.append(var1)
for item in list_of_var1:
    var2 = item - max_i
    if var2 == 1:
        print(2**item)
    else:
        pass

#float32
max_i= 23
e_range = range(127,382)
list_of_var1 = []
list_of_var2 = []
for item in e_range:
    var1 = item-int(127)
    list_of_var1.append(var1)
for item in list_of_var1:
    var2 = item - max_i
    if var2 == 1:
        print(2**item)
    else:
        pass

#float64
max_i= 52
e_range = range(1023,3070)
list_of_var1 = []
for item in e_range:
    var1 = item-int(1023)
    list_of_var1.append(var1)
for item in list_of_var1:
    var2 = item - max_i
    if var2 == 1:
        print(2**item)
    else:
        pass

#float128
max_i= 112
e_range = range(16383,49150)
list_of_var1 = []
list_of_var2 = []
for item in e_range:
    var1 = item-int(16383)
    list_of_var1.append(var1)
for item in list_of_var1:
    var2 = item - max_i
    if var2 == 1:
        print(2**item)
    else:
        pass