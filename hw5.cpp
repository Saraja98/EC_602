// Copyright 2022 Shannon Hull sghull@bu.edu
// Copyright 2022 Saraja saraja@bu.edu 

#include <iostream>
#include <cstdint>
using std::cout;
using std::cin;
using std::endl;
int main(){

    while (true){

        int x;
        cout << "Type a number: "; // Type a number and press enter
        cin >> x; // Get user input from the keyboard

        if (x == 0){
            break;
        }
        else{

    
    
        int halfn=x/2;
        int arr[100] = {0};
        int total=0;
        cout<<x<<":";
        for (int i = 1; i <= halfn; i++) {
            int remainder = (x%i);
            if (remainder==0){
                total+=i;
                int tmp = i;
            //cout<<tmp;
        cout<<tmp<<"+";    
        //cout<<x<<":"<<tmp; 
                }   
        
        }
        cout<<"="<<total;
        //return 0;  //need to exit program when 0 is entered
        }
    }
}
