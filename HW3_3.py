#multiplication


p1 = {2: 4, 1: 3 }
p2 = {2: 5, 1: 2}


p1_coeffs = list(p1.values())
#print("This is p1 coeffs", p1_coeffs)
p1_exp = list(p1.keys())
#print("This is p1 exp", p1_exp)
p2_coeffs = list(p2.values())
#print("This is p2 coeffs",p2_coeffs)
p2_exp = list(p2.keys())
#print("This is p2 exp", p2_exp)

coeffs_prod = []
exp_sum = []

for item in p1_exp:
    for item2 in p2_exp:
        a = item + item2
        exp_sum.append(a)
        
print(exp_sum)

for item in p1_coeffs:
    for item2 in p2_coeffs:
        x = item * (item2)
        coeffs_prod.append(x)
print(coeffs_prod)

test = list(zip(exp_sum, coeffs_prod))
print(test)