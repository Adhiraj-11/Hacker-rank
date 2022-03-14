#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;


int main() {
    
    
    int i, T,N, K, z;
    vector<int> v;
    vector<vector<int>> p;
    vector<int> q;
    
    cin >> T;
    cin >> N >> K;
    
    for(i = 0; i < N; i++){
        cin >> z;
        v.push_back(z);
        cout << v[i] << " ";
       
    }
     for(i = 0; i< N-1; i++){
        q.push_back(v[i]);
        if(q.size() == K){
            p.push_back(q);
            q.clear();
            q.push_back(v[i]);
        }
            
    }
    for(i = 0; i < p.size(); i++){
        for(int j = 0; j< p[i].size(); j++){
            cout << p[i][j] << " ";
        }
    
    }
    return 0;
}
