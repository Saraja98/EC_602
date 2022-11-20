#include <vector>
#include <iostream>
#include <string>
using std:: cin;
using std::cout;
using std::string;
using std::endl;
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
    //declare a vector 
  std::vector<int> num_square;
   //num_square.push_back(num);

  //cout << "Initial Vector: ";

  //for (const int& i : num_square) {
//    cout << i << "  ";
 // }
 //calculate square of each digit add them 
  int num_square_value=sum_of_squares(num,base);

  // add the squares to the vector
  //5,put in a list,go in the loop,append other sqaures depending on if they are zero or not
  num_square.push_back(num_square_value);
  //while value is not 1 keep looping and calculating the 
  //int & element = [0];
  //do the loop as long as you dont get a one or if the number repeats itself then break
  //
 
      for(int i=0;i<100;i++)
      {
        cout<<"num_square_value[i]";
        //for indexing list[0]
        int & element = num_square[i];
       int num_square_value=sum_of_squares(element,base);
       num_square.push_back(num_square_value);
       //breaking condition 
       if (num_square_value==1){
           break;
       }
          
      }
  
      
  

  cout << "\nUpdated Vector: ";

  for (const int& i : num_square) {
    cout << i << "  ";
  }

  return 0;
}
int main(){ //we should be taking input from command line, 2 arguments (plus name of program), argc = 3?
   heavy(5,20);
   //int num = 4  //will be argv[1]
   //int base = 10 //will be argv[2]
}
