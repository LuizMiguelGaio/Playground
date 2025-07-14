package src.cap4;

import javax.swing.JFrame;
import java.awt.Polygon;

public class DrawJavaLogo {
    public static void main(String[] args) {
        // Cria um JFrame
        JFrame frame = new JFrame("Java Logo");

        // Cria uma instância de DrawPanel
        DrawPanel drawPanel = new DrawPanel();

        // Adiciona a instância de DrawPanel ao JFrame
        frame.add(drawPanel);

        // Configura o JFrame
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

class DrawPanel extends javax.swing.JPanel {
    @Override
    public void paintComponent(java.awt.Graphics g) {
        super.paintComponent(g);

        // Cria um objeto Polygon para representar o logotipo do Java
        Polygon poly = new Polygon();
        poly.addPoint(30, 80);
        poly.addPoint(60, 40);
        poly.addPoint(90, 80);
        poly.addPoint(80, 80);
        poly.addPoint(60, 60);
        poly.addPoint(40, 80);

        // Desenha o logotipo do Java usando o Polygon
        g.drawPolygon(poly);
    }
}
