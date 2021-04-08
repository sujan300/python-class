// #include<stdio.h>
// int main(){
//     int n;
//     printf("\n enter number you want");
//     scanf("%d",&n);
//     for(int i=2;i<n;i++){
//         int count=0;
//         for(int j=2;j<i;j++){
//             if(i%j==0){
//                 count++;
//             }
//         }
//         if(count==0){
//             printf("\n the prime number is=%d",i);
//         }
//     }
//     return 0;
// }


#include<stdio.h>
int main(){
    int n,sumeven,sumodd;
    printf("\n enter number:");
    scanf("%d",&n);
    int a[n];

    for(int i=0; i<n;i++){
        printf("\n enter data in array:");
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        if(a[i]%2==0){
            sumeven=sumeven+a[i];
        }
        else
        {
            sumodd=sumodd+a[i];
        }
        
        
    }

    printf("\n sum of odd is =%d",sumodd);
    printf("\n sum of even number is=%d",sumeven);
    return 0;
}