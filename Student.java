package exam;

public abstract class Student implements Comparable<Student>
{
	// Has a static int variable idCounter set to 0 (Make this public)
	public static int idCounter = 0;
	
	// Has int instance variables arrivalTimeAtAdvisingCenter, advisorStartTime, waitTime, meetingDuration,
	// totalTimeAtAdvisingCenter
	private int arrivalTimeAtAdvisingCenter;
	private int advisorStartTime;
	private int waitTime;
	private int meetingDuration;
	private int totalTimeAtAdvisingCenter;
	
	// Has a AdvisingType instance variable advType
	private AdvisingType advType;
	
	// Has a String instance variable studentType
	private String studentType;
	
	// Has a single constructor with a parameter for arrivalTime
	public Student(int arrivalTime)
	{
		// Calls setArrivalTimeAtAdvisingCenter with the arrivalTime from the constructor as the parameter
		setArrivalTimeAtAdvisingCenter(arrivalTime);
	}
	
	// The mutator method for setArrivalTimeAtAdvisingCenter accepts an int parameter and has a void
	// return
	public void setArrivalTimeAtAdvisingCenter(int arrivalTime)
	{
		// It sets the arrivalTimeAtAdvisingCenter equal to the input parameter value
		arrivalTimeAtAdvisingCenter = arrivalTime;
	}
	
	// There are simple accessor (getXXX) methods for each of the seven instance variables
	public int getArrivalTimeAtAdvisingCenter()
	{
		return arrivalTimeAtAdvisingCenter;
	}
	
	// The mutator method for setMeetingDuration accepts an int parameter and has a void return
	public void setMeetingDuration(int duration)
	{
		// It sets the meetingDuration equal to the input parameter value
		meetingDuration = duration;
	}
	
	// There are simple accessor (getXXX) methods for each of the seven instance variables
	public int getMeetingDuration()
	{
		return meetingDuration;
	}
	
	// The setAdvisorStartTime accepts an int with the advisorStartTime as the parameter and has a void return
	public void setAdvisorStartTime(int advisorStartTime)
	{
		// It sets the advisorStartTime equal to the input parameter
		this.advisorStartTime = advisorStartTime;
		
		// It sets the waitTime as the difference between the advisorStartTime and the
		// arrivalTimeAtAdvisingCenter
		waitTime = advisorStartTime - arrivalTimeAtAdvisingCenter;
	}
	
	// There are simple accessor (getXXX) methods for each of the seven instance variables
	public int getAdvisorStartTime()
	{
		return advisorStartTime;
	}
	
	// The setTotalTimeAtAdvisingCenter method accepts an int with the endTime as a parameter and has a
	// void return
	public void setTotalTimeAtAdvisingCenter(int endTime)
	{
		// It sets the totalTimeAtAdvisingCenter to the difference between the endTime and the
		// arrivalTimeAtAdvisingCenter
		totalTimeAtAdvisingCenter = endTime - arrivalTimeAtAdvisingCenter;
	}
	
	// There are simple accessor (getXXX) methods for each of the seven instance variables
	public int getTotalTimeAtAdvisingCenter()
	{
		return totalTimeAtAdvisingCenter;
	}
	
	// The setAdvisingType method accepts a reference to an AdvisingType as the parameter and has a void
	// return
	public void setAdvisingType(AdvisingType advisingType)
	{
		// It sets advType to the parameter (a reference variable)
		advType = advisingType;
	}
	
	// There are simple accessor (getXXX) methods for each of the seven instance variables
	public AdvisingType getAdvisingType()
	{
		return advType;
	}
	
	// The setStudentType method accepts a String reference to the studentType as the parameter and has a
	// void return
	public void setStudentType(String studentType)
	{
		// It sets studentType to the parameter (a reference variable)
		this.studentType = studentType;
	}
	
	// There are simple accessor (getXXX) methods for each of the seven instance variables
	public String getStudentType()
	{
		return studentType;
	}
	
	// There are simple accessor (getXXX) methods for each of the seven instance variables
	public int getWaitTime()
	{
		return waitTime;
	}
	
	// abstract setStudentID has no parameters and a void return
	public abstract void setStudentID();
	
	// abstract getStudentID has no parameters and returns a String
	public abstract String getStudentID();
	
	// abstract compareTo has a reference to a Student as a parameter and returns an int (this is the method from
	// Comparable, but it is given a body in each of the subclasses)
	public abstract int compareTo(Student otherStudent);
}
