// Copyright 2022 Saraja Kadambari saraja@bu.edu
// Copyright 2022 Shannon Hull sghull@bu.edu


#include <vector>
#include <iostream>
#include <string>
using std:: cin;
using std::cout;
using std::string;
using std::endl;
using std::stoi;
int sum_of_squares (int num, int base){ //function to put input in the assigned base

    int rem, sum = 0;
    while (num>0){
        
        rem = num%base;
        int square = rem*rem;
        
        sum+=square;
        num = num/base;
    }
    return sum;
}

int heavy(int num, int base) {
  std::vector<int> num_square;
  int size = num_square.size(); //this is not giving how many terms in the  

  int num_square_value=sum_of_squares(num,base);

  num_square.push_back(num_square_value);

 
      for(int i=0;i<100;i++)
      {
        //cout<<"num_square_value[i]";
        //.at does error cheacking ,raises exception,easy debugging
        
        int & element = num_square.at(i);
       int num_square_value=sum_of_squares(element,base);
       num_square.push_back(num_square_value);
       //breaking condition 
       if (num_square_value==1){
           //cout<<"1"<<endl;
           return 1;
           break;
       }
       else{
       continue;
          
      }

}
  if (num_square.size() == 101){  //this if/else statement is inside heavy, but outside all other loops
        //cout<<"0"<<endl;
        return 0;
} 
    
  }
int main(int argc, char** argv){
    //we should be taking input from command line, 2 arguments (plus name of program), argc = 3?
    //std::cout << "Have " << argc << " arguments:" << std::endl;
    if (argc >= 2)
         {
             int val = stoi(argv[1]);
             int base = stoi(argv[2]);
             cout<<heavy(val,base)<<endl;
             return heavy(val,base);
              
         }
         
         

}