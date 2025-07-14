package src.cap4;

import java.util.Scanner;
public class Analisys {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

    int count = 1;
    int aprov = 0;
    int reprov = 0;
    int result = 0;

        while (count <= 10){
            System.out.printf("%d Insira Resultado: %n", count);
            result = input.nextInt();
            if(result==1)
                aprov = aprov + 1;
            else if(result==2)
                reprov = reprov + 1;
            count++;
        }
        System.out.println("Numero de Alunos aprovados : \n"+ aprov);
        System.out.println("Numero de Alunos reprovados : \n"+ reprov);

        if(aprov >= 8) {
            System.out.println("Bonus to Instructor!");
        }
    }

}
