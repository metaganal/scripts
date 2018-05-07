/*
 * gene.cpp
 *
 *  Created on: 2018/03/09
 *      Author: user
 */
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

int main()
{
	std::string buff, bufftext, type, filename;
	int i, j, start, stop, genecount, genelength;

	i = j = start = stop = genecount = genelength = 0;
	buff = "";
	bufftext = "gene";
	type = "";

	std::ifstream geneFile;

	std::cout<< "Please input file path of the file to read :" << std::endl;
	std::getline(std::cin,filename);

	geneFile.open(filename);

	if (!geneFile)
	{
  	std::cerr << "Can't open input file." << std::endl;
  	exit(1);
	}

	while (std::getline(geneFile, buff))
	{
		std::stringstream fulltext(buff);

		if(buff.find_first_of('\t') != std::string::npos)
		{
			i= 1;
			while (std::getline(fulltext, buff, '\t'))
			{
				switch(i)
				{
				case 1:
					i++;
					break;
				case 2:
					i++;
					break;
				case 3:
					if(!buff.compare(bufftext))
					{
						genecount++;
						type = bufftext;
					}
					i++;
					break;
				case 4:
					if(!type.compare(bufftext))
					{
						start = stoi(buff);
					}
					i++;
					break;
				case 5:
					if(!type.compare(bufftext))
					{
						stop = stoi(buff);
						genelength += stop - start;
						j++;
						type = "";
					}
					i++;
					break;
				case 6:
					i++;
					break;
				case 7:
					i++;
					break;
				case 8:
					i++;
					break;
				case 9:
					i++;
					break;
				default:
					i = 1;
				}
			}
		}
	}

	geneFile.close();

	filename = "";

	std::ofstream geneOut;

	std::cout << "Please input file path for output file :" << std::endl;
	std::getline(std::cin, filename);

	geneOut.open(filename);

	geneOut << "Total gene count = " << genecount << std::endl;
	geneOut << "Total length of gene regions = " << genelength << std::endl;

	geneOut.close();

	return 0;
}
