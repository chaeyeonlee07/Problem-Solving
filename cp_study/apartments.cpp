#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;   

 
int main() { 
    int n; // number of applicants
    int m; // number of apartments
    int k; // maximum allowed difference 
    cin >> n; 
    cin >> m; 
    cin >> k; 

    vector<int> desired(n);  
    for (int i = 0; i < n; i++) cin >> desired[i];  
    vector<int> apartments(m);   
    for (int i = 0; i < m; i++) cin >> apartments[i];   

    sort(desired.begin(), desired.end()); 
    sort(apartments.begin(), apartments.end()); 
    int count = 0 ; 
    int smallest_desired = 0; 
    int smallest_available = 0; 

    while (smallest_desired < n && smallest_available < m) { 
        if (abs(desired[smallest_desired] - apartments[smallest_available]) <= k) {
            count += 1; 
            smallest_desired += 1; 
            smallest_available += 1; 
        }
        // what is available is so much smaller than what is desired --> incldue what is smallest available
        else if (apartments[smallest_available] + k < desired[smallest_desired]) { 
            smallest_available += 1; 
        }
        // available smallest apartment is larger than what is desired smallest --> desire += 1 
        else if (apartments[smallest_available] > desired[smallest_desired] + k) {
            smallest_desired += 1; 
        }
    } 
    cout << count << endl; 
}
 