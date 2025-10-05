#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string input;
    cin >> input;

    string cir_input = input + input;

    int window_len = count(input.begin(), input.end(), 'a');

    int cur_a_in_window = 0;
    int max_a_in_window = 0;
    
    for (int i = 0; i < window_len; ++i) {
        if (cir_input[i] == 'a') cur_a_in_window++;
    }
    max_a_in_window = cur_a_in_window;

    for (int i = 1; i <= input.length(); ++i) {
        if (cir_input[i - 1] == 'a') cur_a_in_window--;
        if (cir_input[i + window_len - 1] == 'a') cur_a_in_window++;
        max_a_in_window = max(max_a_in_window, cur_a_in_window);
    }

    cout << window_len - max_a_in_window << endl;
    
    return 0;
}