using System;

public class Program
{
    public static School courses;

    public static void Main()
    {
        Operations myOperator = new Operations(); //created a new instance of operations
        courses = new School(); //created a new object instance of the class School

        Console.WriteLine("Please enter your current subject:");
        string subject = Console.ReadLine(); //takes the input from the console

        courses.currentSubject = (School.Subject)Enum.Parse(typeof(School.Subject), subject); //fancyiness courtesy of chatGTP. Im still figuring out exactly how it works. 
        courses.CheckState(); //calls the function check state 

        Console.WriteLine("Please enter your exam score as a percentage");
        int score = int.Parse(Console.ReadLine());
        myOperator.CheckScore(score);
    }
}

public class School
{
    public enum Subject //the label giver we covered during this unit
    {
        Math,
        Science,
        History,
        Biology,
        Default
    }

    public Subject currentSubject;

    public void CheckState() //void function that uses switch to write different lines to the console 
    {
        switch (currentSubject)
        {
            case Subject.Math:
                Console.WriteLine("Make sure you bring a calculator.");
                break;
            case Subject.Science:
                Console.WriteLine("Science exam? Good luck!");
                break;
            case Subject.History:
                Console.WriteLine("History exam? Study those dates!");
                break;
            case Subject.Biology:
                Console.WriteLine("Biology exam? Remember the life cycles.");
                break;
            case Subject.Default:
                Console.WriteLine("No specific subject selected.");
                break;
        }
    }
}

public class Operations //created a public class to handle checking the score of the user. 
{
    public void CheckScore(int score)
    {
        if (score >= 90 && score <= 100)
        {
            Console.WriteLine("Your grade is an A. Nice.");
        }
        else if (score >= 80 && score < 90)
        {
            Console.WriteLine("Your grade is a B. Try drinking more water.");
        }
        else if (score >= 70 && score < 80)
        {
            Console.WriteLine("Your grade is a C. At least you're passing.");
        }
        else if (score >= 60 && score < 70)
        {
            Console.WriteLine("Your grade is a D. For Dreadful.");
        }
        else
        {
            Console.WriteLine("Your grade is an F. Have you tried studying?");
        }
    }
}























// using System;

// public class Program
// {
//     public GameStates gameStates;

//     public void Main()
//     {
//         gameStates = new GameStates();
//         gameStates.currentState = GameStates.states.Ending;
//         gameStates.CheckState();

//     }
// }

// public class GameStates 
// {
//     public enum States 
//     {
//         Starting,
//         Playing,
//         Ending
//     }
    

//     public States currentState = States.Starting;

//     public void CheckState()
//     {
//         switch (currentState)
//         {
//             case States.Starting:
//                 Console.WriteLine("Starting");
//                 break;
//             case States.Playing:
//                 Console.WriteLine("Playing");
//                 break;
//             case States.Ending:
//                 Console.WriteLine("Ending");
//                 break;
//         }
//     }
// }















//Temperature Adviser
// using System;

// public class Program
// {
//     public static void Main()
//     {
//         Operations myOperator = new Operations();

//         Console.WriteLine("Please enter the current temperature in Celsius.");
//         int temp = int.Parse(Console.ReadLine());
//         myOperator.CheckTemp(temp);
//     }
// }

// public class Operations 
// {
//     public void CheckTemp(int temp)
//     {
//         if (temp >= 30 && temp < 40)
//         {
//             Console.WriteLine("Please stay hydrated and avoid staying in the sun for too long.");
//         }
//         else if (temp >= 20 && temp < 30)
//         {
//             Console.WriteLine("Consider enjoying the pleasent weather.");
//         }
//         else if (temp >= 10 && temp < 20)
//         {
//             Console.WriteLine("It may be a little chilly, consider wearing a jacket.");
//         }
//         else
//         {
//             Console.WriteLine("It is freezing stay inside. Or enter a valid temperature");
//         }
//     }
// }
















