/*
 * enzyme_sort.cpp
 *
 *  Created on: 2018/03/12
 *      Author: user
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include "alphanum.hpp"

int main()
{
	std::ifstream enzymes;
	std::ofstream sortedlist;
	std::vector<std::string> enzymelist;
	std::string buff, filename;
	int i, n;

	filename = "";
	buff = "";

	std::cout << "Please input filepath of file to read :" << std::endl;
	std::getline(std::cin, filename);
	enzymes.open(filename);

	if (!enzymes)
	{
	  	std::cerr << "Can't open input file." << std::endl;
	  	exit(1);
	}

	while(std::getline(enzymes, buff))
	{
		enzymelist.push_back(buff);
	}

	enzymes.close();

	filename = "";

	std::sort(std::begin(enzymelist), std::end(enzymelist), doj::alphanum_less<std::string>());

	std::cout << "Please input filepath of output file :" << std::endl;
	std::getline(std::cin, filename);

	sortedlist.open(filename);

	if (!sortedlist)
	{
		std::cerr << "Can't open output file." << std::endl;
		exit(1);
	}

	n = enzymelist.size();

	for(i = 0; i < n; ++i)
	{
		sortedlist << enzymelist[i] << std::endl;
	}

	sortedlist.close();

	return 0;
}
