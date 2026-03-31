class Solution {
    public int solution(int n) {
        int r = 0;
        
        if (n%2==0) {
            for (int i = 1; i <= n; i++) {
                if (i%2==0) {
                    r += i*i;
                }
            }
        } else {
            for (int i = 1; i <= n; i++) {
                if (i%2!=0) {
                    r += i;
                }
            }
        }
        return r;
    }
}