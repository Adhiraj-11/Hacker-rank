#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int main() {
    int Q, y, z;
    string a, x;

    cin >> Q;
    
    map<string, int> m;
    for(int j = 0; j < Q; j++){
        cin >> z;
        
        if(z == 1){
            cin >> x >> y;
            if(m.find(x) == m.end()){
            m.insert({x, y});
            }else{
                m[x] += y;
            }
        }else if(z == 2){
            cin >> a;
            m.erase(a);
        }else{
            cin >> a;
            cout << m[a] << endl;
        }
    }
    
    return 0;
}