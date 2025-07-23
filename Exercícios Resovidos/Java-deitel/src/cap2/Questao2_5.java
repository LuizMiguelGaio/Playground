package cap2Deitel;

import java.util.Scanner;

public class Questao2_5 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int x,y,z, produto;
		
		System.out.println("insira um inteiro: ");
		x = input.nextInt();
		System.out.println("insira um inteiro: ");
		y = input.nextInt();
		System.out.println("insira um inteiro: ");
		z = input.nextInt();
		
		input.close();
		
		produto = x * y * z;
		
		System.out.printf("Product is %d%n", produto);		
	}

}
