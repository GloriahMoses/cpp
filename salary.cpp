// salary.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
using namespace std;

int main()
{
	float basic_salary, percentage_bonus, bonus, gross_salary;

	char job_category;
	cout << "Enter your job group category:";
	cin >> job_category;
	job_category = tolower(job_category);


	if (job_category == 'a') {
		basic_salary = 10000;
		percentage_bonus = 0.12;
		bonus = basic_salary * percentage_bonus;
		gross_salary = basic_salary + bonus;
		cout << "Your Gross salary is: " << gross_salary;
	}
	
	else if (job_category == 'b') {
		basic_salary = 15000;
		percentage_bonus = 0.14;
		bonus = basic_salary * percentage_bonus;
		gross_salary = basic_salary + bonus;
		cout << "Your Gross salary is: " << gross_salary;
	}
	
	else if (job_category == 'c') {
		basic_salary = 20000;
		percentage_bonus = 0.16;
		bonus = basic_salary * percentage_bonus;
		gross_salary = basic_salary + bonus;
		cout << "Your Gross salary is: " << gross_salary;
	}
	
	else if (job_category == 'd') {
		basic_salary = 30000;
		percentage_bonus = 0.20;
		bonus = basic_salary * percentage_bonus;
		gross_salary = basic_salary + bonus;
		cout << "Your Gross salary is: " << gross_salary;
	}
	
	else if (job_category == 'e') {
		basic_salary = 50000;
		percentage_bonus = 0;
		bonus = basic_salary * percentage_bonus;
		gross_salary = basic_salary + bonus;
		cout << "Your Gross salary remains the same for this job category: " << gross_salary;
	}
	system("pause");
	return 0;
}
