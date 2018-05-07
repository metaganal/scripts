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

int main(int argc, char** argv)
{
	std::ifstream enzymes;
	std::ofstream sortedlist;
	std::vector<std::string> enzymelist;
	std::string buff;
	int i, n;

	buff = "";

    if (argc < 3)
    {
        std::cerr << "Usage: " << argv[0] << " <Path of input file> <Path of output file>" << std::endl;
    }

	enzymes.open(argv[1]);

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

	std::sort(std::begin(enzymelist), std::end(enzymelist), doj::alphanum_less<std::string>());

	sortedlist.open(argv[2]);

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
