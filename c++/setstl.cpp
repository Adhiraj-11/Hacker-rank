#include <iostream>
#include <set>

using namespace std;

int main() {
    int q, i,x,y;
    set<int> s;
    
    cin >> q;
    
    for(i =0; i < q; i++){
        cin >> x >> y;
        if(x == 1){
            s.insert(y);
        }else if(x == 2){
            s.erase(y);
        }else if(x == 3){
            
            set<int>::iterator itr=s.find(y);
            if(itr == s.end()){
                cout << "No" << endl;
            }else{
                cout << "Yes" << endl;
            }

        
        }
        
        
            
            
        }
        

}


