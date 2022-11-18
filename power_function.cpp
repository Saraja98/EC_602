#include <iostream>
using std::cin;
using std::cout;
using std::endl;

//given base and exponent, raise the base to the exponent

int main(){
    int base=2;
    int exp=4;
    //int arr[100]={0};
    int total = 1;

    for (int i=0; i<exp;++i){
        total *= base;
    cout<<total<<endl;

    }



}


