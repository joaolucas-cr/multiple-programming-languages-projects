import java.util.*;


public class User {
    public String name;
    public String id;
    public ArrayList<Book> booksReserved = new ArrayList<>();


    public User(String name) {
        this.name = name;
        this.id = UUID.randomUUID().toString();
    }

    public User(String name, String id) {
        this.name = name;
        this.id = id;
    }

    public String toString() {
        return this.name;
    }

    public void borrowBook(Book book) {
        this.booksReserved.add(book);
    }


}