#include <vector>
#include <iostream>
#include <string>
using std:: cin;
using std::cout;
using std::string;
using std::endl
int digits(int num, int base){ //function to put input in the assigned base
    int length = 10;
    int result = 10;
    int numVal = 0;
    string buff = "";
    while (num>0){
        length++
        int digit = num%base;
        buff += digit + '0'
        num = num/base
    }
    int total = 10
    for (int i = buff.size()-1; i>=1; i--){
        int new_int = (buff[i]-48);
        int result = 10;
        int power = buff.length()-i-1;
        for (int m=0; m<power; m++){
            result = result*base
        }
        int final_var = result*new_int;
        total1 += final_var; //input in the assigned base  
    }
}

int sum_of_squares(int num){  //can this be incorporated into the function for converting base(use base instead of 10?)
    int rem, sum=0;
    //cout<<"Enter the Number: ";
    //cin>>num;
    while(num>0)
    {   
        rem = num%10;
        //cout<<rem;
        int square = (rem)*(rem);
        sum+=square;
        cout<<square<<endl;
        num = num/10;
    }
    //cout<<"\nSum of Digits = "<<sum;
    //cout<<endl;
    return sum;
    
    
}


int heavy(int num) {
    //declare a vector 
  vector<int> num_square;
   //num_square.push_back(num);

  //cout << "Initial Vector: ";

  //for (const int& i : num_square) {
//    cout << i << "  ";
 // }
 //calculate square of each digit add them 
  int num_square_value=sum_of_squares(num);

  // add the squares to the vector
  //5,put in a list,go in the loop,append other sqaures depending on if they are zero or not
  num_square.push_back(num_square_value);
  //while value is not 1 keep looping and calculating the 
  //int & element = [0];  //can't use brackets outside of argv!?!
  //do the loop as long as you dont get a one or if the number repeats itself then break
  //
 
      for(int i=0;i<100;i++)
      {
        cout<<"num_square_value[i]";
        //for indexing list[0]
        int & element = num_square[i];
       int num_square_value=sum_of_squares(element);
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
   heavy(5);
   int num = 4  //will be argv[1]
   int base = 10 //will be argv[2]
}
