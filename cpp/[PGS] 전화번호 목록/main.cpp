#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());
    
    for (int i = 0; i < phone_book.size() - 1; ++i) {
        const string& current = phone_book[i];
        const string& next = phone_book[i + 1];

        if (next.compare(0, current.size(), current) == 0) {
            return false;
        }
    }
    return true;
}

// sorting을 해두면 어떤 번호가 다른 번호의 접두어인 경우는 항상 인접해 있음
// 1차원 벡터에서 인접한 노드만 비교