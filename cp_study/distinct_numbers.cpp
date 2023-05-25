#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;  

 
int main() { 
    int n;
    cin >> n ;  

    vector<int> arr(n);  
    for (int i = 0; i < n; i++) cin >> arr[i]; 
    sort(arr.begin(), arr.end());
    int count = 1 ; 

    for (int i = 0; i < n - 1; i++) { 
        if (arr[i] != arr[i+1]) { 
            count += 1; 
        }
    }
    cout << count << endl; 
}


     