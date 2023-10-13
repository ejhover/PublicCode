// Written by Emmet Hoversten, hover114
public class King {
    private int row;
    private int col;
    private boolean isBlack;
    public King (int row, int col, boolean isBlack) {
        this.row = row;
        this.col = col;
        this.isBlack = isBlack;
    }
    public boolean isMoveLegal(Board board, int endRow, int endCol) {
        return (board.verifyAdjacent(this.row, this.col, endRow, endCol) && board.verifySourceAndDestination(this.row, this.col, endRow, endCol, this.isBlack));
    }
}
