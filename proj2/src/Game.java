// Written by Emmet Hoversten, hover114
import java.util.Scanner;
public class Game {
    public static void main(String[] args) {
        Board gameBoard = new Board();
        System.out.println(gameBoard.verifyDiagonal(0, 1, 4, 5));
        String[] turnShift = {"White", "Black"};
        int turn = 0;
        String[] moves;
        int[] moveList = new int[4];
        Scanner scanner = new Scanner(System.in);
        Fen.load("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", gameBoard);
        while (!gameBoard.isGameOver()) {
            System.out.println(gameBoard);
            System.out.println("It is currently " + turnShift[turn] + "'s turn to play.");
            System.out.println("What is your move?(format: [start row] [start col] [end row] [end col]) ");
            moves = scanner.nextLine().split(" ");
            for (int i = 0; i < 4; i++) {
                moveList[i] = Integer.parseInt(moves[i]);
            }
            if (turn == 0) {
                if (!gameBoard.getPiece(moveList[0], moveList[1]).getIsBlack()) {
                    gameBoard.movePiece(moveList[0], moveList[1], moveList[2], moveList[3]);
                }
                turn = 1;
            } else {
                if (gameBoard.getPiece(moveList[0], moveList[1]).getIsBlack()) {
                    gameBoard.movePiece(moveList[0], moveList[1], moveList[2], moveList[3]);
                    turn = 0;
                }
            }
            if (turn == 0) {
                System.out.println("White has won the game!");
            } else {
                System.out.println("Black has won the game!");
            }
        }

    }
}