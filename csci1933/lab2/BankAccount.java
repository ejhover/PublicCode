import java.util.Scanner;

public class BankAccount {
    private String name;
    private String password;
    private double balance;
    public BankAccount(String initName, String initPass, double initBalance) {
        this.name = initName;
        this.password = initPass;
        this.balance = initBalance;
        }
    public void withdraw(String enteredPassword, double amount) {
        // Only people with the right password and sufficient funds can withdraw
        if (password.equals(enteredPassword) && balance >= amount) {
            balance = balance - amount;
        }
    }
    public void deposit(String enteredPassword, double amount) {
        if (password.equals(enteredPassword)) {
            balance = balance + amount;
        }
    }
    public double getBalance(String enteredPassword) {
        if (password.equals(enteredPassword)) {
        return balance;
        } else {
        return -1;
        }
    }
    public boolean setPassword(String oldPassword, String newPassword) {
        if (password.equals(oldPassword)) {
            password = newPassword;
            return true;
        } 
        else {
            return false;
        }
    }
    public void transfer(BankAccount other, String enteredPassword, double amount) {
        if (this.password.equals(enteredPassword)) {
            Scanner passChecker = new Scanner(System.in);
            System.out.println("Enter the other account's password: ");
            String pass = passChecker.nextLine();
            passChecker.close();
            if ((other.getBalance(pass))!=-1) {
                other.deposit(pass, amount);
                this.withdraw(enteredPassword, amount);
            }
            System.out.println(this.name + "s' balance: " + this.balance);
            System.out.println(other.name + "s; balance: " + other.balance);
        }
    }

    public static void main(String[] args) {
        BankAccount Dovolis = new BankAccount("Dovolis", "Hello1234", 1000);
        BankAccount Taylor = new BankAccount("Taylor", "Hello12345", 100);
        Dovolis.transfer(Taylor, "Hello1234", 100);
    }
}