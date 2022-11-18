#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(){
    string input = "1C";
    int start_base = 37;
    int new_base = 80;
    //get inputs
    //cout<< "Enter string, start base, new base:\n ";
    //cin>> input>>start_base>>new_base;
    int total = 0;
    for (int i = input.size() - 1; i >= 0; i--) {
        int var1=(input[i]-48); //start here - getting the integer version of each character in the string in reverse order
        //cout<<var1<<endl;  
        int exp=input.size() - i-1; //getting exponents that the bases will be raised to 
        //cout<<exp<<endl;  
        int result;             //changed so not equal to 1 at the beginning anymore
        for(int m = 0; m <=exp; m++){  // setting up loop to raise base to exponents, fixed to m<=exp, except this outputs 0 twice
            result = m * start_base; // fixed so multiplying m and start_base?  But this still doesn't equate to raising to an exponent 
            cout<<result<<endl; //do we need a loop to replicate the result of raising a base to an exponent? 
            
            int var2=var1*result;
            total += var2; //all the var2 need to be added before the // and % steps
    while (total>0){  //will probably have to make this a separate function
        int digit = total % new_base; // fixed so using target_base instead of starting base
        total = total / new_base;
        cout<<digit<<endl; 
    
    

    }
        
           

        }
    }


}