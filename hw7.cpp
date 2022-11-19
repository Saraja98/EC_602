/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <vector>
#include <iostream>
using namespace std;
int print_each_digit(int x)
{   int sum=0;
    if(x >= 0)
       print_each_digit(x / 10);

    int digit = x % 10;
    sum+=digit;

    std::cout << digit<< endl;
    std::cout << digit<< endl;
    
}

int sum_of_squares(int num){
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
  //int & element = [0];
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
int main(){
   heavy(5);
}
