class Solution {
public:
    bool isValid(string s) {
        stack<int> st_data;
        unordered_map <char, char> unmap = {
            { '}', '{' },
            { ']', '[' },
            { ')', '(' },
        };

        for(char c : s ) {
            if(unmap.count(c)) {
                if (!st_data.empty() && st_data.top() == unmap[c]) {
                    st_data.pop();
                } else {
                    return false;
                }
            } else {
                st_data.push(c);
            }
        }

        return st_data.empty();
    }
};
