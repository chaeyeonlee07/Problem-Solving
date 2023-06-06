#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>

using namespace std;

int main(void) { 
 
    int n; cin >> n; 
 
    stack<int> S;   
    while (n--) { 
        string input; 
        cin >> input ;
 
        if (input == "push") { 
            int n ; cin >> n; 
            S.push(n);
        }
        else if (input == "top") { 
            if (S.empty()) cout << -1 << endl;
            else cout << S.top() << endl; 
        }
        else if (input == "size") { 
            cout << S.size() << endl;
        }
        else if (input  == "empty") { 
            if (S.empty()) {cout << 1 << endl;}
            else {cout << 0 << endl;}
        }
        else if (input == "pop") { 
            if (S.empty()) cout << -1 << endl; 
            else { 
            cout << S.top()  << endl; 
            S.pop(); 
            }
         }

    }
}