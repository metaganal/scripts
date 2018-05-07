/*
 * aminotranslate.cpp
 *
 *  Created on: 2018/03/10
 *      Author: user
 */

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <algorithm>
#include <vector>

std::vector<std::string> translate(std::string seq)
{
	std::map<char,std::vector<std::string> > codontable{
			{'I', {"ATA", "ATC", "ATT"}},
			{'M', {"ATG"}},
			{'T', {"ACA", "ACC", "ACG", "ACT"}},
			{'N', {"AAC", "AAT"}},
			{'K', {"AAA", "AAG"}},
			{'S', {"AGC", "AGT", "TCA", "TCC", "TCG", "TCT"}},
			{'R', {"AGA", "AGG", "CGA", "CGC", "CGG", "CGT"}},
			{'L', {"CTA", "CTC", "CTG", "CTT", "TTA", "TTG"}},
			{'P', {"CCA", "CCC", "CCG", "CCT"}},
			{'H', {"CAC", "CAT"}},
			{'Q', {"CAA", "CAG"}},
			{'V', {"GTA", "GTC", "GTG", "GTT"}},
			{'A', {"GCA", "GCC", "GCG", "GCT"}},
			{'D', {"GAC", "GAT"}},
			{'E', {"GAA", "GAG"}},
			{'G', {"GGA", "GGC", "GGG", "GGT"}},
			{'F', {"TTC", "TTT"}},
			{'Y', {"TAC", "TAT"}},
			{'C', {"TGC", "TGT"}},
			{'W', {"TGG"}}
		};
	std::map<char,std::vector<std::string> >::iterator mapkey;

	std::size_t strlen;
	strlen = seq.size();

	char amino;
	std::string buff, temp;


	if(int(strlen) == 1)
	{
		std::vector<std::string> DNAseq;
		amino = seq.back();
		mapkey = codontable.find(amino);
		for(auto vectit = mapkey->second.begin(); vectit < mapkey->second.end(); ++vectit)
		{
			buff = *vectit;
			DNAseq.push_back(buff);
		}

		return DNAseq;
	}
	else
	{
		amino = seq.back();
		temp = seq.substr(0, strlen - 1);
		std::vector<std::string> DNAseq = translate(temp);
		int n = DNAseq.size();
		for(int i = 0; i < n; ++i)
		{
			std::string buff1 = DNAseq[i];
			mapkey = codontable.find(amino);
			for(auto vectit = mapkey->second.begin(); vectit < mapkey->second.end(); ++vectit)
			{
				std::string buff2 = *vectit;
				buff = buff1 + buff2;
				DNAseq.push_back(buff);
			}
		}
		DNAseq.erase(DNAseq.begin(), DNAseq.begin()+n);

		return DNAseq;
	}
}

int main()
{
	int i = 0;
	std::string seq;

	std::vector<std::string> DNAseq;

	seq = "";

	std::cout << "This program generates all possible DNA sequences coding the amino acid sequence." << std::endl;
	std::cout << "Input amino acid sequence :" << std::endl;
	std::cout << "(Press Enter key to finish.)" << std::endl;
	std::getline(std::cin,seq);

	DNAseq = translate(seq);

	for(i = 0; i < int(DNAseq.size()); ++i)
	{
		std::cout << DNAseq[i] << std::endl;
	}

	return 0;
}
