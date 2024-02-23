package cap2Deitel;
//aritmética
import java.util.Scanner;

public class Questao2_15 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int x,y;
		
		System.out.printf("Insira um inteiro: ");
		x = input.nextInt();
		System.out.printf("Insira um inteiro: ");
		y = input.nextInt();
		
		System.out.printf("soma :%d%n", x + y);
		System.out.printf("produto :%d%n", x * y);
		System.out.printf("diferença :%d%n", x - y);
		System.out.printf("quociente :%d%n", x / y);
	}

}
