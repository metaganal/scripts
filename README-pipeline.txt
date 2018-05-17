GUT METAGENOMIC DATA ANALYSIS PIPELINE

1 June 2016 --> update 20 December 2016
Pande Putu Erawijantari--Dept.Biological Information--Graduate School of Life Science and Biotechnology
Kurokawa-Nakashima-Yamada Laboratory
Tokyo Institute of Technology

A. Important directory
==All of data in ddbj2 server(lustre4 of ddbj): gw2.ddbj.nig.ac.jp==
Raw data 			: /home/pande/gut_microbiome_analysis/all_fastq_gz
Script 				: /home/pande/gut_microbiome_analysis/script
Pogram installed 	: /home/pande/gut_microbiome_analysis/program
Database			: /home/pande/gut_microbiome_analysis/DB

B. Program need to install

==Software version==
Cutadapt    		: 1.9.1
MetaGeneMark 		: 3.26
Bowtie2 			: 2.2.9
idba 				: 1.1.1
ghostx 				: 1.3.7
How to install 		: /home/pande/gut_microbiome_analysis/Install_process.txt

C. Run the bash script
	1. High quality filtering
	   The filtering will including the phix filtering, adapter remover, N-contaminated sequence elimination, length filtering, human genome contamination filtering, combine file and non pair end elimination, and converting the fastq file into fasta file.
	   Script : /home/pande/gut_microbiome_analysis/script/pl2_reads_filtering.sh
	   ussage:
	   normal
	   $bash /home/pande/gut_microbiome_analysis/script/hq_reads/hq_reads_filtering.sh "key" .<dir_out> <dir_raw_data>
	   qsub 
	   $qsub -cwd -l month -l medium -l s_vmem=30G /home/pande/gut_microbiome_analysis/script/hq_reads/hq_reads_filtering.sh "key" <dir_out> <dir_raw_data>
	   final results
	   <dir_out>/"key"/"key".hiseq.final.fasta 

	2. Assembly 
	 	Assemble the high quality sequence after filtering using idba-ud then resulting the scaffold
	 	script : /home/pande/gut_microbiome_analysis/script/pl2_assembly.sh
	 	ussage:
	 	normal:
	 	$bash /home/pande/gut_microbiome_analysis/script/pl2_assembly.sh "key" <dir_out>
	 	qsub :
	    $qsub -cwd -l month -l medium -l s_vmem=100G /home/pande/gut_microbiome_analysis/script/pl2_assembly.sh "key" .<dir_out>
	    final results:
	    <dir_out>/"key"/"key".idba.contig/scaffold.fa

	3 Metagene
	  	Metagene can be used for gene calling through the ORF prediction. In this case we will filter out the protein prediction with sequence more then 50bp sequence of amino acid. 
	  	Script: /home/pande/gut_microbiome_analysis/script/pl2_metagene.sh
	  	ussage:
	  	normal:
	 	$bash /home/pande/gut_microbiome_analysis/script/pl2_metagene.sh "key" <dir_out>
	 	qsub 
	    $qsub -cwd -l month -l medium -l s_vmem=100G /home/pande/gut_microbiome_analysis/script/pl2_metagene.sh "key" <dir_out>
	    final results:
	    <dir_out>/"key"/key.bowtie2.sam
	    <dir_out>/"key"/key.metagenemark/key.metagenemark.gff
	    <dir_out>/"key"/key.metagenemark/key.metagenemark.prot50.fa
	    <dir_out>/"key"/key.metagenemark/key.metagenemark.nucleotide.fa

	4. Ghostx and Bowtie
	   	Ghostx can align the sequence to the database and get the gene prediction homology
	   	Bowtie2 will mapping back the reads to the scaffold results that important for gene coverage calculation
	   	Script: /home/pande/gut_microbiome_analysis/script/pl2_ghostx_bowtie.sh
	   	ussage:
	  	normal:
	 	$bash /home/pande/gut_microbiome_analysis/script/pl2_ghostx_bowtie.sh "key" <dir_out>
	 	qsub --> medium node
	    $qsub -cwd -l month -l medium -l s_vmem=200G /home/pande/gut_microbiome_analysis/script/pl2_ghostx_bowtie.sh "key" <dir_out>
	    final results:
	    <dir_out>/"key"/key.ghostx.aln
	    <dir_out>/"key"/key.bowtie2.sam
	    *notes : sometimes need to specified the consumable memmory using h_vmem

	5. KO Table, KO Pathway and KO module generator
	   This KO_Table script will resulting the final KO abundance, KO pathway and KO module
	   The calculation performed are including the gene coverage calculation; number of top hit; filter out the top hit gene; filter out the gene that has less than 40 of identity and less then 70 of score; filter out the gene hich has less then 80% of coverage; got the final gene abundance; KO mapped to pathway and module; KO, pathway, and module relative abundance
		script : /home/pande/gut_microbiome_analysis/script/pl3_new_KO_Table2.sh
	 	ussage:
	 	normal:
	 	$bash /home/pande/gut_microbiome_analysis/script/pl3_new_KO_Table2.sh "key" <dir_out>
	 	qsub --> medium node
	    $qsub -cwd -l month -l medium -l s_vmem=30GB /home/pande/gut_microbiome_analysis/script/pl3_new_KO_Table2.sh "key" <dir_out>
	    final results:
	    <dir_out>/"key"/key.KO-USCG.txt
	    <dir_out>/"key"/key.KO-pathway.txt
	    <dir_out>/"key"/key.KO-module.txt 

D. Qsub-array
Submiting multiple task can be performed by using qsub-array system in SGE
Default code for the qsub_array
/home/pande/gut_microbiome_analysis/script/qarray_def.sh
ussage:
$ qsub <option> -l s_vmem=<specify> qarray_def <script from the C part>

E. Further analysis (matrix generation, statistic analysis, graph generation)
Several python packsage need to be installed such as numpy, pandas, statsmodel,etc
anaconda is highly recomended to carried out all of analysis in python
"https://docs.continuum.io/anaconda/pkg-docs"
	1.  Matrix generation
		Resume all of the results into one big matrix
		The sequence ID to stage file needed to convert the sequence into the stage
		ussage
		$python pl2_matrix.g.py path_to_the_results file_reference_convert_seq_to_stage
	2.	Hypothesis test and log-odds score (Mann Whitney U test/ranksum test)
		Multiple hypothesis test can be choosed from ranksums or mannwhitneyu package module can be specified in the "hyp_test" variable
		The correction of p-value performed by fdr
		Log odds score to see the data tendency
		positive means the variable overrepresented in the dividen
		negative means the variable overrepresented in the divisor
		ussage
		$python pl2_hyptest.py matrix_table
	3. Graph generation
		Generate the distribution graph of data
		ussage:
		$python table.py matrix_that_need_to_be_analyzed
*Notes: this code only for comparison of two population

*Notes:
-the memmory request value (s_vmem;h_vmem) can be specify based on the memmory required by the sample 
-h_mem should be higher or in the same value with the s_vmem
-Not all nodes can give the number of memmory that requested --> configuration of each neads can be seen by qhost -F h_vmem

#####UPDATE 3 July 2016########3
-No.5 of pipeline got the major update due to eliminnation of USCG marker ussage to relative abundance. 
-addition of session E for further analysis
-IGC related data
momo:/DataPart/IGC/160904_IGC_JPN.annotation_summary
gw2:/home/hshiroma/IGC_JPN/160904_IGC_JPN.annotation_summary
IGC_JPN_ID || Kegg Gene_ID || Prokaryotes or Eukaryotes || Kegg Ortholog_ID || Kegg module_ID || Kegg pathway_ID || enteropathway_ID || Top Hit Score

Step after got the pipeline done:


check