import java.util.Scanner;
import java.io.*;
public class BookshelfReader {
    public static Bookshelf readBooksFromFile(String fileName){
        Bookshelf newShelf = new Bookshelf(20);
        String[] bookInfo = new String[3];
        // assume our filename is stored in the string fileName
        Scanner s = null; // declare s outside try-catch block
        try {
            s = new Scanner(new File(fileName));
        } catch (Exception e) { // returns false if fails to find fileName
            System.out.println("Error");
            return new Bookshelf();
        }
        while(s.hasNextLine()) {
            bookInfo = s.nextLine().split(",");
            newShelf.add(new Book(bookInfo[0], bookInfo[1], Double.parseDouble(bookInfo[2])));
        }
        return newShelf;
// Now use s in the same way we used Scanners previously for user input
    }
    public static void writeShelfToFile(Bookshelf b, String fileName){
        PrintWriter p = null; // declare p outside try-catch block
        try {
            p = new PrintWriter(new File(fileName));
            p.println(b.toString()); // "hello" is added to the file, ending with a newline character (\n)
            p.close();//if you do not close the file, the output file will remain blank
        } catch (Exception e) {
            return;
        }
    }
}
