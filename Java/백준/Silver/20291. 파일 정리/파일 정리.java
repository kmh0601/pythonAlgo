import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> result = new HashMap<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(),".");
            st.nextToken();
            String s = st.nextToken();
            
            if (result.containsKey(s)) {
                result.replace(s, result.get(s) + 1);
            } else {
                result.put(s, 1);
            }
        }

        List<String> keySet = new ArrayList<>(result.keySet());
        Collections.sort(keySet);

        for (String key : keySet) {
            System.out.println(key + " " + result.get(key));
        }
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}