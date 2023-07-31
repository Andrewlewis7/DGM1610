using UnityEngine;
using System.Collections;

public class EnableComponents : MonoBehaviour
{
    private Light myLight;
    
    // so If i start a project it will take like 5 years to create because my friends wifi is so slow. Do you want to create one and I can clone your github. sounds good
    // sure, but in eed to restart my pc rq. brb
    void Start ()
    {
        myLight = GetComponent<Light>();
    }
    
    
    void Update ()
    {
        if(Input.GetKeyUp(KeyCode.Space))
        {
            myLight.enabled = !myLight.enabled;
        }
    }
}