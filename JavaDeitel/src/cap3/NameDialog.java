package src.cap3;
import javax.swing.JOptionPane;
public class NameDialog {
    public static void main(String[] args) {
        //pede para o usuario inserir seu nome.
        String name = JOptionPane.showInputDialog("What is your name?");

        //cria a mensagem
        String message = String.format("Welcome, %s, to Java Programming!", name);

        //exibe a mensagem na tela
        JOptionPane.showMessageDialog(null,message);
    }

}
