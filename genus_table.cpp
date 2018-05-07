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

int main()
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
	filename = "";
	choice = "y";

	int i;
	i = 0;

	while (true)
	{
		std::cout << "Please input path of file to read  :" << std::endl;
		std::getline(std::cin, filename);
		genus.open(filename);

		if (!genus)
			{
				std::cout << filename << " is an invalid file path." << std::endl;
				filename = "";
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

			std::cout << "Finished reading " << filename << "." << std::endl;

			filename = "";
		}

		std::cout << "Any more files to read? (Y/N)" << std::endl;
		std::cin >> buff;
		std::transform(buff.begin(), buff.end(), buff.begin(), ::tolower);
		if (buff.compare(choice))
		{
			break;
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


	std::cout << "The lists contain :" << std::endl;

	for(genusit = genustable.begin(); genusit != genustable.end(); ++genusit)
	{
		std::cout << genusit->first;
		for(auto vectit = genusit->second.begin(); vectit != genusit->second.end(); ++vectit)
		{
			std::cout << "\t" << *vectit;
		}
		std::cout << std::endl;
	}
	return 0;
}
