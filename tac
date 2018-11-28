#include <iostream>
#include <string>
using namespace std;

void expenses() {
	char cost[4][25];
	cout << "Enter the Costs:" << endl;

	for (int i = 0; i <= 4; i++)
	{
		cout << "Expense" << i + 1 << ": ";
		cin >> cost[i];

	}
	//display costs
	/*for (int j=0;j<=5;j++)
	{
		cout<<cost[j]<<endl;
	} */
}

void income(){
  int myincome;
  string mystatus;
	cout << "Are your depedent or independent: ";
	cin >> mystatus;

	cout << "Enter your total income: ";
	cin >> myincome;

}

int allocateExpenses(){

}

string advisor(){

}

int average(){

}

int main() {
	expenses();
  income();
	return 0;
}
