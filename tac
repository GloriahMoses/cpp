// #include "pch.h"
#include <iostream>
#include <string>
using namespace std;

string expense[5], status;
int myincome, spend[5], totalExpenses = 0;
double percentage, pweeklyExpenses;

string expenses() 
{   
  cout<< "Enter your weekly five expenses below." <<endl; 
    for (int i = 0; i <= 4; i++)
    {
      cout << "Expense " << i + 1 << ": ";
      cin >> expense[i];
      }

    return "0";
}

void income() 
{
    cout << "Enter 'd' for Dependent or 'i' for Independent: ";
    cin >> status;

    if (status != "d" && status != "i") {
        throw "Unknown status!";
    }

    cout << "Enter Weekly Income: ";
    cin >> myincome;

    if (myincome <= 0) {
        throw "income not enough";
    }
}

string allocateExpenses() {
    
    cout << "Cost of " + expense[0] + ": ";
    cin >> spend[0];
    totalExpenses = totalExpenses + spend[0];
    percentage = (spend[0] *100)/myincome;
    cout <<expense[0] <<" - Kshs."<<spend[0] <<"("<<percentage <<"%"<<" of the total income)"<<endl;

    cout << "Cost of " + expense[1] + ": ";
    cin >> spend[1];
    totalExpenses = totalExpenses + spend[1];
    percentage = (spend[1] *100)/myincome;
    cout <<expense[1] <<" - Kshs."<<spend[1] <<"("<<percentage <<"%"<<" of the total income)"<<endl;

    cout << "Cost of " + expense[2] + ": ";
    cin >> spend[2];
    totalExpenses = totalExpenses + spend[2];
    percentage = (spend[2] *100)/myincome;
    cout <<expense[2] <<" - Kshs."<<spend[2] <<"("<<percentage <<"%"<<" of the total income)"<<endl;

    cout << "Cost of " + expense[3] + ": ";
    cin >> spend[3];
    totalExpenses = totalExpenses + spend[0];
    percentage = (spend[3] *100)/myincome;
    cout <<expense[3] <<" - Kshs."<<spend[0] <<"("<<percentage <<"%"<<" of the total income)"<<endl;

    cout << "Cost of " + expense[4] + ": ";
    cin >> spend[4];
    totalExpenses = totalExpenses + spend[4];
    percentage = (spend[4] *100)/myincome;
    cout <<expense[4] <<" - Kshs."<<spend[0] <<"("<<percentage <<"%"<<" of the total income)"<<endl;

    if (totalExpenses > myincome) {
        throw "income is less!";
    }
    return "0";
}

void advisor() {
  cout<<"Total expenses: " <<totalExpenses <<endl;
  pweeklyExpenses = (totalExpenses * 100)/myincome;
  

}

void average() {

}

int main()
{   
    expenses();
    income();
    allocateExpenses();
    advisor();
    average();

    return 0;
}
