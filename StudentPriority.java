package exam;
import java.util.Comparator;

public class StudentPriority implements Comparator<Student>
{
	public int compare(Student student1, Student student2)
	{
		if(student1.getStudentType().equals(student2.getStudentType()))
		{
			return Integer.compare(student1.getArrivalTimeAtAdvisingCenter(), student2.getArrivalTimeAtAdvisingCenter());
		}
		else
		{
			return student1.compareTo(student2);
		}
	}
	
	
}
