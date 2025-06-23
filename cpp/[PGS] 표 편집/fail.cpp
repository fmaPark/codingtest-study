#include <string>
#include <vector>
#include <iostream>
#include <list>

using namespace std;

string solution(int n, int k, vector<string> cmd) {
    
    list<int> table;
    for (int i=0; i < n; i++) {
        table.push_back(i);
    }
    
    list<int>::iterator cursor = table.begin();
    for (int i=0; i < k; i++) {
        cursor++;
    }
    
    list<pair<int, list<int>::iterator>> deleted_rows;
    
    for (const auto& c : cmd) {
        if (c.substr(0, 1) == "U") {
            int x = stoi(c.substr(1));
            for (int i=0; i < x; i++) {
                cursor--;
            }
        } else if (c.substr(0, 1) == "D") {
            int x = stoi(c.substr(1));
            for (int i=0; i < x; i++) {
                cursor++;
            }
        } else if (c == "C") {
            deleted_rows.push_back({*cursor, next(cursor)});
            cursor = table.erase(cursor);
            if (cursor == table.end()) {
                cursor--;
            }
        } else if (c == "Z") {
            if (!deleted_rows.empty()) {
                pair<int, list<int>::iterator> last_deleted_row = deleted_rows.back();
                deleted_rows.pop_back();
                
                table.insert(last_deleted_row.second, last_deleted_row.first);
            }
        }
    }
    
    string answer(n, 'X');

    for (int idx : table) {
        answer[idx] = 'O';
    }
    
    
    return answer;
}


// 채점 결과
// 정확성: 28.0
// 효율성: 42.0
// 합계: 70.0 / 100.0