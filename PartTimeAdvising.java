package exam;

// class PartTimeAdvising is a subclass of AdvisingType
public class PartTimeAdvising extends AdvisingType 
{
	// Has a static int variable partTimeCounter initialized to 0.
	private static int partTimeCounter = 0;
	
	// Has an instance variable String advisingNumber
	private String advisingNumber;
	
	// Has a single constructor with no parameters
	public PartTimeAdvising()
	{
		// Calls super with the parameter value “PartTime”
		super("PartTime");
		
		// Calls setAdvisingNumber with no parameters
		setAdvisingNumber();
	}
	
	// Overrides the method setAdvisingNumber:
	public void setAdvisingNumber()
	{
		// Increments partTimeCounter by 1
		partTimeCounter++;
		
		// Sets the advisingNumber equal to the concatenation of “PartTime ” and partTimeCounter
		advisingNumber = "PartTime " + partTimeCounter;
	}
	
	// Overrides the method getAdvisingNumber
	public String getAdvisingNumber()
	{
		// returns the reference to the String referred to by advisingNumber
		return advisingNumber;
	}
}
