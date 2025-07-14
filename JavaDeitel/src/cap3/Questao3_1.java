package src.cap3;

import javax.swing.*;

public class Questao3_1 {
    public static void main(String[] args) {
        //pede para o usuario inserir seu nome.
        String name = JOptionPane.showInputDialog("What is your name?");
        //Convertendo a String em Int
        int numeroFromName = name.hashCode();

        //cria a mensagem
        String message = String.format("Welcome, %s, Your numerical value is: %d",name, numeroFromName);

        //exibe a mensagem na tela
        JOptionPane.showMessageDialog(null,message);
    }
}
