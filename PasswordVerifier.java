package password;

public class PasswordVerifier 
{
	// Verifies password entered is at least six characters long
	public static boolean isLengthValid(String password)
	{
		return password.length() >= 6;
	}
	
	// Verfies if password contains one uppercase letter
	public static boolean containsUpperCase(String password)
	{
		for(char ch : password.toCharArray())
		{
			if(Character.isUpperCase(ch))
			{
				return true;
			}
		}
		
		return false;
	}
	
	// Verifies password contains one lowercase letter
	public static boolean containsLowerCase(String password)
	{
		for(char ch : password.toCharArray())
		{
			if(Character.isLowerCase(ch))
			{
				return true;
			}
		}
		
		return false;
	}
	
	// Verifies password contains at least one digit
	public static boolean containsDigit(String password)
	{
		for(char ch : password.toCharArray())
		{
			if(Character.isDigit(ch))
			{
				return true;
			}
		}
		
		return false;
	}
}
