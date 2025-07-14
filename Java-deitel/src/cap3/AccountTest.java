package src.cap3;
// Figura 3.2: AccountTest.Java, atualização 3.15
// Cria e manipula um objeto Account.

import java.util.Scanner;

public class AccountTest {
    public static void main(String[] args) {

        String name;
        float balance;

        // cria um objeto Account e o atribui as Accounts
        Account Account1 = new Account("Luiz Miguel", 10.00);
        Account Account2 = new Account("Ricado Gaio", 30.00);
        // exibe o valor inicial do nome (null)

        // cria um objeto Scanner para obter entrada a partir da janela de comando
        Scanner input = new Scanner(System.in);

        // solicita o deposito Account1 e lê
        System.out.println("Enter deposit Amount for account1: ");
        double depositAmount = input.nextDouble(); // obtem a entrada do usuário
        System.out.printf("%nadding %.2f to account1 balance%n%n", depositAmount);
        Account1.deposit(depositAmount); //adiciona o saldo de account1

        //exibe os saldos
        displayAccount(Account1);
        displayAccount(Account2);

        // solicita o deposito Account2 e lê
        System.out.println("Enter deposit Amount for account2: ");
        depositAmount = input.nextDouble(); // obtem a entrada do usuário
        System.out.printf("%nadding %.2f to account2 balance%n%n", depositAmount);
        Account2.deposit(depositAmount);



        //exibe os saldos
        System.out.printf("%s balance: %.2f %n", Account1.getName(), Account1.getBalance());
        System.out.printf("%s balance: %.2f %n", Account2.getName(), Account2.getBalance());

        //solicita a retirada de Account1 exe 3.11
        System.out.println("Enter de withdraw Account1: ");
        double withdrawAmount = input.nextDouble();
        Account1.withdraw(withdrawAmount);

        //exibe os saldos
        displayAccount(Account1);
        displayAccount(Account2);

        //adiciona o saldo de account1
        //myAccount.setName(theName); // insere theName em myAccount ÿ
        //System.out.println(); // gera saída de uma linha em branco
        // exibe o nome armazenado no objeto myAccount
        //System.out.printf("Name in object myAccount is:%n%s%n", myAccount.getName());
        input.close(); //fecha input
    }
    //exe 3.15

    public static void displayAccount(Account accountToDisplay){
        Account account = new Account(accountToDisplay.getName(), accountToDisplay.getBalance());
        System.out.printf("%s balance: $%.2f %n", accountToDisplay.getName(), accountToDisplay.getBalance());
    }
}
/* fim da classe AccountTest */