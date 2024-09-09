import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for(int i = 0; i < T; i++) {
            String s = br.readLine();

            int result = 0;
            int x = 0;
            int y = s.length() - 1;
            while (x < y && result == 0) {
                if (s.charAt(x) != s.charAt(y)) {
                    int result1 = 1;
                    int result2 = 1;
                    String s1 = s.substring(0,x) + s.substring(x+1);
                    String s2 = s.substring(0,y) + s.substring(y+1);

                    int x1 = 0;
                    int y1 = s1.length() - 1;
                    int x2 = 0;
                    int y2 = s2.length() - 1;

                    while (x1 < y1) {
                        if (s1.charAt(x1) != s1.charAt(y1)) {
                            result1 = 2;
                            break;
                        }
                        x1 += 1;
                        y1 -= 1;
                    }
                    while (x2 < y2) {
                        if (s2.charAt(x2) != s2.charAt(y2)) {
                            result2 = 2;
                            break;
                        }
                        x2 += 1;
                        y2 -= 1;
                    }
                    // System.out.println("result1:" + result1 + " " + "result2" + result2);
                    if (result1 == 1 || result2 == 1) {
                        result = 1;
                    } else {
                        result = 2;
                    }
                }
                x += 1;
                y -= 1;
            }
            System.out.println(result);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}