import java.util.Scanner;
public class helloworld{
public static void main(String[]args){
	Scanner scanner = new Scanner (System.in);
	System.out.println("Enter you age: ");
		int age = scanner.nextInt();
		if (age>=30){
					System.out.println("you are an adult");
					}
		else{
			System.out.println("you are a student");
			}
		scanner.close();
}
}
		