/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tictactoe;

// Design a program to play Tic Tac Toe. The game should allow the User to select the size of the board (i.e. 3 X 3, or 6 X 6, etc.) and 
// whether they'd like to select 'X' or 'O'. The points for the project will be broken up as follows:

// The board is displayed correctly (5 points)
// The User's selection is displayed and updated correctly (5 points)
// The Computer's selection is displayed and updated correctly (5 points)
// A winner is detected immediately and correctly (5 points)
// Partial credit will be available for this project based on how many features you implemented. Good luck!

import java.util.Scanner;
import java.util.Random;

public class TicTacToeGame 
{

    public static char inputComputerSymbol = ' ';
    public static char inputPlayerSymbol = ' ';
    
    
    public static void main(String[] args) 
    {
        Scanner keyboard = new Scanner(System.in);
		
		char[][] board = {{' ',' ', ' '}, 
			          {' ', ' ', ' '}, 
				  {' ', ' ', ' '}};
		
		printBoard(board);
                
                System.out.println("Enter a symbol (X or O): ");
                char chosenSymbol = keyboard.next().charAt(0);
                
                getChosenSymbol(chosenSymbol);
                if(getChosenSymbol(chosenSymbol) == ('X'))
                {
                    inputComputerSymbol = 'O';
                    inputPlayerSymbol = 'X';
                }
                else
                {
                    inputComputerSymbol = 'X';
                    inputPlayerSymbol = 'O';
                }
                
		keyboard.nextLine();
                
		while(true) 
		{
			playerTurn(board, keyboard);
			if (isGameFinished(board))
			{
				break;
			}
			printBoard(board);
			computerTurn(board);
			if (isGameFinished(board))
			{
				break;
			}
			printBoard(board);
		}
		
		
		
		
		keyboard.close();
    }
    
    public static boolean isGameFinished(char[][] board)
	{
		if (hasContestantWon(board, inputPlayerSymbol))
		{
			printBoard(board);
			System.out.println("Player wins!");
			return true;
		}
		
		if (hasContestantWon(board, inputComputerSymbol))
		{
			printBoard(board);
			System.out.println("Computer wins!");
			return true;
		}
		
		
		
		
		for(int i = 0; i < board.length; i++)
		{
			for(int j = 0; j < board[i].length; j++)
			{
				if (board[i][j] == ' ')
				{
					return false;
				}
			}
		}
		
		printBoard(board);
		System.out.println("The game ended in a tie!");
		return true;
	}

	public static boolean hasContestantWon(char[][] board, char symbol) 
	{
		if((board[0][0] == symbol && board[0][1] == symbol && board[0][2] == symbol) ||
		   (board[1][0] == symbol && board[1][1] == symbol && board[1][2] == symbol) ||
		   (board[2][0] == symbol && board[2][1] == symbol && board[2][2] == symbol) ||
		   
		   (board[0][0] == symbol && board[1][0] == symbol && board[2][0] == symbol) ||
		   (board[0][1] == symbol && board[1][1] == symbol && board[2][1] == symbol) ||
		   (board[0][2] == symbol && board[1][2] == symbol && board[2][2] == symbol) ||
		   
		   (board[0][0] == symbol && board[1][1] == symbol && board[2][2] == symbol) ||
		   (board[0][2] == symbol && board[1][1] == symbol && board[2][0] == symbol))
		{
			
			return true;
		}
		return false;
	}
	
	
	public static void computerTurn(char[][] board) 
	{
		Random rand = new Random();
		int computerMove;
		
		while(true)
		{
			computerMove = rand.nextInt(9) + 1;
			if(isValidMove(board, Integer.toString(computerMove)))
			{
				break;
			}
			
			
		}
		System.out.println("Computer chose " + computerMove);
		placeMove(board, Integer.toString(computerMove), inputComputerSymbol);
	}
	
	public static boolean isValidMove(char[][] board, String position)
	{
		switch(position)
		{
		case "1":
			return ( board[0][0] == ' ');
		case "2":
			return ( board[0][1] == ' ');
		case "3":
			return ( board[0][2] == ' ');
		case "4":
			return ( board[1][0] == ' ');
		case "5":
			return ( board[1][1] == ' ');
		case "6":
			return ( board[1][2] == ' ');
		case "7":
			return ( board[2][0] == ' ');
		case "8":
			return ( board[2][1] == ' ');
		case "9":
			return ( board[2][2] == ' ');
		default:
			return false;	
			
		}
	}

	public static void playerTurn(char[][] board, Scanner keyboard) 
	{
		String userInput;
		while(true) 
		{
		
		System.out.println("Where would you like to play? (1-9) ");
		userInput = keyboard.nextLine();
		if (isValidMove(board, userInput)) 
		{
			break;
		}
		else
		{
			System.out.println(userInput + " is not a valid move.");
		}
		
		
		}
		
		placeMove(board, userInput, inputPlayerSymbol);
	}

	public static void placeMove(char[][] board, String position, char symbol) 
	{
		switch(position)
		{
		case "1":
			board[0][0] = symbol;
			break;
		case "2":
			board[0][1] = symbol;
			break;
		case "3":
			board[0][2] = symbol;
			break;
		case "4":
			board[1][0] = symbol;
			break;
		case "5":
			board[1][1] = symbol;
			break;
		case "6":
			board[1][2] = symbol;
			break;
		case "7":
			board[2][0] = symbol;
			break;
		case "8":
			board[2][1] = symbol;
			break;
		case "9":
			board[2][2] = symbol;
			break;
		default:
			System.out.println(":(");	
			
		}
	}

	public static void printBoard(char[][] board) 
	{
		System.out.println(board[0][0] + "|" + board[0][1] + "|" + board[0][2]);
		System.out.println("-+-+-");
		System.out.println(board[1][0] + "|" + board[1][1] + "|" + board[1][2]);
		System.out.println("-+-+-");
		System.out.println(board[2][0] + "|" + board[2][1] + "|" + board[2][2]);
	}
        
        public static char getChosenSymbol(char c)
        {
            return c;
        }
       
}
