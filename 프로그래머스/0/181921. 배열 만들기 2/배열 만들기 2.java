import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = l; i <= r; i++) {
            String s = "" + i;
            if (s.replace("0", "").replace("5", "").equals("")) {
                list.add(i);
            }
        }

        if (list.isEmpty()) {
            return new int[]{-1};
        }

        int[] answer = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}