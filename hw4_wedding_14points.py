# Copyright 2022 Shanon sghull@bu.edu
# Copyright 2022 Saraja saraja@bu.edu
# Copyright 2022 Chris Kelly  cekelly@bu.edu




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
                    
                    # Counter Clockwise (to the left) case
                    ccw_list = current_guests[1:] + current_guests[0]
                    ccw_str = ''.join(ccw_list)
                    memory[x].append(ccw_str)
                    
                    # Remaining cases where first and last letter swap, everything in between does linear shuffle
                    middle_ltrs = guests[1:-1]
                    middle_ltrs_linear = w.linear(middle_ltrs)
                    
                    for y in middle_ltrs_linear[x-2]:
                        current_str = current_guests[-1] + y + current_guests[0]
                        memory[x].append(current_str)
                        
                    
                    
            # Prints memory result in a nice format
            #print("\nShuffle Levels: {}\n".format(''.join(guests)))
            #for i in range(len(memory)):
            #    print("Level {}".format(i), memory[i])
                    
            return memory[3]

def  show_result(v, partial=False,ind=None):
  v.sort()
  if not partial:
    print(len(v),"\n".join(v),sep="\n")
  else:
    print(len(v),v[ind],sep="\n")




def standard_tests():
  standard = Wedding()
  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("WXYZ")
  show_result(res)

  res = standard.barriers("xyz", [0])
  show_result(res)

  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("abcdefXY")
  show_result(res)

  res = standard.barriers("abcDEFxyz", [2, 5, 7])
  show_result(res)

  res = standard.barriers("ABCDef", [4])
  show_result(res)

  res = standard.barriers("bgywqa", [0, 1, 2, 4, 5])
  show_result(res)

  res = standard.barriers("n", [0])
  show_result(res)
  res = standard.shuffle("hi")
  show_result(res)



def main():

  print("""Type quit to exit.
Commands:
tests
s guests
b guests n barriers
sp guests ind
bp guests n barriers ind
""")
  w = Wedding()
  while True:
    asktype=input().split()
    if not asktype or asktype[0] == "quit":
      break;
    elif asktype[0] == "tests":
      standard_tests()
    elif asktype[0] == "s":
      guests = asktype[1]
      r = w.shuffle(guests)
      show_result(r);
    elif asktype[0] == "b":
      guests,nbar,bars = asktype[1],asktype[2],asktype[3:]
      r = w.barriers(guests, [int(x) for x in bars])
      show_result(r)
    elif asktype[0] == "sp":
      guests,ind = asktype[1:]
      r = w.shuffle(guests);
      show_result(r, True, int(ind));
    elif asktype[0] == "bp":
      guests,nbar,bars,ind  = asktype[1],asktype[2],asktype[3:-1],asktype[-1]
      r = w.barriers(guests, [int(x) for x in bars])
      show_result(r, True, int(ind))
    

if __name__ == '__main__':
  main()
