import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;

class a{
    public static void main(String[] args) {
        HashMap<Integer,Integer> data = new HashMap<>();
        list add = new list();
        ArrayList<Integer> a = new ArrayList();
        a.add(1);
        System.out.println(a);
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(3);
        System.out.print(stack.peek());

    }
}

class list{
    private int add(int a, int b){
        return a+b;
    }
    private int sub(int a, int b){
        return a-b;
    }
}