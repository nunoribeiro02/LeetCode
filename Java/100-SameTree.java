class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null || q == null){
            return p == null && q== null; 
        }
        
        if (p.val == q.val){
            return true & isSameTree(p.left, q.left) & isSameTree(p.right, q.right);
        }
        else{
            return false;
        }
    }
}

/*
 Space: O(1)
 Time: O(n), n is the size biggeest tree
*/
