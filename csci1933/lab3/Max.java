import java.util.Scanner;
public class Max {
    public static int recursiveMaxDigit(int num){
        if ((num/10)<1)
            return num;
        return Math.max(num%10, recursiveMaxDigit(num/10));
    }
    public static int iterativeMaxDigit(int num) {
        int ans = 0;
        for (int i=0;i<String.valueOf(num).length();i++) {
            if ((num%10)>ans){
                ans=num%10;
            }
            num=num/10;
        }
        return ans;
    }
    public static void main(String args[]) {
        System.out.println("Enter an integer n to get the max digit:");
        Scanner myScanner = new Scanner(System.in);
        int n = myScanner.nextInt(); // gets an integer from command line
        System.out.println("Recursive Sol: " + recursiveMaxDigit(n));
        System.out.println("Iterative Sol: " + iterativeMaxDigit(n));
        }  
}
