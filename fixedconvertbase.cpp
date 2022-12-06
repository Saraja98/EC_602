//Copyright 2022 Shannon Hull sghull@bu.edu
//Copyright 2022 Saraja saraja@bu.edu

#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::string;
#include <vector>


int digits(int num,int base)
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
        
    }
 
    int total1=0;
    std::vector<int> integer;
    for (int i = buff.size()-1; i>=1; i--){
        int new_int = (buff[i]-48);
        //cout<<"i"<<i<<endl;
        //cout<<"new_int="<<new_int<<endl; //gives back 18, 22 (correct order)
        integer.push_back(new_int);
 

    } 
    //display(integer);
    long long output = 0;
    for (auto i : integer)
        output = output * 10 + i;
        return output;
    

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
    return total;

}


int convert_base(const std::string &s,int base,int target_base)

{   int var8,var9;
    var8=print(s,base);
    int var1=digits(var8,target_base);
    return var1;

}


int main()
{   //int m;
std::string s("");
//int base;
//int target_base;
//cout<<"provide s, base, and target base:\n";
//cin>>s>>base>>target_base;
int f=convert_base("10",10,3);
cout<<f<<endl;
   

   

return 0;
}
