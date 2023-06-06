#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>

using namespace std;

stack<int> S;  
int total = 0;  
int main(void) { 
    int K; cin >> K; 
     
     
    while (K--) {
        int input; cin >> input; 
        if (input == 0) {
            int x = S.top(); 
            S.pop(); 
            total -= x; 
        }
        else {
            total += input; 
            S.push(input); 
        }
    }
    cout << total << '\n'; 
}