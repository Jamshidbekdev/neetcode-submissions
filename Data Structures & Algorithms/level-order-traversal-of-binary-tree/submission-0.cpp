/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;

        queue<TreeNode*> data;
        data.push(root);

        while(!data.empty()) {
            vector<int> level;

            for (int i = data.size(); i > 0; i--) {
                TreeNode* node = data.front();
                data.pop();

                if (node) {
                    level.push_back(node->val);
                    data.push(node->left);
                    data.push(node->right);
                }
            }

            if(!level.empty()) {
                result.push_back(level);
            }
        }

        return result;
    }
};
