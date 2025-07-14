package cap2Deitel;

import java.util.Scanner;

public class Questao2_8 {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int a,b,c;
		System.out.print("Enter an interger: ");
		c = input.nextInt();

		System.out.print("Enter an interger: ");
		b = input.nextInt();

		a = b * c; //calculo de folha de pag. 
		
		System.out.printf("%d", a);
	
	}
}
