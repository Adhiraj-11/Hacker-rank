#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;


int main() {
    int c ;
    string a;
    vector<int> b;
    char ch;
    cin >> a;
    
    stringstream ss;
    ss << a;
    
    while (ss >> c){
        b.push_back(c);
        ss >> ch;
    }
    for(int i = 0; i < b.size(); i++){
        cout << b[i] << endl;
    }
    

    return 0;
}
