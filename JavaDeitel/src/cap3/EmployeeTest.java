package src.cap3;
//exe 3.13
import java.util.Scanner;

public class EmployeeTest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        Employee employee1 = new Employee("Luiz", "Miguel", 100.0);
        Employee employee2 = new Employee("Miguel", "Gaio", 200.0);

        double anualSalary = employee1.getMountSalary();
        double anualSalary2 = employee2.getMountSalary();

        System.out.printf("the anual salary of %s is %.2f%n", employee1.getName(), anualSalary);
        System.out.printf("the anual salary of %s is %.2f%n", employee2.getName(), anualSalary2);

        double aumento1 = anualSalary + anualSalary*0.10;
        double aumento2 = anualSalary2 + anualSalary2*0.10;

        System.out.printf("the anual salary of %s with 10%% is %.2f%n", employee1.getName(), aumento1);
        System.out.printf("the anual salary of %s with 10%% is %.2f%n", employee2.getName(), aumento2);

        /*System.out.println("Change name for : ");
        String name = input.next();
        employee1.setName(name);
        System.out.printf("New name account is %s%n", name);

        System.out.println("Change last name for : ");
        String lastName = input.next();
        employee1.setLastName(lastName);
        System.out.printf("New name account is %s%n", lastName);

        System.out.println("Change the salary for : ");
        double mountSalary = input.nextDouble();
        employee1.setMountSalary(mountSalary);
        System.out.printf("the salary of account is %.2f%n", mountSalary);*/




    }
}
