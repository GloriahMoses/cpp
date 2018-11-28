#include <iostream>
#include <string>

using namespace std;

int main(){
    char cost[4][25];
    cout<<"Enter the Costs:"<<endl;
    
    for (int i = 0; i<=4; i++)
    {
        cout<<"Expense"<<i+1<<": ";
        cin>>cost[i];
        
    }
    //display costs
    for (int j=0;j<=5;j++)
    {
        cout<<cost[j]<<endl;
    }
   
}
