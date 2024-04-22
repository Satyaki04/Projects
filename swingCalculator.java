import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class swingCalculator{
    public static void main(String args[]){
        JFrame f= new JFrame("Calculator");

        JLabel l1=new JLabel("First Number:");
        l1.setBounds(30,100,150,40);

        JTextField t1=new JTextField();
        t1.setBounds(200,100,150,40);

        JLabel l2=new JLabel("Second Number:");
        l2.setBounds(30, 150, 150,40);
        JTextField t2=new JTextField();
        t2.setBounds(200,150,150,40);

        JLabel l3=new JLabel("Result:");
        l3.setBounds(30, 200, 150,40);
        JTextField t3=new JTextField();
        t3.setBounds(200,200,150,40);

        JButton add=new JButton("Add");
        add.setBounds(30, 250, 70,30);
        add.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num1=Integer.parseInt(t1.getText());
                int num2=Integer.parseInt(t2.getText());
                int r=num1+num2;
                t3.setText(" "+r);
            }
        });

        JButton sub=new JButton("Sub");
        sub.setBounds(110, 250, 70,30);
        sub.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num1=Integer.parseInt(t1.getText());
                int num2=Integer.parseInt(t2.getText());
                int r=num1-num2;
                t3.setText(" "+r);
            }
        });

        JButton mul=new JButton("Mul");
        mul.setBounds(190, 250, 70,30);
        mul.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int num1=Integer.parseInt(t1.getText());
                int num2=Integer.parseInt(t2.getText());
                int r=num1*num2;
                t3.setText(" "+r);
            }
        });

        JButton re=new JButton("Reset");
        re.setBounds(270, 250, 70,30);
        re.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                t1.setText("");
                t2.setText("");
                t3.setText("");
            }
        });

        
        f.add(l1);f.add(l2);f.add(l3);f.add(t1);f.add(t2);f.add(t3);f.add(add);f.add(sub);f.add(mul);f.add(re);
        f.setSize(400,300);
        f.setLayout(null);
        f.setVisible(true);
    }
}