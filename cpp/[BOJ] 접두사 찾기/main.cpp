#include <iostream>
#include <list>
#include <string>

using namespace std;

struct TRIE {
    TRIE *Node[26];
    
    TRIE() { 
        for (int i=0; i < 26; i++) Node[i] = NULL;
    }

    void insert(const char *str) {
        if (*str == '\0') {
            return;
        }

        int cur = *str - 'a';
        if (Node[cur] == NULL) Node[cur] = new TRIE(); 
        Node[cur]->insert(str + 1); 
    }
    
    int find(const char *str) {
        if (*str == '\0') {
            return true;
        }

        int cur = *str - 'a';
        if (Node[cur] == NULL) return false;
        return Node[cur]->find(str + 1);
    }
    
};

int main(void) {
    int n;
    int m;
    list<string> s;
    list<string> t;

    // reigon input
    cin >> n >> m;

    string input;

    for (int i = 0; i < n; i++) {
        cin >> input;
        s.push_back(input);
    }

    for (int i = 0; i < m; i++) {
        cin >> input;
        t.push_back(input);
    }
    // endreigon input

    TRIE trie;

    for (const string &s_str: s) {
        trie.insert(&s_str[0]);
    }

    int cnt;

    for (const string &t_str: t) {
        bool is_find = trie.find(&t_str[0]);
        if (is_find) {
            cnt++;
        }
    }

    cout << cnt << endl;

    return 0;
}


// TRIE
// s 전체를 TRIE로 저장
// t를 TRIE 구조에서 서치