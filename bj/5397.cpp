#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main() { 
    ios::sync_with_stdio(0); 
    cin.tie(0);
    int n ; cin >> n; 
    while (n--) {
        string init; 
        cin >> init; 
        list<char> L;  
        auto cursor = L.begin();
        for (char c: init) {
            if (c == '<') { 
                if (cursor != L.begin()) {
                    cursor --; 
                }
            }
            else if (c == '>') { 
                if (cursor != L.end()) {
                    cursor ++; 
                }
            }
            else if (c == '-') { 
                if (cursor != L.begin()){
                    cursor --; // 커서의 앞 문자를 지워야 하기 때문에. 
                    cursor = L.erase(cursor);
             
                }
            }
            else { 
                L.insert(cursor, c); 
            }
        }
        for (char c: L) { cout << c;}
        cout << endl;

        
    }

} 
