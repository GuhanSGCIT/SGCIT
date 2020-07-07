#include <iostream>

#include<math.h>

using namespace std;

int main()

{

   int n;

   cin>>n;

   int arr[n][3];

   for(int i=0;i<n;i++)

   {

       cin>>arr[i][0]>>arr[i][1]>>arr[i][2];

   }

   float dis[n];

   for(int i=0;i<n;i++)

   {

       int x=arr[i][0]*arr[i][0];

       int y=arr[i][1]*arr[i][1];

       dis[i]=sqrt(x+y);

   }

   int count=0;

   for(int i=0;i<n;i++)

   {

       for(int j=i+1;j<n;j++)

       {

           if(dis[i]/arr[i][2]==dis[j]/arr[j][2])

               count++;

       }

   }

   cout<<count;

   return 0;

}
