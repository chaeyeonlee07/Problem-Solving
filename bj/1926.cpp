#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iterator>
#include <list>
#include <queue>

using namespace std;

int main() {
    int vertices;
    int edges; 
    int start; 
    // map<int, int> dict; 
    // vector<int>;
    // queue<int>;


    cin >> vertices >> edges >> start; 
    vector<vector<int> > dict; 
    int con1;
    int con2; 
    for (int i = 0 ; i < edges; i++) {
        cin >> con1 >> con2; 
        dict[con1].push_back(con2);
        dict[con2].push_back(con1);
    }
    queue<int> dfs;
    vector<bool> visited; 
    vector<int> dfs_ret; 
    int vis_size = visited.size();
    dfs_ret.push_back(start);
    visited[start] = true
    list<int>::iterator myitr;
    for (myitr = dict[begin].begin(); myitr = dict[begin].end(); ++myitr) {
        
    }

        
    }

    dict[start]
}