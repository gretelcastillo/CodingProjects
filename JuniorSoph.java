package exam;

// class JuniorSoph is a subclass of Student
public class JuniorSoph extends Student
{
	// Has a String instance variable studentID
	private String studentID;
	
	// Has a single constructor with an int parameter indicating the arrivalTime, and a AdvisingType parameter
	// advT referring to a AdvisingType
	public JuniorSoph(int arrivalTime, AdvisingType advT)
	{
		// Calls super with arrivalTime as the parameter
		super(arrivalTime);
		
		// Calls setStudentType with “JuniorSoph ” as the parameter
		setStudentType("JuniorSoph");
		
		// Calls setAdvisingType with advT as the parameter
		setAdvisingType(advT);
		
		// Calls setStudentID with no parameters
		setStudentID();
	}
	
	// setStudentID has no parameters and a void return – this is an override of the abstract method
	// setStudentID
	public void setStudentID()
	{
		// It increments the static variable idCounter declared in Student
		idCounter++;
		
		// It sets studentID to the concatenation of “CSUDH ”, the studentType, and the Student.idCounter
		studentID = "CSUDH " + getStudentType() + " " + idCounter;
	}
	
	// There is a normal accessor getStudentID that overrides the abstract version of this method
	public String getStudentID()
	{
		return studentID;
	}
	
	// compareTo has a reference to a Student as a parameter and returns an int - this is an override of the
	// abstract method in Student
	public int compareTo(Student otherStudent)
	{
		// Returns an int based on a reversal of the natural order for the String studentType. (i.e. Senior will
		// precede JuniorSoph which precedes Freshman.)
		return otherStudent.getStudentType().compareTo(getStudentType());
	}
}
