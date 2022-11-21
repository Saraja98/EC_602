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
  std::vector<int> num_square;
  int size = num_square.size();

  int num_square_value=sum_of_squares(num,base);

  num_square.push_back(num_square_value);

 
      for(int i=0;i<100;i++)
      {
        cout<<"num_square_value[i]";
        //for indexing list[0]
        int & element = num_square[i];
       int num_square_value=sum_of_squares(element,base);
       num_square.push_back(num_square_value);
       //breaking condition 
       if (num_square_value==1){
           cout<<"heavy 1"<<endl;
           break;
       }
       else{
       continue;
          
      }
  if (size == 100){
        cout<<"not heavy 0"<<endl;
        } //do not want an else statement, can we do that??
      
  

  cout << "\nUpdated Vector: ";

  for (const int& i : num_square) {
    cout << i << "  ";
  }

  return 0;
}

}
int main(){ //we should be taking input from command line, 2 arguments (plus name of program), argc = 3?
   heavy(5,20);

}
