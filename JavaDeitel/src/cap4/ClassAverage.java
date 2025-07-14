package src.cap4;
//resolvido a partir de um pseudo código. 4.9 figura 4.8(livro)
import java.util.Scanner;
public class ClassAverage {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int total = 0;
        int cont = 1;
        int media;
        while(cont <=10){
            System.out.printf("%d Insira uma nota :", cont);
            int nota = input.nextInt();
            total = total + nota;
            cont++;
        }
        media = total/10;
        System.out.println("A media da turma é: "+ media);
    }
}
