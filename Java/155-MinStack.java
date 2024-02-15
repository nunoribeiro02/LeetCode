import java.util.*;

class MinStack {

    private List<Integer> stack = new ArrayList<Integer>();
    private List<Integer> minStack = new ArrayList<Integer>();

    public MinStack() {
    }
    
    public void push(int val) {
        stack.add(val);
        
        if (minStack.size() == 0 || val < minStack.get(minStack.size() -1)){
            minStack.add(val);
        }
        else{
            minStack.add(minStack.get(minStack.size() -1));           
        }

    }
    
    public void pop() {
        if (stack.size() > 0){
            int index = stack.size() -1;
            stack.remove(index);
            minStack.remove(index);
        }
    }
    
    public int top() {
        return stack.get(stack.size() -1);
    }
    
    public int getMin() {
        return minStack.get(minStack.size() -1);
    }
}

/**
Space: O(n), grows linearly with the inputs
Time: O(1)
 */
