
#include <bits/stdc++.h>
using namespace std;

int main() {
    
    long long int l, q;
    cin >> l >> q;

    vector<vector<long long int>> qry(q, vector<long long int>(2));
    int c;
    int x;
    for (int i = 0; i < q; ++i) {
        cin >> c >> x;
        qry.at(i).at(0) = c;
        qry.at(i).at(1) = x;
        } 
    
    set<long long int> st = {0,l};
    
    for (int i = 0; i < q; ++i) {
        if (qry.at(i).at(0) == 1) {
            st.insert(qry.at(i).at(1));
            }
        else {
            auto it = st.lower_bound(qry.at(i).at(1));
            cout << *it - *prev(it) << endl;
            }
        }
    }
