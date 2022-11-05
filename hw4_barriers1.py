# Copyright 2022 Shanon sghull@bu.edu
# Copyright 2022 Saraja saraja@bu.edu
# Copyright 2022 Chris Kelly  cekelly@bu.edu


from itertools import product

class Wedding():
    def __init__(self) -> None:
         pass

    def linear(self,guests):
                n = len(guests)
                memory = n*[''] # Creates empty list to store recursion results for future reference
                
                for x in range(n):
                    
                    # Hardcoding first two levels is necessary for recursion-like behavior
                    if x == 0:
                        memory[0] = [guests[0]]
                    if x == 1:
                        memory[1] = [guests[0] + guests[1], guests[1] + guests[0]]
                    if x >= 2:
                        
                        # Adds the next guest to the end of each of the previous levels combinations 
                        # Example: If next guest is d [abc,bac,acb] becomes [abcd,bacd,acbd]
                        memory[x] = []
                        for y in range(len(memory[x-1])):
                            memory[x].append(memory[x-1][y] + guests[x])
                        
                        # Finds remaining combinations for this level
                        # Pulls n-2 level and adds the reverse of last two letters to each combination
                        # Example: For level 3, pulls level 1 [ab, ba] and adds dc to each level 1 entry
                        last_2_reversed = guests[x] + guests[x-1]
                        for y in range(len(memory[x-2])):
                            memory[x].append(memory[x-2][y] + last_2_reversed)
                    
                return memory
    def shuffle(self,guests):
        


            n = len(guests)
            w=Wedding()
          
            
            
            memory = w.linear(guests) # memory for shuffle starts off as memory for linear function
            
            for x in range(n):
                # Level 0 and level 1 remained unchanged, so we skip those
                if x >= 2:
                    current_guests = guests[:x+1] # Creates list with only first x+1 number of guests
                
                    # Clockwise (to the right) case
                    cw_list = current_guests[-1] + current_guests[:-1]
                    cw_str = ''.join(cw_list)
                    memory[x].append(cw_str)
                    #print(memory)
                    
                    # Counter Clockwise (to the left) case
                    ccw_list = current_guests[1:] + current_guests[0]
                    ccw_str = ''.join(ccw_list)
                    memory[x].append(ccw_str)
                    #print(memory)
                    
                    # Remaining cases where first and last letter swap, everything in between does linear shuffle
                    middle_ltrs = guests[1:-1]
                    middle_ltrs_linear = w.linear(middle_ltrs)
                    
                    for y in middle_ltrs_linear[x-2]:
                        current_str = current_guests[-1] + y + current_guests[0]
                        memory[x].append(current_str)
                        memory
            #for i in t[3]:
            #    pri    
            # Prints memory result in a nice format
            #print("\nShuffle Levels: {}\n".format(''.join(guests)))
            #for i in range(len(memory)):
                #print("Level {}".format(i), memory[i])
                    
            return memory


    def barriers(self, guests, barriers):
        
        #establishing position of barriers 
        #guests = "abcde"
        #barriers = [2,3]
        w=Wedding()
        li = list(guests)
        combos = [] #empty list to put rearranged individual panels in
        if (len(barriers) == 1) and (str(0) in barriers):  #send guests string to linear function if 1 barrier at 0
            print("regular panel")
            final = w.linear.Wedding(guests) 
        else:
            pass

        #breaks into separated panels
        s = barriers+[len(li)]
        sep_panels = ([li[i1:i2] for i1,i2 in zip([0]+s[:-1],s)])
        #new_s = "".join(sep_panels)
        #print(new_s)
        for i in sep_panels:
           
            new_s = "".join(i)
        
            m=w.linear(new_s)
   
            arr1=(m[len(i)-1])


            
        print(len(sep_panels))

        #swapping guests in each separated panel
        for item in sep_panels:

            if len(item) == 1:    #keeps panel of 1 guests as-is
            
                combos.append(item)
            if len(item) == 2:  #swaps guests in panel of 2
                item[0],item[1]= item[1],item[0]
               
                combos.append(item)
            if len(item) > 2:
                w=Wedding()
                print("more than 2", item)
                w.linear.Wedding(item)  #will need to convert item to a string first!
        print("these are combos",combos) #shows list of now-swapped panels

        #swaps first and last guests if no barrier at 0 
        #if not str(0) in barriers:
            #print("no zero")
            #end_swap = li[0], li[-1] = li[-1], li[0] 

      




def main():

  w = Wedding()
  w.barriers("abcdef",[2,3])
  
    

if __name__ == '__main__':
  main()
