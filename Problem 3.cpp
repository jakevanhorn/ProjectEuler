#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	long int number1 = 600851475143;
    bool prime = false;
    for (long int a = (number1 - 1); a > 1; a--)
    {
        if (number1 % a == 0)
        {
            for (long int b = (a-1); b >= 1; b--)
            {
                if (b == 1)
                {
                    prime = true;
                    break;
                }
                if (a % b == 0)
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
