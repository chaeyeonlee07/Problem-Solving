#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;  
 
int main() { 
    int n; // number of children
    int x; // maximum allowed weight 
    cin >> n; 
    cin >> x; 
    vector<int> weights(n); 
    for (int i = 0; i < n; i++) cin >> weights[i];     
    int left; 
    int right; 
    int count; 

    left = 0; 
    right = n - 1; 
    count = 0;  
    sort(weights.begin(), weights.end()); 
    while (left <= right) { 
        if (weights[left] + weights[right] <= x) { 
            count += 1; 
            left += 1; 
            right -= 1; 
        }
        // Remember that you need to decrease right by 1 everytime if the current sum of weights[left] + weights[right] is greater than x/
        // Simultaneously, we need to increase count by 1.  
        else { 
            right -= 1; 
            count += 1; 
        }
     
    }
    cout << count << endl;
}


