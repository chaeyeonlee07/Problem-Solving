#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int count = 0;
    string input;
    for (int i = 0; i < 8; i++) {
        cin >> input;
        int len = input.length();
        for (int j = 0; j < len; j++) {
            if ((i + j) % 2 == 0) {
                if (input[j] == 'F') {
                    count++;
                }
            }
        }
    }
    cout << count << endl;
}
