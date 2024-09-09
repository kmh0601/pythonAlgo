import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public void solution() throws Exception{
        String rexp = "^[A-F]?A+F+C+[A-F]?$";
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0 ; i < T ; i++) {
            String s = br.readLine();
            if (s.matches(rexp)) {
                System.out.println("Infected!");
            }
            else {
                System.out.println("Good");
            }
        }
    }

    public static void main(String[] args) throws Exception{
        new Main().solution();
    }
}
