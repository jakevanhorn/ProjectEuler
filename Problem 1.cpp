#include <math.h>

using namespace std;

int main()
{
    int sum = 0;

    for (int a = 1; a < 1000; a++)
    {
        if (a % 3 == 0)
        {
            sum += a;
        }
        else if (a % 5 == 0)
        {
            sum += a;
        }
    }

    return sum;
}
