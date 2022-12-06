//Copyright 2022 Shannon Hull sghull@bu.edu
//Copyright 2022 Saraja saraja@bu.edu

#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::string;

char digits(int num,int base)
{   int length=0;
    int result=1;
    int numVal = 0;
    //int numArray [2];
    string buff = " ";
    while (num > 0){
        //{
        //int total1;
        length++;
        int digit = num % base; //modulas (100%37=26)(2%37=2)
        buff += digit +'0';
        num = num / base;
        //cout<<"buff:"<<buff<<endl;



        //}
    //for(int i = buff.length() - 1; i >= 0; cout << buff[i--])
    //cout<<buff.length()-1<<endl;
    //cout << endl;
    }
    //cout<<"buff0"<<buff[1]<<endl;
    //for (int i = 1; i<=buff.length()-1; i++)
    int total1=0;
    for (int i = buff.size()-1; i>=1; i--){
        int new_int = (buff[i]-48);
        cout<<new_int; //gives back 18, 22 (correct order)
        int result = 1;  
        int power = buff.length() -i -1;
        for (int m=0; m<power; m++){
            result = result*base;  //only giving 80, but its ok because 18 is still stored
            //cout<<"result"<<result<<endl;

        
        }
            int final_var = result*new_int;  //is giving 18 and 80, which we want
            //cout<<"final_var"<<final_var<<endl;
            //int total1;
            total1 += final_var;  



    }   
    //cout<<total1<<endl;  //prints out 1778, which we want
    char final_char = char(total1);
    //cout<<final_char<<endl;
   //return total1; 
   return final_char;
}

   
//function to raise to the power, 22 and 18 ===

int print(const std::string &s,int base)
{   int total=0;
for (int i = s.size() - 1; i >= 0; i--) {
        //std::cout << s[i] << ' ';
        int power;
        //cout<<"this is i"<<i<<endl;
       //i=1

       
        int var1=(s[i]-48);
//cout << "this is var1"<<var1<<endl;
        //pow did not work so raising base to i using this loop
        //for m=0,its 1

        int exp=s.size() - i-1;
        int result=1;
        for(int m = 0; m < exp; m++){
            result = result * base;
           

            }
            int var3= result*var1;
            //cout<<"var3:"<<var3<<endl;
            total+=var3;
    }
    //cout << "total:"<< total<<endl;
       
        //cout<<"this is result"<<result<<endl;
           
    return total;
 
        //total has to be passed through a function again to convert it into the target base
    //int var4=digits(total,target_base);

}


int convert_base(const std::string &s,int base,int target_base)

{   int var8,var9;
    var8=print(s,base);
    //cout<<"total:"<<var8<<endl;
    //total has to be passed through a function again to convert it into the target base
    int var1=digits(var8,target_base);
    //cout<<"var4:"<<var4<<endl;
    //var9=print(s,target_base);
    //cout<<"var9:"<<var9<<endl;


   
    return var1;
 

     

 

        //std::cout << (int(s[i])-48)*power << ' ';

}


int main()
{   int m;
std::string s("");
int base;
int target_base;
cout<<"provide s, base, and target base:\n";
cin>>s>>base>>target_base;
convert_base(s,base,target_base);
    //cout<<m<<endl;
   

   

return 0;
}