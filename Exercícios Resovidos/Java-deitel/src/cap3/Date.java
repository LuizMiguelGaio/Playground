package src.cap3;

//exe 3.14
public class Date {
    private int mes;
    private int dia;
    private int ano;

    public Date() {

    }

    public Date(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public void setDia(int dia) {
        this.dia = dia;
    }

    public int getDia() {
        return dia;
    }

    public void setMes(int mes) {
        this.mes = mes;
    }

    public int getMes() {
        return mes;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public int getAno() {
        return dia;
    }

    public void displayDate(int dia,int mes, int ano){
        String formattedDate = String.format("%02d/%02d/%d", dia, mes, ano);
        System.out.println(formattedDate);
    }

}
