package src.cap3;
//3.16

public class HeartRates {
    private String nome;
    private String sobreNome;
    private Date dataNascimento;

    public HeartRates(String nome, String sobreNome, int dia, int mes, int ano){
        this.nome = nome;
        this.sobreNome = sobreNome;
        this.dataNascimento = new Date(dia, mes, ano);
    }

    public void calcIdade(){

    }

    public void freqCardiacaMax(int ano){
        int freqCardiacaMax = ano - 220;
    }

    public void freqCardiacaAlvo(){

    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setSobreNome(String sobreNome) {
        this.sobreNome = sobreNome;
    }

    public String getSobreNome() {
        return sobreNome;
    }
}
