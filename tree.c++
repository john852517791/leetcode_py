#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct TreeNode {
    char val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(char c) : val(c), left(NULL), right(NULL) {}
};

TreeNode* constructTree(const vector<char>& nodes) {
    if (nodes.empty())
        return NULL;

    vector<TreeNode*> treeNodes(nodes.size());
    for (int i = 0; i < nodes.size(); ++i) {
        if (nodes[i] != ' ')
            treeNodes[i] = new TreeNode(nodes[i]);
    }

    for (int i = 0; i < treeNodes.size(); ++i) {
        if (treeNodes[i]) {
            int leftIdx = 2 * i + 1;
            int rightIdx = 2 * i + 2;
            if (leftIdx < treeNodes.size())
                treeNodes[i]->left = treeNodes[leftIdx];
            if (rightIdx < treeNodes.size())
                treeNodes[i]->right = treeNodes[rightIdx];
        }
    }

    return treeNodes[0];
}

string smallestFromLeaf(TreeNode* root) {
    if (!root)
        return "";

    string left = smallestFromLeaf(root->left);
    string right = smallestFromLeaf(root->right);

    if (left.empty() && right.empty())
        return string(1, root->val);
    else if (left.empty())
        return right + root->val;
    else if (right.empty())
        return left + root->val;

    return (left < right) ? left + root->val : right + root->val;
}

int main() {
    vector<char> nodes = {'d', 'b', 'a', ' ', 'c', 'b', 'c'};
    TreeNode* root = constructTree(nodes);
    string result = smallestFromLeaf(root);
    cout << "Output: " << result << endl;
    return 0;
}