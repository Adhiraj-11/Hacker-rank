#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int T,a,b;
    cin >> T;
    cin >> a >> b;
    int A[a][b];
    int B[a][b];
    int C[a][b];
    
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cin >> A[i][j];
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cin >> B[i][j];
        }
    }
    for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                C[i][j] = A[i][j] + B[i][j];
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cout << C[i][j];
            cout << " ";
        }
        cout << endl;
    }


    return 0;
}
