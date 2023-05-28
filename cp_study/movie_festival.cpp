#include <queue>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;  
int main() {  
    int n; 
    int a; 
    int b; 
    int currEnd;
    int end; 
    int this_end; 
    int count; 
    cin >> n;
    map<int, int> times; 
    priority_queue<int, vector<int>, greater<int> > start; 
    // store the pairs of starting and ending time
    for (int k = 0; k < n; k++) { 
        cin >> a; 
        cin >> b; 
        if (!times.count(a) || (times.count(a) && times[a] > b)) { 
            times[a] = b; 
        }
        start.push(a); 
    } 
    currEnd = 0; 
    count = 0;
    for (int j = 0; j < n; j++) {
        this_end = start.top(); 
        start.pop();
        end = times[this_end];  
        if (currEnd == 0) {
            currEnd = end; 
            count ++;     
        }
        else {
            if (currEnd <= this_end) {
                count ++; 
                currEnd = end;
            }
            else if (currEnd > end) {
                currEnd = end; 
            }
        }
    }
    cout << count << endl; 
}


