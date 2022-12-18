// #include<stdio.h>
// void roman(int year);
// int main()
// {

//     int year;
//     printf("Enter year: ");
//     scanf("%d", &year);
//     roman(year);

// }

// void roman(int year)
// {
//     if(year>=1000)
//     {
//         printf("M");
//         roman(year-1000);
//     }
//     else if(year>=500)
//     {
//         printf("D");
//         roman(year-500);
//     }
//     else if(year>=100)
//     {
//         printf("C");
//         roman(year-100);
//     }
//     else if(year>=50)
//     {
//         printf("L");
//         roman(year-50);
//     }
//     else if(year>=10)
//     {
//         printf("X");
//         roman(year-10);
//     }
//     else if(year>=5)
//     {
//         printf("V");
//         roman(year-5);
//     }
//     else if(year>=1)
//     {
//         printf("I");
//         roman(year-1);
//     }
// }




#include<stdio.h>
#include<stdlib.h>
int main()
{
    int Roman(int,int,char[],char[],char[]);
    static unsigned year;
    static short choice;
    do
    {
        printf("\n=====================");
        printf("\nRoman Equivalent of Years\n");
        printf("=====================\n");
        printf("\nEnter a year: ");
        scanf("%u",&year);
        if(year>399999)
            printf("\nRange beyond the limit [0,400K)\n");
        else if(year==0)
            printf("N");
        else
        {
            year=Roman(year,100000,"C'","","");
            year=Roman(year,10000,"X'","L'","C'");
            year=Roman(year,1000,"M","V'","X'");
            year=Roman(year,100,"C","D","M");
            year=Roman(year,10,"X","L","C");
            year=Roman(year,1,"I","V","X");
        }
        printf("\nYour Choice\nPress 1 to Run Again\nPress other No. to Exit\t");
        scanf("%hd",&choice);
    }while(choice==1);
    return 0;
}
//--------------------------------------
int Roman(int year, int div, char a[], char b[], char c[])
{
    register short unsigned rem,i;
    rem=year/div;
    if(rem==9)
    {
        printf("%s%s",a,c);
        rem=rem-9;
    }
    else if(rem==4)
    {
        printf("%s%s",a,b);
        rem=rem-4;
    }
    else if(rem>=5)
    {
        printf("%s",b);
        rem=rem-5;
    }
    if(rem!=0)
        for(i=1;i<=rem;i++)
            printf("%s",a);
    return (year%div);
}
//--------------------------------------