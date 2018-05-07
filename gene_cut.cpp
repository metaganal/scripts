/*
 * gene_cut.cpp
 *
 *  Created on: 2018/03/12
 *      Author: user
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::string readfasta (std::ifstream& gene, std::string a, std::string b)
{
	int i = 0;
	std::string buff = "";
	while(std::getline(gene, buff))
	{
		if (i == 0)
		{
			b = buff;
			i++;
		}
		else
		{
			a = a + buff;
		}
	}

	return a;
}

std::vector<std::string> genecut (std::string gene, std::string enzyme, int cut_pos)
{
	std::size_t start, end;
	std::vector<std::string> frags;
	std::string buff ="";

	start = 0;
	end = gene.find(enzyme);

	while (end != std::string::npos)
	{
			buff = gene.substr(start, end + cut_pos - start);
			frags.push_back(buff);
			start = end + cut_pos;
			end = gene.find(enzyme, start);
	}

	if(end == std::string::npos)
	{
		buff = gene.substr(start);
		frags.push_back(buff);
	}


	return frags;
}

void printfrags(std::vector<std::string> frags)
{
	int i = 0;
	int n = frags.size();

	for (i = 0; i < n; ++i)
	{
		std::cout << "Length of fragment " << i + 1 << " = " << frags[i].length() << std::endl;
	}
}

int main()
{
	std::ifstream fasta;
	std::string filename, fullgene, header, ecor1, hind3, bamh1, not1;
	std::vector<std::string> frags;

	filename = "";
	fullgene = "";
	header = "";
	ecor1 = "GAATTC";
	hind3 = "AAGCTT";
	bamh1 = "GGATCC";
	not1 = "GCGGCCGC";

	int i, n;

	i = 0;
	n = 0;

	std::cout << "Please input filepath of file to read :" << std::endl;
	std::getline(std::cin, filename);

	fasta.open(filename);

	if (!fasta)
	{
		std::cerr << "Can't open input file." << std::endl;
		exit(1);
	}

	std::cout << "Choose restriction enzyme to cut the gene." << std::endl;
	std::cout << "1. EcoRI" << std::endl;
	std::cout << "2. HindIII" << std::endl;
	std::cout << "3. BamHI" << std::endl;
	std::cout << "4. NotI" << std::endl;
	std::cout << "5. All of the above" << std::endl;
	std::cin >> i;

	switch(i)
	{
		case 1:
		{
			fullgene = readfasta(fasta, fullgene, header);
			frags = genecut(fullgene, ecor1, 1);
			printfrags(frags);
			break;
		}
		case 2:
		{
			fullgene = readfasta(fasta, fullgene, header);
			frags = genecut(fullgene, hind3, 1);
			printfrags(frags);
			break;
		}
		case 3:
		{
			fullgene = readfasta(fasta, fullgene, header);
			frags = genecut(fullgene, bamh1, 1);
			printfrags(frags);
			break;
		}
		case 4:
		{
			fullgene = readfasta(fasta, fullgene, header);
			frags = genecut(fullgene, not1, 2);
			printfrags(frags);
			break;
		}
		case 5:
		{
			fullgene = readfasta(fasta, fullgene, header);
			frags = genecut(fullgene, ecor1, 1);
			std::vector<std::string> buff_frags;

			n = frags.size();
			for(i=0;i<n;++i)
			{
				buff_frags = genecut(frags[i], hind3, 1);
				frags.insert(std::end(frags), std::begin(buff_frags), std::end(buff_frags));
			}

			if(buff_frags.size() != 0)
			{
				frags.erase(std::begin(frags), std::begin(frags) + n);
			}

			n = frags.size();
			for(i=0;i<n;++i)
			{
				buff_frags = genecut(frags[i], bamh1, 1);
				frags.insert(std::end(frags), std::begin(buff_frags), std::end(buff_frags));
			}

			if(buff_frags.size() != 0)
			{
				frags.erase(std::begin(frags), std::begin(frags) + n);
			}

			n = frags.size();
			for(i=0;i<n;++i)
			{
				buff_frags = genecut(frags[i], not1, 2);
				frags.insert(std::end(frags), std::begin(buff_frags), std::end(buff_frags));
			}

			if(buff_frags.size() != 0)
			{
				frags.erase(std::begin(frags), std::begin(frags) + n);
			}

			printfrags(frags);
			break;
		}
		default:
		{
			std::cout << "Invalid input, please enter a number between 1 - 5." << std::endl;
		}
	}

	fasta.close();

	i = 0;
	n = 0;

	for(i = 0; i< int(frags.size()); ++i)
	{
		n = n + frags[i].length();
	}

	std::cout<< "Total genome length = " << n << std::endl;

	return 0;
}
