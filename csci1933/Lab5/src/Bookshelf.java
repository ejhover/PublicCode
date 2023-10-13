public class Bookshelf {
    public Book[] books;
    private int nextEmpty = 0;
    public Bookshelf(){
        books = new Book[20];
    }
    public Bookshelf(int numBooks){
        books = new Book[numBooks];
    }
    public Bookshelf(Book[] bookList){
        books = bookList;
    }
    public boolean add(Book newBook){
        if (nextEmpty>=books.length) {
            return false;
        }
        else{
            books[nextEmpty] = newBook;
            nextEmpty++;
            return true;
        }
    }
    public Bookshelf getBooksByAuthor(String author){
        int newLen = 0;
        Bookshelf newShelf;
        for (int i=0; i<books.length; i++){
            if (books[i].getAuthor().equals(author)){
                newLen++;
            }
        }
        newShelf = new Bookshelf(newLen);
        for (int i=0; i<books.length; i++) {
            if (books[i].getAuthor().equals(author)) {
                newShelf.add(books[i]);
            }
        }
        return newShelf;
    }
    public void sort(char sortBy){
        Boolean swapped = true;
        Book temp;
        System.out.println(nextEmpty-1);
        System.out.println(books.length);
        for (int i=0; i<nextEmpty && swapped ; i++) {
            swapped = false;
            for (int j = 1; j < nextEmpty-i; j++){
                if ((books[j].compareTo(books[j - 1], sortBy)) < 0) {
                    swapped = true;
                    temp = books[j];
                    books[j] = books[j - 1];
                    books[j - 1] = temp;
                }
            }
        }
    }
//    for (i = 0; i < a.length && swapped == true; i++) {
//        swapped = false;
//        for (j = 1; j < a.length - i; j++) {
//            counter++;
//            if (a[j] < a[j-1]) {
//                swapped = true;
//                temp = a[j];
//                a[j] = a[j-1];
//                a[j-1] = temp;
//            }
//        }
//    }
    public String toString(){
        String bookString = "";
        for (int i=0;i<nextEmpty;i++){
            bookString+=(books[i].getTitle()+", "+books[i].getAuthor()+", "+books[i].getRating()+"\n");
        }
        return bookString;
    }
}
