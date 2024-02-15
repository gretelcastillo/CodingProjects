package exam;
import java.util.*;
import java.io.*;

public class ModelAdvisingCenter 
{

	public static void main(String[] args) throws IOException
	{
		// Create a Scanner to read keyboard input
		Scanner keyboard = new Scanner(System.in);
		
		// Request and read in the department name at the AdvisingCenter ( using nextLine()), a seed, and the
		// number of Advisors
		// department name at the AdvisingCenter 
		System.out.println("Please enter the name of the department at the Advising Center at CSUDH:");
		String departmentName = keyboard.nextLine();
		
		// seed
		System.out.println("Please enter a seed value as an int:");
		int seed = keyboard.nextInt();
		
		// number of Advisors
		System.out.println("Please enter the number of advisors as an int:");
		int numAdvisors = keyboard.nextInt();
		
		// Create a new AdvisingCenter with those 3 values as parameters (see below)
		AdvisingCenter advisingCenter = new AdvisingCenter(departmentName, seed, numAdvisors);
		
		// Call openAdvisingCenter for the just created AdvisingCenter with no parameters
		advisingCenter.openAdvisingCenter();
		
		System.out.println("Please enter the number of minutes to keep the Advising Center open:");
		int durationForArriving = keyboard.nextInt();
		
		// Call operateAdvisingCenter for the AdvisingCenter created with durationForArriving in minutes as the
		// parameter
		advisingCenter.operateAdvisingCenter(durationForArriving);
		
		System.out.println("Please enter the name of the output file for Advising Center results:");
		String outputFile = keyboard.next();
		
		// Call generateAdvisingCenterResults for the AdvisingCenter created with the name of the output file as a
		// parameter
		advisingCenter.generateAdvisingCenterResults(outputFile);
		
	}

}
