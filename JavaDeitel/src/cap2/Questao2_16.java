package cap2Deitel;
//Comparando inteiros
import java.util.Scanner;

public class Questao2_16 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		double x,y;
		
		System.out.println("Insira um número: ");
		x = input.nextDouble();
		System.out.println("Insira um número: ");
		y = input.nextDouble();
		
		if(x > y)
			System.out.println("is larger");
		if(x == y)
			System.out.println("There numbers are equal");
		
		
	}

}
