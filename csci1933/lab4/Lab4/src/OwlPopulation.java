import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileWriter;

public class OwlPopulation {
    private String fileName;
    private Owl[] data;


    public OwlPopulation(String fN) throws FileNotFoundException {
        //TODO: Populate the class variables in OwlPopulation
        fileName = fN;
        populateData();
    }
    public int populateData() throws FileNotFoundException {
        File f = new File(fileName);
        Scanner scanner = new Scanner(f);

        int numLines = 0;
        while(scanner.hasNextLine()){
            numLines++;
            String s = scanner.nextLine();
        }
        scanner.close();

        data = new Owl[numLines];   //data is allocated the exact amount of space it needs
//        File o = new File(fileName);
        Scanner scan = new Scanner(f);
        int i = 0;
        while(scan.hasNextLine()) {
            String s = scan.nextLine();
            String tempName = s.split(",")[0];
            int tempAge = Integer.parseInt(s.split(",")[1]);
            double tempWeight = Double.parseDouble(s.split(",")[2]);
            data[i] = new Owl(tempName, tempAge, tempWeight);
            i++;
        }
        //TODO: Populate the data with owls constructed from the lines of the file given
        return numLines;
    }

    public double averageAge(){
        int totalAge = 0;
        for (int j=0; j<data.length; j++){
            totalAge += data[j].getAge();
        }
        return (float) totalAge/data.length;
    }

    public Owl getYoungest(){
        Owl youngest = new Owl("youngOwl", 999, 0.0);
        for (int i=0; i<data.length; i++) {
            if (data[i].getAge() < youngest.getAge()) {
                youngest = data[i];
            }
        }
        return youngest;
    }

    public Owl getHeaviest(){
        Owl heaviest = new Owl("youngOwl", 999, 0.0);
        for (int i=0; i<data.length; i++) {
            if (data[i].getWeight() > heaviest.getWeight()) {
                heaviest = data[i];
            }
        }
        return heaviest;
    }

    public String toString(){
        return "The youngest owl is " + this.getYoungest().getName() + ", which is " + this.getYoungest().getAge() + " years old.\n" + "The heaviest owl is " + this.getHeaviest().getName() + ", which weighs " + this.getHeaviest().getWeight() + " pounds.\n" + "The average age of the population is " + this.averageAge() + ".";
    }

    public boolean containsOwl(Owl other){
        for (int i=0;i<data.length;i++){
            if (data[i].equals(other))
                return true;
        }
        return false;
    }

    public void merge(OwlPopulation other){
        //TODO: a brief overview of what you can do to implement this method is given below:
        Owl[] newOwls;
        int numUnique = 0;
        for (int i=0; i<other.popSize(); i++){
            if (! this.containsOwl(other.data[i])) {
                other.data[numUnique] = other.data[i];
                numUnique++;
            }
        }
        newOwls = new Owl[this.popSize()+numUnique];
        for (int i=0;i<this.popSize();i++){
            newOwls[i]=this.data[i];
        }
        for (int i=0;i<numUnique;i++) {
            newOwls[this.popSize()+i] = other.data[i];
        }
        this.data = newOwls;
        //1) determine (and store) the distinct owls in the other population.

        //2) make a new data array to hold the correct number of owls for the merged population

        //3) copy over the distinct owls from each population to the data array

        //4) set the new data array to "this" data (where is the merged population? what happens to the original populations?)
    }

    public int popSize(){
        return data.length;
    }

    public static void main(String[] args) {
        try {

            //The following should run when you are complete. Feel free to comment out as you see fit while you work.
            OwlPopulation pop1 = new OwlPopulation("owlPopulation1.csv");

            System.out.println(pop1);
            System.out.println(pop1.popSize());

            OwlPopulation pop2 = new OwlPopulation("owlPopulation2.csv");
            System.out.println(pop2);
            System.out.println(pop2.popSize());

            pop1.merge(pop2);
            System.out.println(pop1);
            System.out.println(pop1.popSize());
        }
        catch (FileNotFoundException f){
            System.out.println("File not found.");
        }
    }


}