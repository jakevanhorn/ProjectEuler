#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    long int number1 = 13195;
    bool prime = false;
    for (long int a = (number1 - 1); a > 0; a--)
    {
        if (number1 % a == 0)
        {
            for (long int b = a; b >= 1; b--)
            {
                if (b == 1)
                {
                    prime = true;
                    break;
                }
                if (b % a == 0)
                {
                    break;
                }

            }
        }
        if (prime == true)
        {
            return a;
            break;
        }
    }
}
