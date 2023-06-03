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
int board[502][502]; 
int visited[502][502];
int n, m; 
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1 ,1}; 
int main() { 
    ios::sync_with_stdio(0);
    cin.tie(0); 
    for (int i = 0 ; i < n; i++) { 
        for (int j = 0; j < m; j++) {
            cin >> board[i][j] ; 
        }
    }
    int count = 0; 
    int maxSize = 0; 
    for (int i = 0 ; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visited[i][j] || board[i][j] == 0) {continue;}
            else if (!visited[i][j] && board[i][j] == 1) { 
                queue<pair<int,int> > Q;
                int area = 0; 
                visited[i][j] = 1; 
                Q.push({i,j}); 
                while (!Q.empty()) {
                    area++; // 큐에 들어있는 원소를 하나 뺄 때 마다 넓이를 1 증가시킴
                    pair<int,int> cur = Q.front(); Q.pop(); 
                    for (int dir = 0; dir < 4; dir ++) {
                        int nx = cur.first + dx[dir]; 
                        int ny = cur.second + dy[dir];
                        if (nx < 0 || nx >= n || ny >= m || ny < 0) { continue;}
                        if (visited[nx][ny]) {continue;}
                        visited[nx][ny] = 1 ; 
                        Q.push({nx, ny}); 
                    }

                }
            maxSize = max(maxSize, area);
            }
             
        }
    }
    cout << count << '\n' << maxSize;
    

}
