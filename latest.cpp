//Copyright 2022 Shannon Hull sghull@bu.edu
//Copyright 2022 Saraja saraja@bu.edu

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::pair;
using std::make_pair;
void sortArr(vector<int> &vect, int n,vector<int> &Player)
{

	// Vector to store element
	// with respective present index
	vector<pair<int, int> > vp;

	// Inserting element in pair vector
	// to keep track of previous indexes
	for (int i = 0; i < n; ++i) {
		vp.push_back(make_pair(vect[i], i));
	}

	// Sorting pair vector
	sort(vp.begin(), vp.end());

	// Displaying sorted element
	// with previous indexes
	// corresponding to each element
	cout << "Element\t"
		<< "index" << endl;
	for (int i = 0; i < vp.size(); i++) {
		cout << vp[i].first<<endl;
		//second is the previous index which will be mapped to the player
	
        
            //std::cout << Player[i].Player<< ' ';
		    int m=vp[i].second;
		    //cout<<m<<endl;
		    cout<<"Player"<<Player[m]<<endl;
	}
}
void print(std::vector <int> const &a) {
   std::cout << "The vector elements are : ";

   for(int i=0; i < a.size(); i++)
   std::cout << a.at(i) << ' ';
}


//vector<int> myVector;
void heat(const vector<int> &vect){
    vector<int> Time;
    vector<int> Player;
    
    for (int i = 0; i < vect.size(); i++) {
        if(i%2==0){
           Player.push_back(vect[i]);
           //cout << "Time"<<vect[i] << " ";
                   }
        else{
            Time.push_back(vect[i]);
            //cout <<"Player"<<vect[i] << " ";
            }
            
        
    
    }
    print(Player);
    //now I will map the sorted time to the player to decide who won 1st ,2nd,3rd 
    //Keep track of previous indexes after sorting a vector so that I can map it back 
    //int n = sizeof(Time) / sizeof(Time[0]);
	sortArr(Time, 8,Player);
    
    
    

    
    
        
    
    
    }


int main() {

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
   

   return 0;
} 
   

   
