#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>

using namespace std; 
stack<int> S; 
string ans;
int main(void) { 
    int n; cin >> n;
    int curr; 
    curr = 1; 
    while (n--) {
        int a; cin >> a;
        while (curr <= a) { 
       
            S.push(curr); 
            curr ++; 
            ans += "+\n";
        }
        
        if (S.top() == a) { 
             
            S.pop();
            ans += "-\n";
        }
        else if( S.top() != a) {
            cout << "NO" << endl; 
            return 0; 
        }
    }
    cout << ans;
}
     
