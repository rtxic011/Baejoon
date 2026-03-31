class Solution {
    public int solution(int a, int b) {
        int ab = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int tab = 2*a*b;
        
        if (ab < tab) {
            return tab;
        } else {
            return ab;
        }
    }
}