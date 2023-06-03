using System;

public class Program
{
    public static Homework statistics;

    public static void Main()
    {
        statistics = new Homework();


        Console.Write("Enter number of assignments: "); // asks for the number of assignments
        statistics.numberCountForAssignments = int.Parse(Console.ReadLine());


        Console.Write("Enter number of days till due: ");  // asks for the number of days till due
        statistics.numberCountDaysTillDue = float.Parse(Console.ReadLine());


        if (statistics.numberCountForAssignments > 0 && statistics.numberCountDaysTillDue > 0) //if conditional to say a total for each catagory or that there are no days/assigments left. 
        {
            Console.WriteLine("You have " + statistics.numberCountForAssignments + " assignments left and " + statistics.numberCountDaysTillDue + " days to submit.");
        }
        else
        {
            Console.WriteLine("No assignments left or no days left to submit. You might be screwed.");
        }
    }
}

public class Homework //created a public class called homework that tracks assignments and days till due. also declared several variables
{
    public int numberCountForAssignments = 2;
    public string homeworkName = "math";
    public float numberCountDaysTillDue = 2.0f;
}
