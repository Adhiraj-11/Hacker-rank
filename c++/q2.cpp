#include <iostream>

using namespace std;

int main() {
    int n,i;
    string aray;
    cin >> n;
    cout << "enter the numbers: ";
    getline(cin, aray);
    cout << aray << endl;
    // for(i = 0; i < n; i++){
    //     cin >> aray[i];
        
    // }
    for(i =n-1; i >= 0; --i){
        cout << aray[i];
        
    }
    
    return 0;
}
