// Written by Emmet Hoversten, hover114
import java.lang.Math;
public class Board {

    // Instance variables
    private Piece[][] board;

    //TODO:
    // Construct an object of type Board using given arguments.
    public Board() {
        this.board = new Piece[8][8];
    }

    // Accessor Methods

    //TODO:
    // Return the Piece object stored at a given row and column
    public Piece getPiece(int row, int col) {
        return this.board[row][col];
    }

    //TODO:
    // Update a single cell of the board to the new piece.
    public void setPiece(int row, int  col, Piece piece) {
        this.board[row][col] = piece;
    }
    // Game functionality methods

    //TODO:
    // Moves a Piece object from one cell in the board to another, provided that
    // this movement is legal. Returns a boolean to signify success or failure.
    // This method calls all necessary helper functions to determine if a move
    // is legal, and to execute the move if it is. Your Game class should not 
    // directly call any other method of this class.
    // Hint: this method should call isMoveLegal() on the starting piece. 
    public boolean movePiece(int startRow, int startCol, int endRow, int endCol) {
        if (getPiece(startRow, startCol) != null && getPiece(startRow, startCol).isMoveLegal(this, endRow, endCol)){
            setPiece(endRow, endCol, getPiece(startRow, startCol));
            setPiece(startRow, startCol, null);
            return true;
        }else {return false;}
    }

    //TODO:
    // Determines whether the game has been ended, i.e., if one player's King
    // has been captured.
    public boolean isGameOver() {
        int answerChecker = 0;
        for (int i=0; i<board.length; i++) {
            for (int j=0;j<board[i].length; j++){
                if (board[i][j]==null){
                    continue;
                }
                if (board[i][j].character == '\u2654' || board[i][j].character == '\u265A')
                    answerChecker++;
            }
        }
        return answerChecker!=2;
    }

    // Constructs a String that represents the Board object's 2D array.
    // Returns the fully constructed String.
    public String toString() {
        StringBuilder out = new StringBuilder();
        out.append(" ");
        for(int i = 0; i < 8; i++){
            out.append(" ");
            out.append(i);
        }
        out.append('\n');
        for(int i = 0; i < board.length; i++) {
            out.append(i);
            out.append("|");
            for(int j = 0; j < board[0].length; j++) {
                out.append(board[i][j] == null ? "\u2001|" : board[i][j] + "|");
            }
            out.append("\n");
        }
        return out.toString();
    }

    //TODO:
    // Sets every cell of the array to null. For debugging and grading purposes.
    public void clear() {
        for (int i=0; i<this.board.length; i++){
            for (int j=0; j<this.board[i].length; j++){
                this.board[i][j] = null;
            }
        }
    }

    // Movement helper functions

    //TODO:
    // Ensure that the player's chosen move is even remotely legal.
    // Returns a boolean to signify whether:
    // - 'start' and 'end' fall within the array's bounds.
    // - 'start' contains a Piece object, i.e., not null.
    // - Player's color and color of 'start' Piece match.
    // - 'end' contains either no Piece or a Piece of the opposite color.
    public boolean verifySourceAndDestination(int startRow, int startCol, int endRow, int endCol, boolean isBlack) {
        return (startRow<8 && startCol<8 && startRow >=0 && startCol>= 0 && endRow<8 && endCol<8 && endCol >=0 && endRow>= 0 && this.board[startRow][startCol] != null && (isBlack==this.getPiece(startRow, startCol).getIsBlack()) && (board[endRow][endCol]==null || (board[endRow][endCol].getIsBlack()!=board[startRow][startCol].getIsBlack())));
    }

    //TODO:
    // Check whether the 'start' position and 'end' position are adjacent to each other
    public boolean verifyAdjacent(int startRow, int startCol, int endRow, int endCol) {
        return (Math.abs(endCol-startCol)<=1 && Math.abs(endRow-startRow)<=1);
    }

    //TODO:
    // Checks whether a given 'start' and 'end' position are a valid horizontal move.
    // Returns a boolean to signify whether:
    // - The entire move takes place on one row.
    // - All spaces directly between 'start' and 'end' are empty, i.e., null.

    public boolean verifyHorizontal(int startRow, int startCol, int endRow, int endCol) {
        if (startRow==endRow){
            if (endCol==startCol){
                return true;
            }
            if (endCol>startCol) {
                for (int i = 1; i < (Math.abs(endCol - startCol)); i++) {
                    if (board[startRow][startCol + i] != null) {
                        return false;
                    }
                }
                return true;
            }
            else if (endCol<startCol) {
                for (int i = 1; i < (Math.abs(endCol - startCol)); i++) {
                    if (board[startRow][startCol - i] != null) {
                        return false;
                    }
                }
                return true;
            }
        }
        return false;
    }

    //TODO:
    // Checks whether a given 'start' and 'end' position are a valid vertical move.
    // Returns a boolean to signify whether:
    // - The entire move takes place on one column.
    // - All spaces directly between 'start' and 'end' are empty, i.e., null.
    public boolean verifyVertical(int startRow, int startCol, int endRow, int endCol) {
        int temp;
        if (startCol!=endCol){
            return false;
        }
        if (startRow==endRow && startCol==endCol){
            return true;
        }
        if (startRow>endRow){
            temp=startRow;
            startRow=endRow;
            endRow=temp;
        }
        for (int i=startRow+1; i<endRow; i++){
            if (board[i][startCol]!=null){
                return false;
            }
        }
        return true;
    }

    //TODO:
    // Checks whether a given 'start' and 'end' position are a valid diagonal move.
    // Returns a boolean to signify whether:
    // - The path from 'start' to 'end' is diagonal... change in row and col.
    // - All spaces directly between 'start' and 'end' are empty, i.e., null.
    public boolean verifyDiagonal(int startRow, int startCol, int endRow, int endCol) {
        int rowShift = 0;
        int colShift = 0;
        if (startRow == endRow && startCol==endCol){
            return true;
        }
        if (Math.abs(endCol-startCol)==Math.abs(endRow-startRow)){
            if (startCol<endCol){
                colShift=1;
            }
            else{
                colShift=-1;
            }
            if (startRow<endRow){
                rowShift=1;
            }
            else{
                rowShift=-1;
            }
            int end = Math.abs(endCol-startCol);
            for (int i=1; i<end; i++){
                if (board[(startRow+rowShift)][(startCol+colShift)] != null){
                    return false;
                }
                startRow+=rowShift;
                startCol+=colShift;
            }
            return true;
        }
        return false;
    }
}
