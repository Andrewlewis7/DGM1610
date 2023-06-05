using System;

public class Program
{
    public static void Main()
    {
        Operations myOperator = new Operations();

        Console.WriteLine("Please enter your exam score as a percentage."); //writes a message to the console
        int score = int.Parse(Console.ReadLine()); //reads user input
        myOperator.CheckScore(score);//calls the function CheckScore
    }
}

public class Operations 
{
    public void CheckScore(int score) //void function that uses an if-else checker for the different scores and outputs a message. 
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
            Console.WriteLine("Your grade is a C. Atleast you're passing.");
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



// Temperature Adviser
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
//         if (temp > 30)
//         {
//             Console.WriteLine("Please stay hydrated and avoid staying in the sun for too long.");
//         }
//         else
//         {
//             Console.WriteLine("Consider enjoying the pleasant weather. I.E. go touch grass....");
//         }
//     }
// }






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











// using System;

// public class Program
// {
//     public static void Main()
//     {
//         public Operations myOperator;

//         Console.WriteLine("Welcome");
        
//         myOperator.DoMath(10, 4);
//         myOperator.Compare(4,5);
//         myOperator.CheckPassword(234234);
//     }
// }

// public class Operations 
// {
//     public static void DoMath(int value, int value2)
//     {
//         var number = value + value2;
//         Console.WriteLine(number);
//     }

//     public static void Compare(int value, int value2)
//     {
//         if(value > value2)
//         {
//             Console.WriteLine("True, the first is greater.");
//         }
//         else
//         {
//             Console.WriteLine("False, the second is greater.");
//         }
//     }

//     public static void CheckPassword (string password)
//     {
//         if(password == "89345")
//         {
//             Console.WriteLine("Correct Password");
//         }
//         else
//         {
//             Console.WriteLine("Incorrect Password");
//         }
//     } 
// }
