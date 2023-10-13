
public class Histogram {
    int lower;
    int upper;
    int histo[];
    public Histogram(int lowerbound, int upperbound) {
        lower=lowerbound;
        upper=upperbound;
        histo = new int[upper-lower+1];
    }
    public boolean add(int i) {
        if (i<=upper && i>=lower){
            histo[i-lower]=histo[i-lower]+1;
            return true;
        }
        else{
            return false;
        } 
    }
    public String toString() {
        String ans="";
        for (int i=lower; i<=upper;i++){
            ans=ans+i+":";
            for (int j=0;j<histo[i-lower];j++){
                ans=ans+"*";
            }
            ans=ans+"\n";
        }
        return ans;
    }
    public static void main(String args[]) {
        Histogram histog = new Histogram(0, 5);
        histog.add(3);
        histog.add(2);
        histog.add(1);
        histog.add(2);
        histog.add(3);
        histog.add(0);
        histog.add(1);
        histog.add(5);
        histog.add(3);
        System.out.println(histog);
    }
}
