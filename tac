
#include <iostream>
#include <string>
using namespace std;

char cost[4][25];
void expenses() {
	cout << "Enter the Costs:" << endl;
	for (int i = 0; i <= 4; i++)
	{
		cout << "Expense" << i + 1 << ": ";
		cin >> cost[i];
	}
}

void income() {
	int myincome;
	string mystatus;
	cout << "Are your depedent or independent: ";
	cin >> mystatus;
	cout << "Enter weekly income: ";
	cin >> myincome;
}

void allocateExpenses() {
	int expenseamt[4];
	for (int i = 0; i <= 4; i++)
	{
		cout << "Kindly enter amount for expense"<< i + 1 << ": ";
		cin >> expenseamt[i];
	}	
}

void advisor() {

}

void average() {

}

int main() {
	expenses();
	income();
	allocateExpenses();
	return 0;
}

/*for (int j = 0; j <= 4; j++)
	{
		//display costs
		for (int j = 0; j <= 5; j++)
		{
			cout << cost[j] << endl;
		}
	}*/
