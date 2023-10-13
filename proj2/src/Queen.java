// Written by Emmet Hoversten, hover114
public class Queen {
    private int row;
    private int col;
    private boolean isBlack;
    public Queen (int row, int col, boolean isBlack) {
        this.row = row;
        this.col = col;
        this.isBlack = isBlack;
    }
    public boolean isMoveLegal(Board board, int endRow, int endCol) {
        if (endRow==this.row){
            return (board.verifySourceAndDestination(this.row, this.col, endRow, endCol, this.isBlack) && board.verifyHorizontal(this.row, this.col, endRow, endCol));
        }
        else if (endCol==this.col){
            return (board.verifySourceAndDestination(this.row, this.col, endRow, endCol, this.isBlack) && board.verifyVertical(this.row, this.col, endRow, endCol));
        }
        else if (board.verifyDiagonal(this.row, this.col, endRow, endCol)){
            return true;
        }
        else{
            return false;
        }
    }
}
