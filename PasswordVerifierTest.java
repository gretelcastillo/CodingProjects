package password;

import java.util.Scanner;

public class PasswordVerifierTest 
{

	public static void main(String[] args) 
	{
		String password;
		
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Enter a Password: ");
		password = keyboard.nextLine();
		
		if(PasswordVerifier.containsUpperCase(password) && PasswordVerifier.containsUpperCase(password)
				&& PasswordVerifier.containsLowerCase(password) && PasswordVerifier.containsDigit(password))
		{
			System.out.println("Password is Valid");
		}
		else
		{
			System.out.println("Password is invalid");
		}

	}

}
