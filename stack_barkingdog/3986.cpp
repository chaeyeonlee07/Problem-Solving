#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <string> 

using namespace std;     

int main(void) { 
    int num; cin >> num;
    int count ; count =0 ;  
    while (num--) {
        string Str; cin >> Str; 
        stack<int> S; 
 
        for (char c : Str) {
            if (S.empty() || S.top() != c) {S.push(c);}
            else  { 
                if (S.top() == c) { 
                    S.pop();
                }
            }
        }
        if (S.empty()) {count ++;}
    }
    cout << count <<'\n' ; 
}