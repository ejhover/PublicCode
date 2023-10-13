import java.util.Scanner;

public class Fib {
    public static int fibonacciRecursive(int n) {
        if (n==0 || n==1)
            return n;
        else return fibonacciRecursive(n-1)+fibonacciRecursive(n-2);
    }
    public static int fibonacciIterative(int n) {
        int result=0,temp=1,temp2;
        if (n==0 || n==1)
            return n;
        for (int i=0;i<n;i++) {
            temp2=result;
            result=temp;
            temp=temp+temp2;
        }
        return result;
    }
    public static void main(String args[]) {
        System.out.println("Enter an integer n to get the n'th Fibonacci number:");
        Scanner myScanner = new Scanner(System.in);
        int n = myScanner.nextInt(); // gets an integer from command line
        System.out.println("The " + n + "'th Fibonacci number using fibonacciRecursive is " + fibonacciRecursive(n));
        System.out.println("The " + n + "'th Fibonacci number using fibonacciIterative is " + fibonacciIterative(n));
        }
}
