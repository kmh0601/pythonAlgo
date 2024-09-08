import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, Boolean> noSeeAndHearMan = new HashMap<>();
        List<String> result = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            noSeeAndHearMan.put(br.readLine(), true);
        }
        for (int j = 0 ; j < M ; j++) {
            String temp = br.readLine();
            if (noSeeAndHearMan.get(temp) != null){
                result.add(temp);
            }
        }

        Collections.sort(result);

        System.out.println(result.size());

        for (String s : result) {
            System.out.println(s);
        }

    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}