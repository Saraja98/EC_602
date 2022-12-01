#include<iostream>
#include<string>
#include<array>
#include<vector>
#include<map>
#include movedef.h
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

//don't have to have this if I include movedef.hp
struct Move{
    int r;  //identifies row
    int c;  //identifies column
    char player; //identifies player (x or o)
};
    
  //checking to make sure the values or r, c and player are valid (need all of these conditions to be true at the same time)
    bool error(int r, int c, char player) const{
        if ((r>=0) and (r<=2))
            return true;
        else
            return false;
        if ((c>=0) and (r<=2))
            return true;
        else
            return false;
            
        if ((player = 'x') or (player = '0'))
            return true;
        else
            return false;

        
    }
    
    
    
};

char tttresult(vector<Move> board){
    
}





int main(){  //used to testing purposes
    vector<Move> board; //creates a vector called board that is part of the Move class
    bool error;//boolean variable, can only be true or false
    char result;
    Move m; //sets up data structure to hold information about the move
    //the following are samples for testing purposes
    m.r = 1;
    m.c = 1;
    m.player='x';
    board.push_back(m);  //will put info about move into the vector board
}
