#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

struct TRIE {
    TRIE *Node[26];
    int count;
    
    TRIE() { 
        count = 0;
        for (int i=0; i < 26; i++) Node[i] = NULL;
    }

    void insert(char *str) {
        count++;
        if (*str == '\0') {
            return;
        }

        int cur = *str - 'a';
        if (Node[cur] == NULL) Node[cur] = new TRIE(); 
        Node[cur]->insert(str + 1); 
    }
    
    int find(char *str) {
        if (*str == '\0') {
            return count ? 1 : 0;
        }
        
        if (*str == '?') {
            return count;
        }

        int cur = *str - 'a';
        if (Node[cur] == NULL) return false;
        return Node[cur]->find(str + 1);
    }
};


vector<int> solution(vector<string> words, vector<string> queries) {

    // TRIE *trie = new TRIE();
    // TRIE *reverse_trie = new TRIE();
    
    vector<TRIE*> tries(10001, nullptr);
    vector<TRIE*> reverse_tries(10001, nullptr);
    
    for (const string &word : words) {
        int len = word.size();
        if (tries[len] == nullptr) {
            tries[len] = new TRIE();
        }
        if (reverse_tries[len] == nullptr) {
            reverse_tries[len] = new TRIE();
        }
        
        tries[len]->insert((char *)word.c_str());
        string rev = word;
        reverse(rev.begin(), rev.end());
        reverse_tries[len]->insert((char*)rev.c_str());
    }
    
    vector<int> answer;
    
    for (const string &query : queries) {
        int len = query.size();
        if (tries[len] == nullptr && reverse_tries[len] == nullptr) {
            answer.push_back(0);
            continue;
        }
        
        if (query.front() == '?') {
            string rev = query;
            reverse(rev.begin(), rev.end());
            answer.push_back(reverse_tries[len]->find((char *)rev.c_str()));
            
            // cout << "query" << query << endl;
            // cout << "cnt" << reverse_tries[len]->find((char *)rev.c_str()) << endl;
        } else if (query.back() == '?') {
            answer.push_back(tries[len]->find((char *)query.c_str()));
            
            // cout << "query" << query << endl;
            // cout << "cnt" << tries[len]->find((char *)query.c_str()) << endl;
        } else {
            answer.push_back(tries[len]->find((char *)query.c_str()));
            
            // cout << "query" << query << endl;
            // cout << "cnt" << tries[len]->find((char *)query.c_str()) << endl;
        }
    }
    return answer;
}

//  TRIE로 풀이
// 단, find 시 와일드카드가 있을 경우 남은 단어를 전부 카운트해서 반환
// 이때 길이가 다른 문자열도 과다 검색될 경우가 있으므로 길이별 벡터로 TRIE를 따로 저장
// 와일드카드가 앞 또는 뒤이므로 앞에 있을 경우에는 문자열을 뒤집어서 검색