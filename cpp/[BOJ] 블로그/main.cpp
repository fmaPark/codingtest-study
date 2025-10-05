#include <iostream>
#include <vector>

using namespace std;

int main() {
    // reigon input
    int N, X;
    cin >> N >> X;

    vector<int> numArr(N);
    for (int i = 0; i < N; ++i) {
        cin >> numArr[i];
    }
    // endreigon input

    int cur = 0;
    int max = 0;
    int cnt = 0;

    for (int i = 0; i <= N - X + 1; i++) {
        if (i == 0) {
            for (int j = 0; j < X; j++) {
                cur += numArr[j];
            }
            max = cur;
            cnt = 1;
        } else {
            cur = cur - numArr[i - 1] + numArr[i + X - 1];
            if (cur == max) {
                cnt++;
            } else if (cur > max) {
                max = cur;
                cnt = 1;
            }
        }
    }

    if (max == 0) {
        cout << "SAD" << endl;
    } else {
        cout << max << '\n' << cnt << endl;
    }

    return 0;
}