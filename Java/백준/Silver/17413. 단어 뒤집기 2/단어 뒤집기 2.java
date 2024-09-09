//package week8.BJ17413;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> stack = new Stack<Character>();
        List<Character> result = new ArrayList<>();

        String s = br.readLine();

        boolean flag = false;
        for (Character c : s.toCharArray()) {
            if (c.equals('<')) {
                while (!stack.isEmpty()) {
                    result.add(stack.pop());
                }
                result.add(c);
                flag = true;
            } else if (c.equals(' ')) {
                while (!stack.isEmpty()) {
                    result.add(stack.pop());
                }
                result.add(c);
            } else if (c.equals('>')) {
                result.add(c);
                flag = false;
            } else if (flag) {
                result.add(c);
            } else {
                stack.push(c);
            }
        }

        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }

        result.forEach(System.out::print);
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}