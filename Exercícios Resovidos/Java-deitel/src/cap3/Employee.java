package src.cap3;
//exe 3.13
public class Employee {
    private String name;
    private String lastName;
    private double mountSalary;

    public Employee(){

    }

    public Employee(String name, String lastName, double mountSalary){
        this.name = name;
        this.lastName = lastName;
        if(mountSalary < 0)
            System.out.println("the amount typed its negative.");
        else   this.mountSalary = mountSalary;
    }

    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }

    public void setLastName(String lastName){
        this.lastName = lastName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setMountSalary(double mountSalary){
        if(mountSalary < 0)
            System.out.println("the amount typed its negative.");
        else
            this.mountSalary = mountSalary;
    }

    public double getMountSalary(){
        return mountSalary;
    }

}
