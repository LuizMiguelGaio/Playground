package src.cap4;
//4.18
import java.util.Scanner;
public class CalcularLimitCred {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int numeroDeConta;
        int saldoInicial =0;
        int despesas =0;
        int credito =0;
        int limiteCredito;
        int saldoTeste;
        int saldo;

        System.out.println("Digite o numero da conta: \n");
        numeroDeConta = input.nextInt();
        System.out.println("Digite o saldo inicial da conta: \n");
        saldoInicial = input.nextInt();
        System.out.println("Digite o qtd total de item: \n");
        despesas = input.nextInt();
        System.out.println("Digite o qtd Credito: \n");
        credito = input.nextInt();
        System.out.println("Digite o limite de crédito: \n");
        limiteCredito = input.nextInt();

        saldoTeste = saldoInicial+despesas-credito;



        if(saldoTeste>limiteCredito){
            System.out.println("O limite de credito foi excedido");
        }else{
            saldo = saldoTeste;
            System.out.println("O novo saldo é de: "+saldo);
        }

    }
}
