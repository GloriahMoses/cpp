// salary.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
using namespace std;

int main()
{
	float percentage_bonus, basic_salary, bonus, gross_salary;
	char str;
	cout << "Enter your job group category:";
	cin >> str;


	if (str == 'a') {
		basic_salary = 10000;
		percentage_bonus = 0.12;
		bonus = basic_salary * percentage_bonus;
		gross_salary = basic_salary + bonus;
		cout << "Your Gross salary is: " << gross_salary;
	}

	else if (str == 'b') {
		basic_salary = 15000;
		percentage_bonus = 0.14;
		bonus = basic_salary * percentage_bonus;
		gross_salary = basic_salary + bonus;
		cout << "Your Gross salary is: " << gross_salary;
	}

	system("Pause");
	return 0;
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
