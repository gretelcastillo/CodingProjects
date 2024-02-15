package exam;

// abstract class AdvisingType
public abstract class AdvisingType 
{
	// String advisingType
	private String advisingType;
	
	// There is a single constructor with a single parameter with the advisingType which
	// Calls setAdvisingType with advisingType as the parameter.
	public AdvisingType(String advisingType)
	{
		setAdvisingType(advisingType);
	}
	
	// This class has both a standard mutator and accessor method for advisingType:
	public void setAdvisingType(String advisingType)
	{
		this.advisingType = advisingType;
	}
	
	public String getAdvisingType()
	{
		return advisingType;
	}
	
	// abstract method setAdvisingNumber
	public abstract void setAdvisingNumber();
	
	// abstract method getAdvisingNumber
	public abstract String getAdvisingNumber();
}
