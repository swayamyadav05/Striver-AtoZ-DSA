#include<bits/stdc++.h>
using namespace std;

int main() {
    string s = "Swayam";
    int len = s.size();
    s[len - 1] = 'z';
    cout << s[len - 1];
    return 0;
}