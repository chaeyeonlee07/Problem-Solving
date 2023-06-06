#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <string> 

using namespace std;  

int n; 
stack<pair<int, int>> tower; 
 
int main(void) { 
    cin >> n; 
    tower.push({1000000001, 0}); 
    for (int i = 1; i <= n ; i++) {
        int height; cin >> height; 
        while (tower.top().first < height) { 
            tower.pop(); 
        } 
        cout << tower.top().second << " "; 
        tower.push({height, i}); 
        }
 
}