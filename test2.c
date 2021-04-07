// #include<stdio.h>

// void main(){
//     int numbers[]={2,5,1,3,4};
//     for(int i=0;i<5;i++){
//         for(int j=1;j<5;j++){
//             if (numbers[i]>numbers[j])
//             {
//                 int min=j;
//             }
//             int temp=numbers[i];
//             numbers[i]=numbers[min];
//             numbers[min]=temp;
//         }
//     }
//     // for(int i=0;i<5;i++){
//     //     printf("\n numbers is=%d",numbers[i]);
//     // }
// }

// #include<stdio.h>
// int main(){
//     int n= 'a'/'a';
    
//     printf("%d",n);
//     return 0;
// }


#include<stdio.h>
int main(){
    int n;
    
    printf("\n enter the size of array:");
    scanf("%d",&n);
    int a[n];

    for(int i=0;i<n;i++){
        printf("\n enter element in array: ");
        scanf("%d",&a[i]);
    }

    int counter =1;
    while (counter<n)
    {
        for(int i=0;i<n-counter;i++){
            if(a[i]>a[i+1]){
                int temp=a[i];
                a[i]=a[i+1];
                a[i+1]=temp;
            }
        }
        counter++;
    }
    

    for (int i = 0; i < n; i++)
    {
        printf("\n %d",a[i]);
    }
    
}