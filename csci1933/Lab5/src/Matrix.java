public class Matrix {
    private int nrows;
    private int ncols;
    private int[][] matrix;
    public Matrix(int nrows, int ncols){
        this.nrows=nrows;
        this.ncols=ncols;
        this.matrix = new int[nrows][ncols];
    }
    public Matrix(int[][] arr){
        this.nrows = arr.length;
        this.ncols = arr[0].length;
        this.matrix = arr;
    }
    public Matrix transpose(){
        Matrix newMatrix = new Matrix(ncols,nrows);
        for (int i=0; i<this.nrows; i++){
            for (int j=0; j<this.ncols; j++){
                newMatrix.matrix[j][i]=this.matrix[i][j];
            }
        }
        return newMatrix;
    }
    public String toString(){
        String answer = "";
        for (int i=0; i<nrows; i++){
            for (int j=0; j<ncols; j++){
                answer+=this.matrix[i][j] + " ";
            }
            answer+="\n";
        }
        return answer;
    }
}
