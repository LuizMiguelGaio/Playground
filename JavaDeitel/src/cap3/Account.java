package src.cap3;
// Figura 3.1: Account.java
// Classe Account que contém uma variável de instância name
// e métodos para configurar e obter seu valor.

public class Account {

    private String name; // variável de instância
    private double balance; // variável de instância

    public Account(String name, double balance){
        this.name = name; //atribui name à variavel de instancia name

        if(balance > 0.0)
            this.balance=balance;
    }

    public void deposit(double depositAmount){ //método que deposita(adiciona) apenas uma quantia válida no saldo
        if(depositAmount > 0.0) //se depositAmount for válido
            balance = balance + depositAmount; //o adiciona ao saldo
    }

    public void withdraw(double withdrawAmount){//método que retira quantia
        if(withdrawAmount > balance)
            System.out.println("Withdrawal amount exceeded account balance");
        else
            balance = balance - withdrawAmount;
    }

    public double getBalance(){ //método que retorna saldo da conta
        return balance;
    }


    public void setName(String name) { // método para definir o nome no objeto

        this.name = name; // armazena o nome
    }


    public String getName() { // método para recuperar o nome do objeto

        return name; // retorna valor do nome para o chamador
    }
} // fim da classe Account