package cap2Deitel;

import java.util.Scanner;

public class CalculadoraIMC {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		
		double pesoEmQuilogramas, alturaEmMetro, IMC;
		
		System.out.print("Escreva seu peso: ");
		pesoEmQuilogramas = input.nextDouble();
		System.out.print("Escreva sua altura: ");
		alturaEmMetro = input.nextDouble();
		
		IMC = pesoEmQuilogramas / Math.pow(alturaEmMetro, 2);
		
		if(IMC <= 18.5)
			System.out.println("Underweight");
		else if(IMC > 18.5 && IMC <= 24.9)
			System.out.println("Normal");
		else if(IMC >= 25 && IMC <= 29.9)
			System.out.println("Overweight");
		else
			System.out.println("Greater");
		
		input.close();

	}

}
