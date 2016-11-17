#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int a = 1;
    int b = 2;
    int b2 = 0;
    int sum = 0;

    while (b <= 4000000)
    {
        if (b % 2 == 0)
        {
            cout << b << endl;
            sum += b;
        }
        b2 = b;
        b += a;
        a = b2;

    }

    return sum;
}
