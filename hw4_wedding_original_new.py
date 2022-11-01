
def linear(guests):
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
def shuffle(guests):
     


        n = len(guests)
        
        
        memory = linear(guests) # memory for shuffle starts off as memory for linear function
        
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
                middle_ltrs_linear = linear(middle_ltrs)
                
                for y in middle_ltrs_linear[x-2]:
                    current_str = current_guests[-1] + y + current_guests[0]
                    memory[x].append(current_str)
                    
                
                
        # Prints memory result in a nice format
        print("\nShuffle Levels: {}\n".format(''.join(guests)))
        for i in range(len(memory)):
            print("Level {}".format(i), memory[i])
                
        return memory


def main():
    
    print(shuffle("afwerg"))

if __name__ == '__main__':
  main()
