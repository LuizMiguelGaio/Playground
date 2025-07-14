package src.cap4;
//resposta 4.17
import java.util.Scanner;
public class QuilometragemComb {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int flag = 0;
        int kmphT = 0;
        int totalLitros = 0;

        while(flag != -1){
            //Entrada de dados
            System.out.println("Insira a Kilometragem ou digite -1 pra sair");
            int kmph = input.nextInt();
            if(kmph == -1){
                flag = -1;
            }else{
                kmphT += kmph;
            }

            System.out.println("Insira os Litros de Gasolina gastos ou digite -1 pra sair");
            int litrosGasolina = input.nextInt();
            if(litrosGasolina == -1){
                flag = -1;
            }else{
                totalLitros += litrosGasolina;
            }
        }

        System.out.println("Total de KM: " + kmphT);
        System.out.println("Total de Litro: " + totalLitros);

        input.close();
    }




        //consumo quilometro/litro




}
