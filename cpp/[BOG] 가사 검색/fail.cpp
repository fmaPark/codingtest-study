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

    TRIE *trie = new TRIE();
    TRIE *reverse_trie = new TRIE();
    
    for (const string &word : words) {
        trie->insert((char *)word.c_str());
        string rev = word;
        reverse(rev.begin(), rev.end());
        reverse_trie->insert((char*)rev.c_str());
    }
    
    vector<int> answer;
    
    for (const string &query : queries) {
        if (query.front() == '?') {
            string rev = query;
            reverse(rev.begin(), rev.end());
            answer.push_back(reverse_trie->find((char *)rev.c_str()));
            
            cout << "query" << query << endl;
            cout << "cnt" << reverse_trie->find((char *)rev.c_str()) << endl;
        } else if (query.back() == '?') {
            answer.push_back(trie->find((char *)query.c_str()));
            
            cout << "query" << query << endl;
            cout << "cnt" << trie->find((char *)query.c_str()) << endl;
        } else {
            answer.push_back(trie->find((char *)query.c_str()));
            
            cout << "query" << query << endl;
            cout << "cnt" << trie->find((char *)query.c_str()) << endl;
        }
    }
    return answer;
}


// 입력값 〉	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]
// 기댓값 〉	[3, 2, 4, 1, 0]
// 실행 결과 〉	실행한 결괏값 [4,2,5,4,0]이 기댓값 [3,2,4,1,0]과 다릅니다.

// 길이가 다른 것들도 개수에 포함되어 과다 누적