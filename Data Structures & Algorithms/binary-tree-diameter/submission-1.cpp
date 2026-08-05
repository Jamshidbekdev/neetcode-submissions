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
    int result = 0;
    int heightOfTreeNode(TreeNode* root) {
        if (!root) return 0;

        int left = heightOfTreeNode(root->left);
        int right = heightOfTreeNode(root->right);

        result = max(result, (left + right));

        return 1 + max(left, right);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0;

        heightOfTreeNode(root);

        return result;
    }
};
