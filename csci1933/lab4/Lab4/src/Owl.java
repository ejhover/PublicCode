public class Owl {
    private String name;
    private int age;
    private double weight;
    public Owl(String owlName, int owlAge, double owlWt) {
        name = owlName;
        age = owlAge;
        weight = owlWt;
    }
    public String getName(){
        return name;
    }
    public void setName(String owlName){
        name = owlName;
    }
    public int getAge(){
        return age;
    }
    public void setage(int owlAge){
        age = owlAge;
    }
    public double getWeight(){
        return weight;
    }
    public void setWeight(double owlWt){
        weight = owlWt;
    }
    public boolean equals(Owl other) {
        return (other.getAge() == this.getAge() && other.getWeight() == this.getWeight() && other.getName().equals(this.getName()));
    }
    public static void main(String[] args){
        Owl owl1 = new Owl("owl1", 5, 12.0);
        Owl owl2 = new Owl("owl2", 5, 12.0);
        Owl owl3 = new Owl("owl1", 5, 12.0);
        System.out.println(owl1.equals(owl2));
        System.out.println(owl1.equals(owl3));
    }
}
