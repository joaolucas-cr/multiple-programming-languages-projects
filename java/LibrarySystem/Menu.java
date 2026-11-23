import java.util.*;

public class Menu {
	public static void showMenu() {
		System.out.println("\nLibrary System CLI:");
		System.out.println("\nadd: add book with publication year, title, author or ID");
		System.out.println("search: search based on publication year, title, author or ID");
		System.out.println("register: create new users in the users bank");
		System.out.println("borrow: borrow a book from the library");
		System.out.println("list: list all book from the library");
		System.out.println("save: save all data from the library");
		System.out.println("return: return a book to the library");

		System.out.println("exit: to exit\n");

		Scanner input = new Scanner(System.in);
		String option;
		boolean exit = false;

		while(!exit) {
			System.out.print("Type command: ");
			option = input.nextLine();
			option = option.trim();
			switch (option) {
				case "search":
					System.out.print("Type author, title, year or ID: ");
					String term = input.nextLine();
					ArrayList<Book> matched = BookCollection.searchBooks(term); 
					System.out.println("\nsearching...");

					for (int i = 0; i < matched.size(); i++) {
						System.out.println(matched.get(i));
					}

					break;

				case "add":
					System.out.print("Author: ");
					String author = input.nextLine();
					System.out.print("Title: ");
					String title = input.nextLine();
					System.out.print("Year: ");
					int year = input.nextInt();
					input.nextLine();
					boolean created = BookCollection.addBook(author, title, year);
					if(created) System.out.println("Successfully added the book");
					break;

				case "exit":
					System.out.println("exiting...");
					exit = true;
					break;

				case "register":  {
					System.out.print("User's name: ");
					String name = input.nextLine();
					String response = UserBank.register(name);
					if(response.length() > 0) {
						System.out.println("Succesfully created user: " + response);
					} else {
						System.out.println("Failed at creating user");
					}
					break;
				}

				case "borrow": {
					System.out.print("User id: ");
					String userId = input.nextLine();
					System.out.print("Book id: ");
					String bookId = input.nextLine();
					String response = BookCollection.borrowBook(userId, bookId);
					System.out.println(response);	
					break;	
				}	

				case "return": {
					System.out.print("User id: ");
					String userId = input.nextLine();
					System.out.print("Book id: ");
					String bookId = input.nextLine();
					BookCollection.returnBook(userId, bookId);
					break;	
				}

				case "list": {
					System.out.println("\n");
					for(int i = 0; i < BookCollection.getBooks().size(); i++) {
						System.out.println(BookCollection.getBooks().get(i));
					}
					System.out.println("\n");
					break;
				}

				case "save": {
					BookCollection.save();
					UserBank.save();
					break;
				}

				default: 
					System.out.println("Invalid input");
					break;
			}
		}
        }
}
