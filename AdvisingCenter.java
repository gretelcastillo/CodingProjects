package exam;
import java.util.*;
import java.io.*;

public class AdvisingCenter 
{
	
	// A Random variable randy
	private Random randy;
	
	// A PriorityQueue of type Student called waitingQ
	private PriorityQueue<Student> waitingQ;
	
	// An ArrayList of type Student called processedStudents
	private ArrayList<Student> processedStudents;
	
	// An array of type Advisor called advisors
	private Advisor[] advisors;
	
	// A String variable deptName
	private String deptName;
	
	// An int variable currentTime set to 0
	private int currentTime = 0;
	
	// It has a single constructor with three parameters: String name, int seed, int numAdvisors
	public AdvisingCenter(String name, int seed, int numAdvisors)
	{
		// It simple sets deptName to name (You can do this without calling a mutator)
		deptName = name;
		
		// It creates the waitingQ object using a new instance of StudentPriority as the parameter, ensuring
		// that waitingQ prioritizes according to StudentPriority rules
		waitingQ = new PriorityQueue<>(new StudentPriority());
		
		// It creates a Random object called randy based on the seed
		randy = new Random(seed);
		
		this.processedStudents = new ArrayList<>();
		
		// It calls createAdvisors with numAdvisors as the parameter
		createAdvisors(numAdvisors);
	}
	
	// createAdvisors has a single int parameter called numAdvisors and a void return
	public void createAdvisors(int numAdvisors)
	{
		// It creates the advisor array with a length equal to the value of numAdvisors
		advisors = new Advisor[numAdvisors];
		
		// For each reference in the array it creates an Advisor (Remember that the Advisor constructor has
		// no parameters)
		for(int i = 0; i < numAdvisors; i++)
		{
			advisors[i] = new Advisor();
		}
	}
	
	// openAdvisingCenter has no parameters and a void return
	public void openAdvisingCenter()
	{
		
		for(currentTime = 0; currentTime < 10; currentTime++)
		{
			for(int i = 0; i < 10; i++)
			{
				int randomNum = randy.nextInt(1, 31);
				
				if(randomNum < 5)
				{
					waitingQ.add(new Senior(currentTime, new FullTimeAdvising()));
				}
				else if(randomNum < 6)
				{
					waitingQ.add(new Senior(currentTime, new PartTimeAdvising()));
				}
				else if(randomNum < 14)
				{
					waitingQ.add(new JuniorSoph(currentTime, new FullTimeAdvising()));
				}
				else if(randomNum < 16)
				{
					waitingQ.add(new JuniorSoph(currentTime, new PartTimeAdvising()));
				}
				else if(randomNum < 29)
				{
					waitingQ.add(new Freshman(currentTime, new FullTimeAdvising()));
				}
				else
				{
					waitingQ.add(new Freshman(currentTime, new PartTimeAdvising()));
				}
			}
		}
	}
	
	// operateAdvisingCenter has a parameter int called durationForArriving and a void return
	public void operateAdvisingCenter(int durationForArriving)
	{
		// Create an int variable endArrivalsTime and set it equal to the sum of the currentTime and
		// durationForArriving
		int endArrivalsTime = currentTime + durationForArriving;
		
		
		while (processedStudents.size() != Student.idCounter || currentTime < endArrivalsTime) 
		{
	        // Simulate arriving students until the office doors close
	        if (currentTime < endArrivalsTime) 
	        {
	            for (int i = 0; i < 8; i++) 
	            {
	                int randomNum = randy.nextInt(30) + 1;

	                if (randomNum < 6) 
	                {
	                    waitingQ.offer(new Senior(currentTime, new FullTimeAdvising()));
	                } 
	                else if (randomNum < 7) 
	                {
	                    waitingQ.offer(new Senior(currentTime, new PartTimeAdvising()));
	                } 
	                else if (randomNum < 15) 
	                {
	                    waitingQ.offer(new JuniorSoph(currentTime, new FullTimeAdvising()));
	                } 
	                else if (randomNum < 18) 
	                {
	                    waitingQ.offer(new JuniorSoph(currentTime, new PartTimeAdvising()));
	                } 
	                else if (randomNum < 29) 
	                {
	                    waitingQ.offer(new Freshman(currentTime, new FullTimeAdvising()));
	                } 
	                else 
	                {
	                    waitingQ.offer(new Freshman(currentTime, new PartTimeAdvising()));
	                }
	            }
	        }

	        // Check on busy advisors
	        for (Advisor advisor : advisors) 
	        {
	            if (!advisor.getIsFree()) 
	            {
	                advisor.decrementTimeRemainingForMeeting();

	                if (advisor.getTimeRemainingForMeeting() == 0) 
	                {
	                    Student tempStudent = advisor.removeAssignedStudent();
	                    
	                    processedStudents.add(tempStudent);
	                    
	                    tempStudent.setTotalTimeAtAdvisingCenter(currentTime);
	                }
	            }
	        }

	        // Assign students to free advisors
	        for (Advisor advisor : advisors) 
	        {
	            if (advisor.getIsFree() && !waitingQ.isEmpty()) 
	            {
	                Student tempStudent = waitingQ.poll();
	                
	                tempStudent.setAdvisorStartTime(currentTime);
	                
	                advisor.setAssignedStudent(tempStudent);
	                
	                int meetingDuration = randy.nextInt(11) + 10; // Random number from 10 to 20
	                
	                tempStudent.setMeetingDuration(meetingDuration);
	                
	                advisor.setTimeRemainingForMeeting(meetingDuration);
	            }
	        }

	        currentTime++;
	    }
	}
	
	// generateAdvisingCenterResults has a String parameter representing the physical output file and returns
	// a void (remember the throws IOException)
	public void generateAdvisingCenterResults(String outputFile) throws IOException
	{
		PrintWriter writer = new PrintWriter(outputFile);
		
		writer.println("Data for CSUDH Advising Center For " + deptName + " Department\n");
		
		writer.println("Summary Data");
		
		for(int i = 0; i < advisors.length; i++)
		{
			writer.println("Advisor " + (i + 1) + " advises " + advisors[i].getTotalStudentsSeenByAdvisor() + " students");
		}
		
		writer.println();
		
		int totalSeniors = 0, totalJuniorSophs = 0, totalFreshman = 0, totalStudents = processedStudents.size();
		int totalTimeSeniors = 0, totalTimeJuniorSophs = 0, totalTimeFreshman = 0, totalTimeAllStudents = 0;
		
		for(Student student : processedStudents)
		{
			if(student instanceof Senior)
			{
				totalSeniors++;
				
				totalTimeSeniors += student.getTotalTimeAtAdvisingCenter();
			}
			else if(student instanceof JuniorSoph)
			{
				totalJuniorSophs++;
				
				totalTimeJuniorSophs += student.getTotalTimeAtAdvisingCenter();
			}
			else if(student instanceof Freshman)
			{
				totalFreshman++;
				
				totalTimeFreshman += student.getTotalTimeAtAdvisingCenter();
			}
			
			totalTimeAllStudents += student.getTotalTimeAtAdvisingCenter();
		}
		
		writer.printf("The average total time in meeting per student for %d Seniors is %.2f minutes\n", totalSeniors, (double) totalTimeSeniors / totalSeniors);
		writer.printf("The average total time in office per student for %d JuniorSophs is %.2f minutes\n", totalJuniorSophs, (double) totalTimeJuniorSophs / totalJuniorSophs);
		writer.printf("The average total time in office per student for %d Freshman is %.2f minutes\n", totalFreshman, (double) totalTimeFreshman / totalFreshman);
		writer.printf("The average total time in office per student for %d Students is %.2f minutes\n", totalStudents, (double) totalTimeAllStudents / totalStudents);
		writer.println();
		
		writer.printf("%-30s%-30s%-20s%-20s%-20s%-20s%-20s%-20s%n",
				 "STUDENT ID", "STUDENT TYPE", "ADVISING TYPE", "ADVISING NUMBER", "ARRIVAL TIME", "WAIT TIME", "MEETING TIME", "TOTAL TIME");
		
		for(Student student : processedStudents)
		{
			writer.printf("%-30s%-30s%-20s%-20s%-20s%-20s%-20s%-20s%n", 
					student.getStudentID(), student.getStudentType(), student.getAdvisingType().getAdvisingType(),
					student.getAdvisingType().getAdvisingNumber(), student.getArrivalTimeAtAdvisingCenter(),
					student.getWaitTime(), student.getMeetingDuration(), student.getTotalTimeAtAdvisingCenter());
		}
		
		writer.close();
	}
}
