package exam;

public class Advisor 
{
	// Has a static int variable advisorCounter set to 0
	private static int advisorCounter = 0;
	
	// Has the boolean instance value isFree
	private boolean isFree;
	
	// Has the int instance values advisorIDNumber, totalStudentsSeenByAdvisor, timeRemainingForMeeting,
	private int advisorIDNumber;
	private int totalStudentsSeenByAdvisor;
	private int timeRemainingForMeeting;
	
	// Has the reference variable assignedStudent of type Student
	private Student assignedStudent;
	
	// Has a single default constructor
	public Advisor()
	{
		// Calls setAdvisorIDNumber with no parameters
		setAdvisorIDNumber();
		
		// Calls setIsFree with true as the value of the parameter
		setIsFree(true);
	}
	
	// setAdvisorIDNumber has no parameters and a void return
	public void setAdvisorIDNumber()
	{
		// It increments the advisorCounter by 1
		advisorCounter++;
		
		// It sets the advisorIDNumber equal to the advisorCounter
		advisorIDNumber = advisorCounter;
	}
	
	// There are simple accessor (getXXX) methods for each of the five instance variables
	public int getAdvisorIDNumber()
	{
		return advisorIDNumber;
	}
	
	// setIsFree has a boolean parameter and a void return
	public void setIsFree(boolean free)
	{
		isFree = free;
	}
	
	// There are simple accessor (getXXX) methods for each of the five instance variables
	public boolean getIsFree()
	{
		return isFree;
	}
	
	// setAssignedStudent has a reference to a Student as the parameter and a void return
	public void setAssignedStudent(Student student)
	{
		// It sets the reference variable assignedStudent to the value of the parameter
		assignedStudent = student;
		
		// It calls setIsFree with false as the parameter
		setIsFree(false);
	}
	
	// There are simple accessor (getXXX) methods for each of the five instance variables
	public Student getAssignedStudent()
	{
		return assignedStudent;
	}
	
	// removeAssignedStudent has no parameters and returns a reference to the assignedStudent
	public Student removeAssignedStudent()
	{
		// Create a temporary Student reference variable tempStudent equal to the current assignedStudent
		// for this Advisor
		Student tempStudent = assignedStudent;
		
		// Set the assignedStudent variable to null
		assignedStudent = null;
		
		// Call setIsFree with the parameter true
		setIsFree(true);
		
		// Increment totalStudentsSeenByAdvisor by 1
		totalStudentsSeenByAdvisor++;
		
		// Return the value in the tempStudent reference variable
		return tempStudent;
	}
	
	// setTimeRemainingForMeeting has an int parameter and a void return
	public void setTimeRemainingForMeeting(int timeRemainingForMeeting)
	{
		// set timeRemainingForMeeting to the value of the parameter
		this.timeRemainingForMeeting = timeRemainingForMeeting;
	}
	
	// There are simple accessor (getXXX) methods for each of the five instance variables
	public int getTimeRemainingForMeeting()
	{
		return timeRemainingForMeeting;
	}
	
	// decrementTimeRemainingForMeeting has no parameters and a void return
	public void decrementTimeRemainingForMeeting()
	{
		// It decrements timeRemainingForMeeting by 1
		timeRemainingForMeeting--;
	}
	
	// There are simple accessor (getXXX) methods for each of the five instance variables
	public int getTotalStudentsSeenByAdvisor()
	{
		return totalStudentsSeenByAdvisor;
	}
	
	// toString has no parameters and returns a String – (normal override)
	public String toString()
	{
		return "Advisor " + advisorIDNumber + " advises " + totalStudentsSeenByAdvisor + " students";
	}
}
