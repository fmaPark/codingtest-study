#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<vector<int>> get_points(int st_r, int st_c, int ed_r, int ed_c) {
    vector<vector<int>> result;
    int cur_r = st_r;
    int cur_c = st_c;
    
    while (true) {
        if (cur_r == ed_r && cur_c == ed_c) break;
        
        if (cur_r > ed_r) {
            cur_r--;
            result.push_back({cur_r, cur_c});
        } else if (cur_r < ed_r) {
            cur_r++;
            result.push_back({cur_r, cur_c});
        } else if (cur_c > ed_c) {
            cur_c--;
            result.push_back({cur_r, cur_c});
        } else if (cur_c < ed_c) {
            cur_c++;
            result.push_back({cur_r, cur_c});
        }
    }
    
    return result;
}

int solution(vector<vector<int>> points, vector<vector<int>> routes) {
    map<int, vector<vector<int>>> all_routes;
    
    int max_len = 0;
    int route_id = 0;
    for (const vector<int>& route : routes) {
        vector<vector<int>> temp_route;
        
        temp_route.push_back({points[route[0] - 1][0], points[route[0] - 1][1]});
        
        for (int i = 0; i < route.size() - 1; i++) {
            int from = route[i] - 1;
            int to = route[i + 1] - 1;

            vector<vector<int>> segment = get_points(
                points[from][0], points[from][1],
                points[to][0], points[to][1]
            );

            temp_route.insert(temp_route.end(), segment.begin(), segment.end());
            if (max_len < temp_route.size()) {
                max_len = temp_route.size();
            }
        }

        all_routes[route_id++] = temp_route;
        
    }

    // for (const auto& [key, path] : all_routes) {
    //     cout << key << ": ";
    //     for (const auto& p : path) {
    //         cout << "(" << p[0] << "," << p[1] << ") ";
    //     }
    //     cout << endl;
    // }
    
    // 0: (2,4) (3,4) (4,4) (5,4) (6,4) 
    // 1: (4,2) (4,3) (4,4) (4,5) (4,6) (4,7) 
    // 2: (5,4) (4,4) (3,4) (2,4) (1,4) 
    
    map<int, map<pair<int, int>, int>> column_map; //<컬럼 <<좌표>횟수>
    
    for (const auto& [route_id, path] : all_routes) {
        for (int i = 0; i < path.size(); i++) {
            pair<int, int> point = {path[i][0], path[i][1]};
            column_map[i][point]++;
        }
    }
    
    int answer = 0;
    for (const auto& [col, point_count_map]: column_map) {
        for (const auto& [point, count] : point_count_map) {
            if (count >= 2) {
                answer++;
            }
        }
    }

    return answer;
}

// 각 로봇별 모든 경로 정렬
// col(같은 시점)을 기준으로 재정렬해서 좌표 등장 횟수 카운트
// 횟수가 2회 이상이면 충돌로 간주