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
int graph[101][101]; 
int dist[101][101]; 
int n, m;  
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1 ,1};  
int main() { 
    ios::sync_with_stdio(0);
    cin.tie(0);  
    cin >> n >> m ; 
    for (int i = 0; i < n ; i++) { 
        for (int j = 0 ; j < m; j++) {
            cin >> graph[i][j]; 
        }
    }
    queue<pair<int,int> > Q;
    Q.push({0,0});
    fill(&dist[0][0], &dist[n][m], -1); 
    dist[0][0] = 0;
    while (!Q.empty()) { 
        pair<int,int> cur = Q.front(); Q.pop();
         
        for(int dir = 0; dir < 4; dir++){ // 상하좌우 칸을 살펴볼 것이다.
          int nx = cur.first + dx[dir];
          int ny = cur.second + dy[dir]; // nx, ny에 dir에서 정한 방향의 인접한 칸의 좌표가 들어감
          if(nx < 0 || nx >= n || ny < 0 || ny >= m) {continue;} // 범위 밖일 경우 넘어감
          else if(dist[nx][ny] > 0 || graph[nx][ny] != 1) {continue;}
          else {dist[nx][ny] = dist[cur.first][cur.second] + 1;}
        }
    }
    cout << dist[n-1][m-1];
}
 