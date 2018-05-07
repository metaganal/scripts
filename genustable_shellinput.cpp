/*
 * genus_table.cpp
 *
 *  Created on: 2018/03/12
 *      Author: user
 */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

int main(int argc, char** argv)
{
	std::ifstream genus;
	std::string buff, filename, choice;
	std::vector<std::string> genuslist;
	std::vector<std::vector<std::string>> totalgenuslist;
	std::map<std::string, std::vector<int> > genustable;
	std::map<std::string, std::vector<int> >::iterator genusit;
	std::pair<std::string, std::vector<int> > insertkey;
	std::ofstream list;

    buff = "";

	int i;
	i = 1;

    if (argc < 2)
    {
        std::cerr << "This program turns lists into a table." << std::endl;
        std::cerr << "Usage: " << argv[0] << " <Path of input file 1> ... <Path of input file n>" << std::endl;
    }

	for (i = 1; i < argc - 1 ; ++i)
	{
		genus.open(argv[i]);

		if (!genus)
			{
				std::cerr << argv[i] << " is an invalid file path." << std::endl;
				break;
			}
		else
		{
			while(std::getline(genus, buff))
			{
				genuslist.push_back(buff);
			}

			genus.close();
			totalgenuslist.push_back(genuslist);
		}
	}

	for(i = 0; i < int(totalgenuslist.size()); ++i)
	{
		for(int j = 0; j < int(totalgenuslist[i].size()); ++j)
		{
			buff = totalgenuslist[i][j];
			genusit = genustable.find(buff);

			if(genusit == genustable.end())
			{
				genustable.insert(std::pair<std::string, std::vector<int> >(buff, std::vector<int>()));
				for(int n = 0; n < int(totalgenuslist.size()); ++n)
				{
					genustable[buff].push_back(0);
				}
				++genustable[buff][i];
			}
			else
			{
				++genustable[buff][i];
			}
		}
	}

    list.open(argv[argc-1]);

	list << "The lists contain :" << std::endl;

	for(genusit = genustable.begin(); genusit != genustable.end(); ++genusit)
	{
		list << genusit->first;
		for(auto vectit = genusit->second.begin(); vectit != genusit->second.end(); ++vectit)
		{
			list << ", " << *vectit;
		}
		list << std::endl;
	}
	return 0;
}
