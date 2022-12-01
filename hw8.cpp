
#include<iostream>
#include<string>
#include<array>
#include<vector>
#include<map>
//#include<movedef.h>
using namespace std;
// This matrix is used to find indexes to check all
// possible winning triplets in board[0..8]
int win[8][3] = {{0, 1, 2}, // Check first row.
                {3, 4, 5}, // Check second Row
                {6, 7, 8}, // Check third Row
                {0, 3, 6}, // Check first column
                {1, 4, 7}, // Check second Column
                {2, 5, 8}, // Check third Column
                {0, 4, 8}, // Check first Diagonal
                {2, 4, 6}}; // Check second Diagonal
bool isCWin(char *board, char c)
{
    // Check all possible winning combinations
    for (int i=0; i<8; i++)
        if (board[win[i][0]] == c &&
            board[win[i][1]] == c &&
            board[win[i][2]] == c )
            return true;
    return false;
}


void isValid(char board[9])
{
    // Count number of 'X' and 'O' in the given board
    //cout<<"board"<<board<<endl;
    int xCount=0, oCount=0,hashCount=0;
    for (int i=0; i<9; i++)
    {
    if (board[i]=='x') 
        xCount++;
    if (board[i]=='o') 
        oCount++;
    if (board[i]=='#')
        hashCount++;
    }
    cout<<"x"<<xCount<<endl;
    cout<<"o"<<oCount<<endl;
    cout<<"#"<<hashCount<<endl;
    bool flag=false;
     // Board can be valid only if either xCount and oCount
    // is same or count is one more than oCount
    //xCount>2*(oCount)
    // if ( xCount != oCount + 1 || xCount<3 || xCount<oCount)
    if (  xCount<oCount ||xCount<3||(oCount==hashCount) && (xCount>oCount))
    {
        cout<<"i:invalid";
   
}
//It is invalid because x played 5 times and o only played 2 times
//check if x is wining 

    else if((xCount==oCount || xCount==oCount+1||hashCount==xCount+1))
    {   // Check if 'O' is winner
        if (isCWin(board, 'o')){
            
            
            // Check if 'X' is also winner, then
           
            //if (isCWin(board, 'x'))
            //{
            //    cout<<"i:invalid";
                
            //}
            
            cout<<"o: valid, o has won";
            flag=true;
            
            
        }
        
        //// If 'X' wins, then count of X must be greater
            if (isCWin(board, 'x')){
            cout<<"x: valid, x has won";
            flag=true;
            
            
            // Check if 'X' is also winner, then
            // return false
            //if (isCWin(board, 'o')){
            //    cout<<"i:invalid";}
            //else{
            //cout<<"o: valid, o has won";
                
            //}
            if(hashCount>xCount&&flag==false){
             cout<<"c: valid, game continues";
        }
        }
        if(hashCount>xCount&&flag==false)
            {
             cout<<"c: valid, game continues";
            }
      
   
}
}

char tttresult(string tttboard){
    char charArr[tttboard.length()];
 
   int i=0;
   while (i < tttboard.length()) {
      charArr[i] = tttboard[i];
      i++;
   }
   for(char ch: charArr){
      cout << ch << "  ";}
    isValid(charArr);

}

int main(){

    string place;
    cin>>place;
    tttresult(place);

}
