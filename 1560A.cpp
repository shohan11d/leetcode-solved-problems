#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int k;
        cin >> k;

        int element = 0;
        int sum = 1;

        while (true) {
            if (sum % 3 != 0 && sum % 10 != 3) {
                element++;

                if (element == k) {
                    cout << sum << '\n';
                    break;
                }
            }

            sum++;
        }
    }

    return 0;
}