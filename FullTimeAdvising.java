package exam;

// class FullTimeAdvising is a subclass of AdvisingType
public class FullTimeAdvising extends AdvisingType
{
	// Has a static int variable fullTimeCounter initialized to 0.
	private static int fullTimeCounter = 0;
	
	// Has an instance variable String advisingNumber
	private String advisingNumber;
	
	// Has a single constructor with no parameters
	public FullTimeAdvising()
	{
		// Calls super with the parameter value “FullTime ”
		super("FullTime");
		
		// Calls setAdvisingNumber with no parameters
		setAdvisingNumber();
	}
	
	public void setAdvisingNumber()
	{
		// Increments fullTimeCounter by 1
		fullTimeCounter++;
		
		// Sets the advisingNumber equal to the concatenation of “FullTime ” and fullTimeCounter
		advisingNumber = "FullTime" + fullTimeCounter;
	}
	
	// Overrides the method getAdvisingNumber
	public String getAdvisingNumber()
	{
		// returns the reference to the String referred to by advisingNumber
		return advisingNumber;
	}
}

