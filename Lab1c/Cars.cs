using System;

public class Program
{
    public void Main()
    {
        string[] cars = {"Mustang", "Camero", "HellCat", "Corvette", "Viper"};
        Console.WriteLine(cars.Length);
        foreach(var car in cars) 
        {
            Console.WriteLine("I love my " + car + ".");
        }
    }
}
