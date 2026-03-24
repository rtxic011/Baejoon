import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        char[] result = new char[a.length()];

        for (int i = 0; i < a.length(); i++) {
            char ch = a.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                result[i] = (char)(ch - 32); 
            }
            else {
                result[i] = (char)(ch + 32);
            }
        }

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
        }
    }
}