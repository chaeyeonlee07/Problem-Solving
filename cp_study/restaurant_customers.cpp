#include <queue>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;  

int main() {
    int n; 
    int a; int b; 
    cin >> n;
    map<int, int> times;
    priority_queue<int, vector<int>, greater<int> > start; 
    priority_queue<int> q;  
    int size; 
    int maxSize; 
  
    priority_queue<int, vector<int>, greater<int> > end; 
    // creating a map of times
    for (int i = 0; i < n ; i ++) {
        cin >> a; 
        cin >> b; 
        start.push(a);
        times[a] = b; 
    }
    size = 0; 
    maxSize = 0;  
    // creating a priority queue based on the ending time.   
    for (int k = 0; k < n; k ++) { 
        int add = start.top(); 
        end.push(times[add]);
        size += 1;  
        start.pop(); 
        while (add > end.top()) { 
            end.pop(); 
            size --; 
        }
        maxSize = max(maxSize, size); 
    }
    cout << maxSize << endl;
} 