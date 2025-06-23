#include <iostream>

struct TRIE
{
    bool Finish; //문자열이 끝난 시점 체트
    TRIE *Node[26]; // 26칸인 이유 : 알파벳이 총 26개
    TRIE() { //생성자
        Finish = false;
        for (int i=0; i < 26; i++) Node[i] = NULL;
    }

    // 문자열 삽입
    void Insert(char *str) {
        // 문자열이 끝날 경우 체크
        if (*str == NULL) {
            Finish = true;
        }

        int cur = *str - 'A'; // 현재 문자 가져오기
        if (Node[cur] == NULL) Node[cur] = new TRIE(); // 현재 연결된 노드가 없는 경우 노드를 생성하고 다음 문자열 탐색
        Node[cur]->Insert(str + 1); // 노드를 통해 다음 문자열로 넘어가기
    }

    // 문자열 찾기
    bool Find(char *str) {
        if (*str == NULL) {
            if (Finish == true) return true;
            return false; // 노드가 생성되지 않았다면(찾고자 하는 노드가 없다면) false를 반환
        }

        int cur = *str - 'A';
        if (Node[cur] == NULL) return false;
        return Node[cur]->Find(str + 1);
    }
};
