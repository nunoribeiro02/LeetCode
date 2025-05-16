/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        return DFS(root1, new ArrayList<>()).equals(DFS(root2, new ArrayList<>()));
    }

    public ArrayList<Integer> DFS(TreeNode t, ArrayList<Integer> al){
        if(t == null) return al;
        
        if(t.left == null && t.right == null) al.add(t.val);
        
        al = DFS(t.left, al);
        al = DFS(t.right, al);
        
        return al;
    }
}
