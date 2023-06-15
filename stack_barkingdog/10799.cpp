#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <string> 

using namespace std;  
string sent;
stack<char> S; 
int fragments = 0 ; 
int main(void) { 
    ios::sync_with_stdio(0);
    cin.tie(0); 
      
 
    cin >> sent; 
 
    for (int i = 0; i < sent.length(); i++) {
        if (sent[i] == '(') { 
            S.push(sent[i]);
        }
        else { 
            if (sent[i-1] == '(') { S.pop(); fragments += S.size() ; } 
            else {S.pop();fragments += 1; }

    }
    }
    cout << fragments << "\n"; 
    return 0; 
}
