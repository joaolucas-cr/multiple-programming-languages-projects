import java.util.*;

public class Book {

	public String id;
	public String title;
	public String author;
	public boolean borrowed = false;
	public int year;

	private void create(String title, String author, int year) {
		this.title = title; 
		this.author = author;
		this.year = year;
		this.borrowed = false;
	}

	public Book(String title, String author, int year) {
		create(title, author, year);
		this.id = UUID.randomUUID().toString();
	}

	public Book(String title, String author, int year, boolean available, String id) {
		create(title, author, year);
		this.borrowed = !available;
		this.id = id;
	}

	

	public String toString() {
        return this.title + ", " + this.author + ", " + this.year + ", " + this.id + ", borrowed: " + this.borrowed;
    }


}
