//Copyright 2022 Shannon Hull sghull@bu.edu
//Copyright 2022 Saraja saraja@bu.edu

#include <iostream>
#include <string>
#include <vector>
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::vector;


//vector<int> myVector;
void heat(const vector<int> &vect){
    
    for (int i = 0; i < vect.size(); i++) {
        if(i%2!=0)
           cout << "Time"<<vect[i] << " ";
        else
           cout <<"Runner"<<vect[i] << " ";
            
        
    
    }
        
    
    
    }


int main() {
   //int a;
   //vector<int> v;
   // user can add 16 element,(player,time)
   //vector <int> original = {1,2,3,4,5,6,7,8,10,11,12,13,14,15,16}; // creating the original vector

   //heat( original ); // calling the function func
   
   // user can input runner and time in pairs, with a space in between)
    vector <int> original;
    cout<<"Input runner number, then time, in pairs"<<endl;
   int runner;
   int speed;
  int n=8;
   for (int i=0; i<n; i++){
   cin>>runner>>speed;
    original.push_back(runner);
    original.push_back(speed);
   }
 


   heat( original ); // calling the function func

  // heat("12345678")

   //heat(v);
   

   return 0;
} 
   

   
