﻿// salary.cpp : This file contains the 'main' function. Program execution begins and ends there.
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
