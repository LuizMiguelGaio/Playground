package src.cap4;
//4.19
import java.util.Scanner;
public class Comissao {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        double venda =0.0;
        double vendaTotal =0.0;


        while (venda != -1){
            System.out.println("Insira um valor da venda ou digite -1 pra encerrar: \n");
            venda = in.nextDouble();
            vendaTotal = vendaTotal + venda;
        }

        double comissao=vendaTotal*0.09; //9% das vendas
        double salario =200.00+comissao;

        System.out.printf("Os redimentos do vendedor de acordo com as vedas é de: %.2f%n",salario);

    }
}
