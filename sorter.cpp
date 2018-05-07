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
#include <sstream>
#include <cctype>
#include <iterator>

bool compareNat(const std::string& a, const std::string& b)
{
    if (a.empty())
        return true;
    if (b.empty())
        return false;
    if (std::isdigit(a[0]) && !std::isdigit(b[0]))
        return true;
    if (!std::isdigit(a[0]) && std::isdigit(b[0]))
        return false;
    if (!std::isdigit(a[0]) && !std::isdigit(b[0]))
    {
        if (std::toupper(a[0]) == std::toupper(b[0]))
            return compareNat(a.substr(1), b.substr(1));
        return (std::toupper(a[0]) < std::toupper(b[0]));
    }

    // Both strings begin with digit --> parse both numbers
    std::istringstream issa(a);
    std::istringstream issb(b);
    int ia, ib;
    issa >> ia;
    issb >> ib;
    if (ia != ib)
        return ia < ib;

    // Numbers are the same --> remove numbers and recurse
    std::string anew, bnew;
    std::getline(issa, anew);
    std::getline(issb, bnew);
    return (compareNat(anew, bnew));
}

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

	std::sort(std::begin(enzymelist), std::end(enzymelist), compareNat);

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
