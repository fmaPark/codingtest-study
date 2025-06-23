#include <iostream>
#include <list>
using namespace std;

int main(void) {
    int t;
    cin >> t;

    while (t--) {
        string input;
        cin >> input;

        list<char> pwd;
        list<char>::iterator cur = pwd.begin();

        for (char c: input) {
            if (c == '<') {
                if (cur != pwd.begin()) {
                    cur--;
                }
            } else if (c == '>') {
                if (cur != pwd.end()) {
                    cur++;
                }
            } else if (c == '-') {
                if (cur != pwd.begin()) {
                    cur--;
                    cur = pwd.erase(cur);
                }
            } else {
                cur = pwd.insert(cur, c);
                cur++;
            }
        }

        for (char c: pwd) {
            cout << c;
        }
        cout << '\n';
    }
    

    return 0;
}

// iterator 커서 선언해서 입력 그대로 적용