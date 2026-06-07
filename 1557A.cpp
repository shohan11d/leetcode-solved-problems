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
    long long sum = 0;
    vector<int> v(n);
    for (auto &x : v) {
      cin >> x;
    }
    sort(v.begin(), v.end(), greater<int>());

    for (int i = 1; i < n; i++) {
      sum += v[i];
    }

    double avg = v[0] + (sum / (double)(n - 1));
    cout << fixed << setprecision(9) << avg << "\n";
  }

  return 0;
}