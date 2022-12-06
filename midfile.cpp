//Copyright 2022 Shannon Hull sghull@bu.edu
//Copyright 2022 Saraja saraja@bu.edu

#include <iostream>
using std::cout;
using std::cin;
using std::endl;
#include <vector>

using std::string;

//Print function
template <typename T>
void display_vector(const std::vector<T> & vec)
{
    for(int i = 0; i < vec.size() ; i++)
    {
        std::cout<<vec[i];
    }
    std::cout<<std::endl;
}
// Replace function..
string replace(string word, string target, string replacement){
    int len, loop=0;
    string nword="", let;
    len=word.length();
    len--;
    while(loop<=len){
        let=word.substr(loop, 1);
        if(let==target){
            nword=nword+replacement;
        }else{
            nword=nword+let;
        }
        loop++;
    }
    return nword;

}



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

std::vector<string> get_all_boards( )

{   
for(int i=0;i<=19682;i++)
{
 std::string s = std::to_string(i);
 //std::cout<<"i="<<i<<endl;
 

    int y=convert_base(s,10,3);
    //cout<<"y-"<<y<<endl;
    std::string old_str = std::to_string(y);
    //cout<<"old_str-"<<old_str;
    
    
    auto new_str = std::string(9-old_str.length(), '0') + old_str;
    //cout<<"new_str="<<new_str<<endl;
    std::vector<string> values;
    for (auto &ch : new_str)
    
    {
      //cout<<old_str.at(r)<<endl;
      
      
      string k=replace(new_str, "0", "#");
      //cout<<"k-"<<k<<endl;
      
      string l=replace(k, "1", "x");
      //cout<<"l-"<<l<<endl;
      
      string m=replace(l, "2", "o");
      values.push_back(m);
      
      
      }
      return values;
     
    
    //std::cout<<m<<std::endl;
}
    //cout<<m<<endl;
 //return 0;
}
int main(){
   // std::vector<string>
    std::vector<string> even_vect= get_all_boards();
    display_vector(even_vect);
}
