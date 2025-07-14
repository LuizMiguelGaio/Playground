package src.cap3;
//3.14
public class DateTest {
    public static void main(String[] args) {
        // Criando uma instância de Date
        Date minhaData = new Date(25, 2, 2022);

        // Exibindo a data utilizando o método displayDate
        minhaData.displayDate(minhaData.getDia(), minhaData.getMes(), minhaData.getAno());

        // Alterando a data utilizando os métodos set
        minhaData.setDia(10);
        minhaData.setMes(6);
        minhaData.setAno(2023);

        // Exibindo a data após a alteração
        minhaData.displayDate(minhaData.getDia(), minhaData.getMes(), minhaData.getAno());
    }
}
