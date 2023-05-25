#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std; 

// Method 1 (O(n^3))

// int main(){ 
// int best = 0; 

// int arr[8] = {-1, 2, 4, -3, 5, 2, -5, 2};
// int lenArray = end(arr)-begin(arr); 
// for (int start = 0; start < lenArray; start++ ) {
//     for (int end = start; end < lenArray; end++) {
//         int sum = 0; 
//         for (int j = start; j <= end ; j++ ) {
//             sum += arr[j];
//         }
//         best = max(best, sum);
//     }
// }
// cout << best << endl; 
// }


// Method 2 (O(n^2))

// int main(){ 
// int best = 0; 

// int arr[8] = {-1, 2, 4, -3, 5, 2, -5, 2};
// int lenArray = end(arr)-begin(arr); 
 

// for (int start = 0; start < lenArray; start++ ) {
//     int sum = 0;  
//     for (int end = start; end < lenArray; end++) {
//         sum += arr[end];
//         best = max(best, sum);
//     }
// }
// cout << best << endl; 
// }

// Method 3 (O(n^3))
// 
int main() {
    int sum = 0; int maximum = 0; 
    int arr[8] = {-1, 2, 4, -3, 5, 2, -5, 2}; 
    int lenArray = end(arr) - begin(arr); 
    for (int start = 0; start < lenArray; start++) {
        sum = max(sum + arr[start], arr[start]);
        maximum = max(sum, maximum);
    }
    cout << maximum << endl; 

}