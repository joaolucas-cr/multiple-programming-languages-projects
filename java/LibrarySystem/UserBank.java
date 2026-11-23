import java.util.*;
import java.io.*;

public class UserBank {
    private static ArrayList<User> users = new ArrayList<>();

    public static String register(String name) {
        try {
            User user = new User(name);
            users.add(user);
            return user.id + " " + user.name;
        } catch (Exception error) {
            System.out.println(error);
            return "";
        }
    } 

    public static User getUser(String userId) {
        for(int i = 0; i < users.size(); i++) {
            if (users.get(i).id.equals(userId)) return users.get(i);
        }
        return null;
    }

    public static void load() {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("data/users.csv"));
            reader.readLine();
            String line = reader.readLine();

            while(line != null) {
                String[] parts = line.split(",");
                String id = parts[0];
                String name = parts[1];
                String bookId1 = parts[2];
                String bookId2 = parts[3];
                String bookId3 = parts[4];
                User user = new User(name, id);
                
                Book book1 = BookCollection.getBook(bookId1);
                Book book2 = BookCollection.getBook(bookId2);
                Book book3 = BookCollection.getBook(bookId3);

                if(book1 != null) {
                    user.booksReserved.add(book1);
                    if(book2 != null) {
                    user.booksReserved.add(book2);
                        if(book3 != null) {
                            user.booksReserved.add(book3);
                        } 
                    }
                } 
                line = reader.readLine();
                users.add(user);
            }

            System.out.println("Loaded users sucessfully");

        } catch (IOException error) {
            System.out.println("Error loading user X X X");
            System.out.println(error.getMessage());
        }
    }

    public static void save() {
        try {
            FileWriter writer = new FileWriter("data/users.csv");
            writer.write("id,name,book1,book2,book3\n");
            for (int i = 0; i<users.size(); i++) {
                User user = users.get(i);
                writer.write(user.id+","+user.name);
                for(int j = 0; j < 3; j++) {
                    if(user.booksReserved.size() > j) {
                        writer.write(","+user.booksReserved.get(j).id);
                    } else {
                        writer.write(",null");
                    }
                }
                writer.write("\n");
            }
            writer.close();
        } catch (IOException error) {
            System.out.println(error.getMessage());
        }
    } 
}