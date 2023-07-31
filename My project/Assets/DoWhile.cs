using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoWhile : MonoBehaviour
{
    
    void Start()
    {
        bool shouldContinue = false;

        do
        {
            print("Hello World");
        }
        while (shouldContinue == true);
    }
}

// can you read the file i made?