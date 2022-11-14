#include <iostream>
using std::cout;
using std::cin;
using std::endl;
int main()
{
    int x,tmp;
    cout << "Type a number: "; // Type a number and press enter
    cin >> x; // Get user input from the keyboard
    //cin >> "type the number";
    //cin>> x; 
    int halfn=x/2;
    int arr[100] = { 0 };
    int total=0;
    for (int i = 1; i <= halfn; i++) {
        int remainder = (x%i);
        if (remainder==0){
            total+=i;
            tmp=i;
        cout<<x<<" "<<tmp; 
            }   
        
        
    }
}
