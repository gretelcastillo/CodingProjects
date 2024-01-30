/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javaapplication126;

import java.util.Scanner;

public class JavaApplication126 
{

    
    public static void main(String[] args) 
    {
        Scanner keyboard = new Scanner(System.in);
        
        double test1;
        double test2;
        double test3;
        
        System.out.println("Enter your score for test 1: ");
        test1 = keyboard.nextDouble();
        
        System.out.println("Enter your score for test 2: ");
        test2 = keyboard.nextDouble();
        
        System.out.println("Enter your score for test 3: ");
        test3 = keyboard.nextDouble();
        
        calcAverage(test1, test2, test3);
        
        
    }
    
    public static void calcAverage(double exam1, double exam2, double exam3)
    {
        double average;
        
        // Don't know the math to calculate the average of scores.
        average = (exam1 + exam2 + exam3)/100;
        
        System.out.println("The average score after inputting your scores is " + average);
        
        determineGrade(exam1, exam2, exam3);
    }
    
    public static void determineGrade(double score1, double score2, double score3)
    {
      
      // Exam 1 Grade Determination
      if (score1 >= 90 && score1 <= 100)  
      {
          System.out.println("Your score for exam 1 is an A.");
      }
      else if( score1 >= 80 && score1 <= 89)
      {
          System.out.println("Your score for exam 1 is a B.");
      }
      else if(score1 >= 70 && score1 <= 79)
      {
          System.out.println("Your score for exam 1 is a C.");
      }
      else if(score1 >= 60 && score1 <= 69)
      {
          System.out.println("Your score for exam 1 is a D.");
      }
      else
      {
          System.out.println("Your score for exam 1 is an F.");
      }
      
      
      // Exam 2 Grade Determination
      if (score2 >= 90 && score2 <= 100)  
      {
          System.out.println("Your score for exam 2 is an A.");
      }
      else if( score2 >= 80 && score2 <= 89)
      {
          System.out.println("Your score for exam 2 is a B.");
      }
      else if(score2 >= 70 && score2 <= 79)
      {
          System.out.println("Your score for exam 2 is a C.");
      }
      else if(score2 >= 60 && score2 <= 69)
      {
          System.out.println("Your score for exam 2 is a D.");
      }
      else
      {
          System.out.println("Your score for exam 2 is an F.");
      }
      
      
      // Exam 3 Grade Determination
      if (score3 >= 90 && score3 <= 100)  
      {
          System.out.println("Your score for exam 3 is an A.");
      }
      else if( score3 >= 80 && score3 <= 89)
      {
          System.out.println("Your score for exam 3 is a B.");
      }
      else if(score3 >= 70 && score3 <= 79)
      {
          System.out.println("Your score for exam 3 is a C.");
      }
      else if(score3 >= 60 && score3 <= 69)
      {
          System.out.println("Your score for exam 3 is a D.");
      }
      else
      {
          System.out.println("Your score for exam 3 is an F.");
      }
      
    }
    
}
