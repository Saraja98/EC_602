// C++ program to print all
// permutations with duplicates allowed
//#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;

// Function to print permutations of string
// This function takes three parameters:
// 1. String
// 2. Starting index of the string
// 3. Ending index of the string.

void permute(string& a, int l, int r)
//vector<string> permute(string& a, int l, int r)
{  
	// Base case
	if (l == r){
	    //cout << a << endl;
	    
	
	    vector<string> v;
	    v.push_back(a);
	   
	   
	   
	    int n=v.size();
	    //return v;
	    //iterate over v
        for(auto item: v){
            cout << item << endl;
            //return item;
          }
        }  
	else {
		// Permutations made
		for (int i = l; i <= r; i++) {
		    //cout<<i<<endl;
		    

			// Swapping done
			swap(a[l], a[i]);

			// Recursion called
			permute(a, l + 1, r);

			// backtrack
			swap(a[l], a[i]);
		}
	}
}
string conversion(std::vector<string> boards)
{
    std::string s;
    for (std::vector<std::string>::const_iterator i = boards.begin(); i != boards.end(); ++i)
        s += *i;
    return s;
}

std::vector<string> get_all_boards( )
{
     
      vector<string> boards;
      boards= {"1", "2", "3"};
      //cout<<"i am here"<<endl;
      string str=conversion(boards);
      //cout<<str<<endl;
      int n = str.size();
      //cout<<n;
      vector<string> m;
      
      permute(str, 0, n - 1);
 
      //cout<<m;
	

      //return boards;
}

// Driver Code
int main()
{
	//string str = "1234";
	//int n = str.size();

	// Function call
	//permute(str, 0, n - 1);
	get_all_boards();
	return 0;
}

// This is code is contributed by rathbhupendra
