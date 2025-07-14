package cap2Deitel;

import java.util.Scanner;

public class CalculadoraCrescimentoDemograficoMundialQueNomeGrandePraCacete {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        double nascimentos, mortes, saldoMigratorio, populacaoTotal, total;

        System.out.println("Antes de inserir seria bom ter os dados de Nascimentos, mortes, Saldo Migratorio e população total atual.");

        System.out.println("De acordo com sua pesquisa, insira a taxa de nascimento mundial: ");
        nascimentos = in.nextDouble();
        System.out.println("Insira a taxa de mortes mundial: ");
        mortes = in.nextDouble();
        System.out.println("Insira o saldo migratorio mundial: ");
        saldoMigratorio = in.nextDouble();
        System.out.println("Insira a população total mundial: ");
        populacaoTotal = in.nextDouble();

        total = nascimentos - mortes + saldoMigratorio * 100 / populacaoTotal;

        System.out.printf("%f", total);

        in.close();

    }

}
