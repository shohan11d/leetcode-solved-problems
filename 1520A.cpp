#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;

  while (t--) {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<bool> v(26, false);
    v[s[0] - 'A'] = true;
    bool ok = true;

    for (int i = 1; i < n; i++) {
      if (s[i] != s[i - 1]) {
        if (v[s[i] - 'A']) {
          ok = false;
          break;
        }
        v[s[i] - 'A'] = true;
      }
    }

    if (ok) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }

  return 0;
}