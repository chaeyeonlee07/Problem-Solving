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
int n; 
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1 ,1}; 
char graph[1002][1002];
int fire[1002][1002]; 
int person[1002][1002];  

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;  
    while (n--) {
        int w, h; 
        bool escape = false; 
        cin >> w >> h; 
         
        queue<pair<int,int> > fire_queue;   
        queue<pair<int,int> > person_queue;    
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {  
                cin >> graph[i][j]; 
                person[i][j] = 0 ; 
                fire[i][j] = 0; 
                if (graph[i][j] == '@') { 
                    person_queue.push({i,j});
                    person[i][j] = 1; }
                if (graph[i][j] == '*') { 
                    fire_queue.push({i,j});
                    fire[i][j] = 1;
                }
            } 
        

        while (!fire_queue.empty()) {
            pair<int, int> curr = fire_queue.front(); 
            fire_queue.pop() ; 
            for (int i = 0; i < 4; i++) {
                int nx = curr.first + dx[i] ; 
                int ny = curr.second + dy[i] ; 
                if (nx < 0 || nx >= w || ny >= h || ny < 0) {continue;}
                if (graph[nx][ny] == '#') {continue;}
                if (fire[nx][ny]) {continue; } 
                fire[nx][ny] = fire[curr.first][curr.second] + 1;
                fire_queue.push({nx, ny});
            }
        }
        while (!person_queue.empty() && !escape) {
            pair<int, int> curr = person_queue.front(); 
            person_queue.pop() ; 
 
            for (int i = 0; i < 4; i++) {
                int nx = curr.first + dx[i] ; 
                int ny = curr.second + dy[i] ; 
                if (nx < 0 || nx >= w || ny >= h || ny < 0) {   
                    cout << "hey" << person[nx][ny] << '\n';
                    escape = true; 
                    break;
                }
                if (graph[nx][ny] == '#') {continue;}
                if (person[nx][ny] !=0) continue;
    
                if (fire[nx][ny] != 0 && fire[nx][ny] <= person[curr.first][curr.second] + 1) {continue;}
                    
                person[nx][ny] = person[curr.first][curr.second] + 1; 
                person_queue.push({nx, ny}); 
            }
        }
        if (!escape) {cout << "IMPOSSIBLE" << endl; break; } 
    }
}
}
