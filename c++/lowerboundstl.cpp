#include <iostream>
#include <vector>
#include <sstream>
using namespace std;


int main() {
    int b,c,x;
    vector<int> v;
    string a;
    int num;
    cin >> x;
    for(int j = 0; j < x; j++){
        cin >> num;
        v.push_back(num);
    }
    int n, val;
   cin >> n;
   for (int i=0; i<n; i++){
       cin >> val;
       auto it = lower_bound(v.begin(), v.end(), val);
       if (val != *it){

       
           cout << "No " << (it - v.begin()+1) << endl;
       }else
           cout << "Yes " << (it - v.begin()+1) << endl;
    }
    
    

    
    
    return 0;
    
}






    
    
