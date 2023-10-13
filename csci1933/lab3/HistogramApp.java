import java.util.Scanner;
public class HistogramApp {
    public static void main(String[] args){
        System.out.println("Please only use the indicated commands.\nadd - used to add nums\nprint - prints current histogram\nquit - leaves the program");
        Scanner scan = new Scanner(System.in);
        System.out.println("Please enter your lowerbound: ");
        int lower = scan.nextInt();
        System.out.println("Please enter your lowerbound: ");
        int upper = scan.nextInt();
        Histogram hist = new Histogram(lower, upper);
        while (true){
            String input = scan.nextLine();
            if (input.equals("add")){
                System.out.println("What number would you like to add? ");
                hist.add(scan.nextInt());
                scan.nextLine();
            }
            else if (input.equals("print")){
                System.out.println(hist);
            }
            else if (input.equals("quit")){
                return;
            }
            else {
                System.out.println("Please only use the indicated commands.\nadd - used to add nums\nprint - prints current histogram\nquit - leaves the program");
            }
        }
    }
}
