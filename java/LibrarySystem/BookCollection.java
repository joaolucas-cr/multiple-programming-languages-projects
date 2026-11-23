import java.util.*;
import java.io.*;

public class BookCollection {

    private static ArrayList<Book> books = new ArrayList<>();
    
    public static void load() {
            try {
                BufferedReader reader = new BufferedReader(new FileReader("data/books.csv"));
                reader.readLine();

                //read csv: id,title,author,year,available
                String line = reader.readLine();

                while(line != null) {
                    String[] parts = line.split(",");
                    String id = parts[0];
                    String title = parts[1];
                    String author = parts[2];
                    int year = Integer.parseInt(parts[3]);
                    boolean available = Boolean.parseBoolean(parts[4]);
                    Book book = new Book(title, author, year, available, id);
                    books.add(book);
                    line = reader.readLine();
                }
                System.out.println("Sucessfully loaded books");
            } catch(Exception error) {  
                System.out.println("Error while loading books X-X-X" + error.getMessage());
            }
    } 


    public static boolean addBook(String title, String author, int year) {
        Book book = new Book(title, author, year);
        books.add(book);
        return true;
    }

    public static ArrayList<Book> searchBooks(String term) {
        ArrayList<Book> matched = new ArrayList<>();
        for (int i = 0; i < books.size(); i++) {
            Book checkingBook = books.get(i);
            if(checkingBook.title.toLowerCase().contains(term)
                || checkingBook.author.toLowerCase().contains(term)
            ) {
                matched.add(checkingBook);
            } else {
                try {
                    int year = Integer.parseInt(term);
                    if (checkingBook.year == year) matched.add(checkingBook);
                } catch (Exception error) {  }
            }
        }

        return matched;
    }

    public static ArrayList<Book> getBooks() {
        return books;
    }

    public static Book getBook(String id) {
        for (int i = 0; i < books.size(); i++) {
            if (books.get(i).id.equals(id)) return books.get(i);
        }
        return null;
    }

    public static String borrowBook(String userId, String bookId) {
        try {
            User user = UserBank.getUser(userId);
            if(user.booksReserved.size() >= 3) {
                return "User already borrowed 3 books, which is the limit. No more borrows allowed, until the user returns one or more books";
            }
            Book book = getBook(bookId);
            if(!book.borrowed) {
                book.borrowed = true; 
            } else {
                return "Book already borrowed";
            }
            user.booksReserved.add(book);    
            return "Succesfully borrowed book";
        } catch (Exception error) {
            return error.getMessage();
        }
    }

    public static void returnBook(String userId, String bookId) {
        Book book = getBook(bookId);
        User user = UserBank.getUser(userId);

        if(book == null) {
            System.out.println("No book found on book bank");
            return;
        }
        if(user == null) {
            System.out.println("No user found on user bank");
            return;
        }

        for (int i = 0; i < user.booksReserved.size(); i++) {
            if(user.booksReserved.get(i).id.equals(bookId)) {
                user.booksReserved.remove(i);
                book.borrowed = false;
                break;
            }
        }
    }

    public static void save() {
        try {
            FileWriter writer = new FileWriter("data/books.csv");
            writer.write("id,title,author,year,available\n");
            for(int i = 0; i < books.size(); i++) {
                Book book = books.get(i);
                writer.write(book.id+","+book.title+","+book.author+","+book.year+","+!book.borrowed+"\n");
            }
            writer.close();
        } catch (IOException error) {
            System.out.println(error.getMessage());
        }
    }

}