#include<stdio.h>

void dec_bin(int num, int a[], int size)
{
	int i;
	for(i=size-1;i>=0;i--)
	{
		a[i]=num%2;
		num=num/2;
	}
}


void main()
{
	int num1=0,num2=0,cin=0,cout=0,intcarry=0;
	int a[4],b[4],s[4];
	printf("Enter number 1(0-15):");
	scanf("%d",&num1);
	printf("Enter number 2(0-15):");
	scanf("%d",&num2);
	printf("Enter Cin(0 or 1) :");
	scanf("%d",&cin);
	dec_bin(num1,a,4);
	dec_bin(num2,b,4);
int j=0;

	s[3]=a[3]+b[3]+cin;
	if(s[3]==2)
	{
		s[3]=0;
		intcarry=1;
	}
	else if(s[3]==3)
	{
		s[3]=1;
		intcarry=1;
	}
	else 
		intcarry=0;
for(j=2;j>=0;j--)
{
	s[j]=a[j]+b[j]+intcarry;
	if(s[j]==2)
	{
		s[j]=0;
		intcarry=1;
	}
	else if(s[j]==3)
	{
		s[j]=1;
		intcarry=1;
	}
	else 
		intcarry=0;
}

printf("Sum : ");
for(int k=0;k<4;k++)
printf("%d",s[k]);
printf("\nCout : %d",intcarry);

}
