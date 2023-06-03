#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <ios>
#include <cstdio>
#include <utility>
#include <queue>
using namespace std; 
int n, m; 
int days = 0; 
int graph[1002][1002]; 
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1 ,1};   
queue<pair<int,int> > Q; 
int totalTomato = 0; 
int curRipen = 0; 
 
int main() { 
    cin >> n >> m; 
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j++) {
            int a; 
            cin >> a; 
            if (a == 1) {
                Q.push({i, j}); 
                totalTomato ++;
                curRipen ++; 
            }
            else if (a == 0) {totalTomato ++;}
            graph[i][j] = a; 
            
        }
    }
    if (curRipen == totalTomato) {
        cout << 0 << endl;
        return;
    }
    while (!Q.empty()) {
        pair<int,int> cur = Q.front(); 
        Q.pop(); 
        int count = 0; 
        for (int i = 0; i < 4; i ++) { 
            
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i]; 
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) {continue;}
            if (graph[nx][ny] != 0) {continue;}
            if (graph[nx][ny] == 0) {Q.push({nx,ny}); 
            count ++;
            curRipen ++;}
            
        }
        if (count > 0) { days ++; }

    }
    if (curRipen < totalTomato) { 
        cout << -1 << endl;
    }
    else if (curRipen == totalTomato) {
        cout << days << endl;
    }

}