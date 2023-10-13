// Written by Emmet Hoversten, hover114
import java.util.Scanner;

public class Piece {
    // Create Instance Variables
    char character;
    int row;
    int col;
    boolean isBlack;

    /**
     * Constructor.
     * @param character     The character representing the piece.
     * @param row           The row on the board the piece occupies.
     * @param col           The column on the board the piece occupies.
     * @param isBlack       The color of the piece.
     */
    public Piece(char character, int row, int col, boolean isBlack) {
        this.character = character;
        this.row = row;
        this.col = col;
        this.isBlack = isBlack;
    }

    /**
     * Determines if moving this piece is legal.
     * @param board     The current state of the board.
     * @param endRow    The destination row of the move.
     * @param endCol    The destination column of the move.
     * @return If the piece can legally move to the provided destination on the board.
     */
    public boolean isMoveLegal(Board board, int endRow, int endCol) {
        switch (this.character) {
            case '\u2659':
            case '\u265f':
                Pawn pawn = new Pawn(row, col, isBlack);
                return pawn.isMoveLegal(board, endRow, endCol);
            case '\u2656':
            case '\u265c':
                Rook rook = new Rook(row, col, isBlack);
                return rook.isMoveLegal(board, endRow, endCol);
            case '\u265e':
            case '\u2658':
                Knight knight = new Knight(row, col, isBlack);
                return knight.isMoveLegal(board, endRow, endCol);
            case '\u265d':
            case '\u2657':
                Bishop bishop = new Bishop(row, col, isBlack);
                return bishop.isMoveLegal(board, endRow, endCol);
            case '\u265b':
            case '\u2655':
                Queen queen = new Queen(row, col, isBlack);
                return queen.isMoveLegal(board, endRow, endCol);
            case '\u265a':
            case '\u2654':
                King king = new King(row, col, isBlack);
                return king.isMoveLegal(board, endRow, endCol);
            default:
                return false;
        }
    }

    /**
     * Sets the position of the piece.
     * @param row   The row to move the piece to.
     * @param col   The column to move the piece to.
     */
    public void setPosition(int row, int col) {
        this.row = row;
        this.col = col;
    }

    /**
     * Return the color of the piece.
     * @return  The color of the piece.
     */
    public boolean getIsBlack() {
        return this.isBlack;
    }

    /**
     * Handle promotion of a pawn.
     * @param row Current row of the pawn
     * @param isBlack Color of the pawn
     */
    public void promotePawn(int row, boolean isBlack) {
        Character[] pieceChars = {'\u2659', '\u2658', '\u2657', '\u2656', '\u2655', '\u265f', '\u265e','\u265d', '\u265c', '\u265b'};
        String[] pieces = {"Pawn", "Knight", "Bishop", "Rook", "Queen"};
        Scanner s = new Scanner(System.in);
        String newPiece;
        if ((this.character=='\u2659' || this.character=='\u265f') &&((row==7 && (isBlack)) || ((row==0 && !(isBlack))))){
            int newIndex=999;
            System.out.println("You've Promoted Your Pawn!");
            System.out.println("Which Piece Would You Like?(Not King) ");
            newPiece=s.nextLine();
            for (int i=0; i<5; i++){
                if (newPiece.equals(pieces[i])){
                    newIndex=i;
                }
            }
            if (isBlack){
                newIndex+=5;
            }
            this.character=pieceChars[newIndex];
        }
    }


    /**
     * Returns a string representation of the piece.
     * @return  A string representation of the piece.
     */
    public String toString() {
        return Character.toString(this.character);
    }


}
