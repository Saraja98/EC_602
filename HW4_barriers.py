#establishing position of barriers (assuming barrier put before position 2)
guests = "abcde"
barriers = [2]
li = list(guests)
#print(li)
#num_guests = len(li)
#print(num_guests)
b_loc = barriers[0]  #finds point where to break up guest list
#print(b_loc)

#breaking up guest list according to barriers, but need to generalize!!
sep_panels = [] #creates empty list to store separated panels
sep = li[:b_loc] #all guests before barrier
sep2 = li[b_loc:] #all guests after barrier
print(sep)
print(sep2)
#puts smaller panels into a list
sep_panels.append(sep) 
sep_panels.append(sep2)
print(sep_panels)
for item in sep_panels:
    if len(item) == 1:    #keeps panel of 1 guests as-is
        item[0] = item[0]
        print(item)
    if len(item) == 2:  #swaps guests in panel of 2
        item[0],item[1] = item[1],item[0]
        print(item)
    if len(item) > 2:
        print("more than 2", item)