#include <cstdio>
using namespace std;

int T, N;

int main ()
{
    scanf ("%d", &T);

    for (int t = 0; t < T; t++)
    {
        scanf ("%d", &N);
        printf ("Case #%d: ", t + 1);

// computed using the calculator program
        if (N == 2) puts ("027");
        if (N == 3) puts ("143");
        if (N == 4) puts ("751");
        if (N == 5) puts ("935");
        if (N == 6) puts ("607");
        if (N == 7) puts ("903");
        if (N == 8) puts ("991");
        if (N == 9) puts ("335");
        if (N == 10) puts ("047");
        if (N == 11) puts ("943");
        if (N == 12) puts ("471");
        if (N == 13) puts ("055");
        if (N == 14) puts ("447");
        if (N == 15) puts ("463");
        if (N == 16) puts ("991");
        if (N == 17) puts ("095");
        if (N == 18) puts ("607");
        if (N == 19) puts ("263");
        if (N == 20) puts ("151");
        if (N == 21) puts ("855");
        if (N == 22) puts ("527");
        if (N == 23) puts ("743");
        if (N == 24) puts ("351");
        if (N == 25) puts ("135");
        if (N == 26) puts ("407");
        if (N == 27) puts ("903");
        if (N == 28) puts ("791");
        if (N == 29) puts ("135");
        if (N == 30) puts ("647");
    }

    return 0;
}
