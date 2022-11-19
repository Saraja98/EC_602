/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int digits(int num,int base)
{   int length=0;
    int result=1;
    int numVal = 0;
    int numArray [2];
    while (num > 0){
        for (int i=0; i<2; i++){
        int total1;
        length++;
        int digit = num % base; //modulas (100%37=26)(2%37=2)
        num = num / base;
        cout<<"digit:"<<digit<<endl;
        //cout << "[" << digit << "] = ";
        

        numArray[i] = digit;


        
}
cout<<numArray[1] <<" ";        
cout<<numArray[0] <<" ";   
result=1;
for(int m = 0; m <length-1 ; ++m){
    std::cout << "m" <<m<< std::endl;
    result = result * base;
    cout<<"result:"<<result<<endl;
    
}

int total1=1;
//index into the array from 0 to 10
//cout<"size of:"<<sizeof(numArray);
for(int i=0;i < sizeof(numArray)/sizeof(int);i++){
    int final=result*numArray[i];
    total1=total1+final;
    cout<<"final"<<final<<endl;

}



//cout<<numArray[0] <<"  ";
}
 

}

        
        //for(int m = 0; m < length; m++){
         //   std::cout << "m" <<m<< std::endl;
         //   result = result * base;
            
        //}
            //cout<<"result:"<<result<<endl;
            //int final=result*digit;
            //total1+=final;
            //cout<<"final"<<final<<endl;
            
           
        
    //return digit;
       
    
    
    
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
    cout<<"total:"<<var8<<endl;
    //total has to be passed through a function again to convert it into the target base 
    int var4=digits(var8,target_base);
    //cout<<"var4:"<<var4<<endl;
    //var9=print(s,target_base);
    //cout<<"var9:"<<var9<<endl;


   
    //return var;
  

     

  

        //std::cout << (int(s[i])-48)*power << ' ';

	}


int main()
{   int m;
	std::string s("12C");
	convert_base(s,37,80);
    //cout<<m<<endl;
    

    

	return 0;
}
