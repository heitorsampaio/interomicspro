from subprocess import call
import os
import sys
import argparse
import shutil
import webbrowser
import subprocess

GLOBAL_PATH='/Users/heitorsampaio/Documents/interomicspro/';


parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="FOLDER", required=True,
                    help="Input folder location")

parser.add_argument("-i", dest="INPUT", required=True,
                    help="Input file .txt")

args = parser.parse_args()

print(args.FOLDER)
print(args.INPUT)

source = args.FOLDER
raw_folder = GLOBAL_PATH+'raw_data_sequence/'
fastQC_out = GLOBAL_PATH+'rnaseq_analysis/FASTQC/unprocessed_fastqc/'
concat = GLOBAL_PATH+'rnaseq_analysis/concatened_data/'

os.mkdir( raw_folder, 0o755 )
os.makedirs( fastQC_out, 0o755 )
os.makedirs( concat, 0o755 )

files = os.listdir(source)
#fastq_Files = os.listdir(raw_folder)

for f in files:
        shutil.move(source+f, raw_folder)


print("Raw Data folder is created")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##### Frist QC analysis by 'fastQC' ########
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for fastq in os.listdir(raw_folder):
        call([
            GLOBAL_PATH+"Software/FastQC/fastqc",
            "--outdir", fastQC_out,
            raw_folder+fastq
])

#Display the outputs of fastqc in a browser with a different tab for each fastq file
for i in os.listdir(fastQC_out):
        if i.endswith(".html"):
                webbrowser.open('file://'+fastQC_out+i)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##### Concatented the sequences that were read in diferent lanes ########
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
script_Concat = open("Concatenate.R", "x")
script_Concat.write('''input<-read.table(file = "input.txt", header = F, sep = "\t")
input[,3]<-as.character(input[,3])

a=NULL
input_2concatenated=NULL
for (i in as.matrix(unique(input[,2]))){
  for (j in c(1:length(unique(input[,5])))){
      assign(paste("a",sep = ),   
      cbind(a,subset(input, (input[,2]==i & input[,4]==1))[,3][j])
         )
    }
  input_2concatenated=rbind(input_2concatenated,a)
  a=NULL
}

a1=NULL
concatenated_files=NULL
for (i in as.matrix(unique(input[,2]))){
  for (j in c(1:length(unique(input[,5])))){
    assign(paste("a1",sep = ),   
           rbind(a1,subset(input, (input[,2]==i & input[,4]==1))[,3][j])
    )
  }
  concatenated_files=rbind(concatenated_files,a1)
  a1=NULL
}

not_concatenated_files<-subset(input, !(input[,3] %in% concatenated_files))[,3]

input_final=NULL
for (i in unique(input[,2])){
  input_final=rbind(input_final,cbind(
    as.character(subset(input, input[,2]==i & input[,4]=="1")[1,1]),
    i,
    subset(input, input[,2]==i & input[,4]=="1")[1,3],
    subset(input, input[,2]==i & input[,4]=="2")[1,3],
    paste(i,".fastq.gz",sep="")) 
  )
}

input_rnase_qc<-cbind(input_final[,2],paste(input_final[,2],".dup.bam",sep = ""),input_final[,1])
colnames(input_rnase_qc)<-c("Sample ID","Bam File","Notes")

input_star<-as.data.frame(input_final)
input_star[,3]<-gsub(".gz","",input_star[,3])
input_star[,4]<-gsub(".gz","",input_star[,4])

rm(i,a,j,input,a1)

setwd(paste(getwd(),"./rnaseq_analysis/tmp_files/",sep=""))
write.table(x = input_2concatenated,
            file = "input_for_concatenated.txt",sep = "\t",quote = F,row.names = F,col.names = F)

write.table(x = not_concatenated_files,
            file = "not_concatenated_file.txt",sep = "\t",quote = F,row.names = F,col.names = F)

write.table(x = input_final,
            file = "input_final.txt",sep = "\t",quote = F,row.names = F,col.names = F)

write.table(x = input_rnaseq_qc,
            file = "input_rnaseq_qc.txt",sep = "\t",quote = F,row.names = F,col.names = T)
q("no")''')

call([
    "R",
    "CMD",
    "BATCH",
    "Concatenate.R"
])

#Informing the file containg the seq to concatenated

input_2_cat = GLOBAL_PATH+'rnaseq_analysis/tmp_files/input_for_concatenated.txt'
input_not_2_cat = GLOBAL_PATH+'rnaseq_analysis/tmp_files/not_concatenated_file.txt'

subprocess.call(["sed -i 's/NA/\ /g'",input_2_cat], shell=True)

#Interar o R 'cat' para varias linhas

os.chdir( raw_folder )

retval = os.getcwd()
print("Directory changes successfully %s" % retval)


subprocess.call(['''
export input_2_cat=../rnaseq_analysis/tmp_files/input_for_concatenated.txt

export file_not_2_cat=../rnaseq_analysis/tmp_files/not_concatenated_file.txt

for i in $(seq 1 $(cat $input_2_cat  | wc -l)); do 
	cat $(sed -n "$i"p $input_2_cat ) > \
       "$concatened_data"/"$(awk -F "\t" '{print $1}' $input_2_cat  | sed -n "$i"p | cut -d '.' -f 1)".fastq.gz
done

'''
], shell=True)

os.chdir("../")

retval = os.getcwd()
print("Directory changes successfully %s" % retval)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##### Preprocess sequence reads with Trimmomatic ##### ter
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# create a directories to store TRIMMOMATIC output

paired = GLOBAL_PATH+'rnaseq_analysis/preprocessed_data/paired/'
unpaired = GLOBAL_PATH+'rnaseq_analysis/preprocessed_data/unpaired/'
tmp_files = GLOBAL_PATH+'rnaseq_analysis/tmp_files/'
tmp_seq = GLOBAL_PATH+'rnaseq_analysis/tmp_files/sequence/'

os.makedirs( paired )
os.makedirs( unpaired )
os.makedirs( tmp_files )
os.makedirs( tmp_seq )

# creating a link to the ln -s /folderorfile/link/will/point/to /name/of/the/link
for i in os.listdir(concat):
        os.link(concat, tmp_seq)

for i in open("not_concatenated_file.txt", 'r'):
        os.link(raw_folder, tmp_seq)

# creat the file wiht the sample names
os.system("awk '{print $2}' input.txt | sort | uniq > ./rnaseq_analysis/tmp_files/sampleNames.txt")
os.system("awk '{print $1}' input.txt | sort | uniq > ./rnaseq_analysis/tmp_files/groupNames.txt")

subprocess.call(['''

for i in $(seq 1 $(cat ./rnaseq_analysis/tmp_files/input_final.txt | wc -l)); do
 java -jar ../Software/trimmomatic/trimmomatic-0.36.jar PE -threads 20 -trimlog ./rnaseq_analysis/preprocessed_data/$(awk -F"\t" '{print $2}' \
 ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p).txt ./rnaseq_analysis/tmp_files/sequence/$(awk -F"\t" '{print $3}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) \
 ./rnaseq_analysis/tmp_files/sequence/$(awk -F"\t" '{print $4}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) \
 ./rnaseq_analysis/preprocessed_data/paired/$(awk -F"\t" '{print $3}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) \
 ./rnaseq_analysis/preprocessed_data/unpaired/$(awk -F"\t" '{print $3}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) \
 ./rnaseq_analysis/preprocessed_data/paired/$(awk -F"\t" '{print $4}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) \
 ./rnaseq_analysis/preprocessed_data/unpaired/$(awk -F"\t" '{print $4}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:25;

'''])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Post processing FASTQC analysis
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# create a directory to store FASTQC output

fastqc_PRE = GLOBAL_PATH+'rnaseq_analysis/FASTQC/preprocessed_fastqc/'

os.makedirs( fastqc_PRE , 0o755)

# run the fastqc program
for fastq in os.listdir(raw_folder):
        call([
            GLOBAL_PATH+"Software/FastQC/fastqc",
            "-t 10",
            "--outdir", fastqc_PRE,
            raw_folder+fastqc_PRE
])

#Display the outputs of fastqc in a browser with a different tab for each fastq file
for i in os.listdir(fastqc_PRE):
        if i.endswith(".html"):
                webbrowser.open('file://'+fastqc_PRE)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creat the index genome
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#FIXME:

subprocess.call(['''

mkdir -p ./RNAseq/reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Sequence/StarIndex_genome
export genome=./RNAseq/reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Sequence
#export genome_index=./RNAseq/reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Sequence/StarIndex
export genome_index=./RNAseq/reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Sequence/StarIndex_genome

STAR --runThreadN 20 --runMode genomeGenerate --genomeDir $genome_index --genomeFastaFiles $genome/WholeGenomeFasta/*.fa --sjdbGTFfile /home/patgen/Documentos/RNAseq/reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Annotation/Genes/genes.gtf --sjdbOverhang 124


'''], shell=True)


mapped = './rnaseq_analysis/mapped'

os.makedirs( mapped, 0o755)

subprocess.call(['''

export mapped_directory=$rnaseq_analysis/mapped


script $mapped_directory/mapped.txt
for i in $(seq 1 $(cat ./rnaseq_analysis/tmp_files/input_final.txt | wc -l)); do
 STAR --genomeDir $genome_index \
 --readFilesIn \
 ./rnaseq_analysis/preprocessed_data/paired/$(awk -F"\t" '{print $3}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) \
 ./rnaseq_analysis/preprocessed_data/paired/$(awk -F"\t" '{print $4}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p) \
 --readFilesCommand zcat \
 --sjdbScore 2 --outSAMattributes NH HI AS nM XS \
 --outFilterIntronMotifs RemoveNoncanonical \
 --outSAMtype BAM SortedByCoordinate \
 --outFileNamePrefix $mapped_directory/$(awk -F"\t" '{print $2}' $./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p)_ \
 --runThreadN 20 \
 --quantMode TranscriptomeSAM GeneCounts \
 --sjdbGTFfile ./reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Annotation/Genes/genes.gtf
done
exit


'''])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quality control analysis RSeqc
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


stat_info = './rnaseq_analysis/rseqc/stat_info/'

os.makedirs( stat_info, 0o755)

os.chdir(stat_info)

subprocess.call (["python bam_stat.py -i ",mapped+"499_control1_Aligned.sortedByCoord.out.bam"])

#FIXME:
#converting .gtf in .bed
#brew install homebrew/science/bedops
#tar jxvf bedops_linux_x86_64-v2.4.27.tar.bz2 | mv bin bedops

#gtf2bed < /home/patgen/Documentos/RNAseq/reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Annotation/Genes/genes.gtf > /home/patgen/Documentos/RNAseq/reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Annotation/Genes/genes.bed

subprocess.call (["python geneBody_coverage.py -r ../reference_genomes/Mus_musculus_UCSC_mm10/Mus_musculus/UCSC/mm10/Annotation/Genes/genes.bed  -i 499_control1_Aligned.sortedByCoord.out.bam  -o ",stat_info,""])

os.chdir("../")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quality control analysis RNASeqQC
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# create a directory to store duplicate marked files for RNASeqQC analysis of mapped data

dedup = './rnaseq_analysis/rnaseq_qc/dedup/'

os.makedirs( dedup, 0o755)

# index the genome fasta file

subprocess.call(['''

samtools faidx ./Genomes/WholeGenomeFasta/genome.fa

java -jar ../Software/picard.jar CreateSequenceDictionary R=./Genomes/WholeGenomeFasta/genome.fa O=./Genomes/WholeGenomeFasta/genome.dict

'''])

# mark duplicate reads
subprocess.call(['''

for i in $(seq 1 $(cat ./rnaseq_analysis/tmp_files/input_final.txt | wc -l)); do  #alterar o diretorio depois
  java -Xmx64G -jar  $Picard/picard.jar MarkDuplicates \
  I=./rnaseq_analysis/mapped/$(awk -F"\t" '{print $2}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p)_Aligned.sortedByCoord.out.bam \
  O=./rnaseq_analysis/rnaseq_qc/dedup/$(awk -F"\t" '{print $2}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p).dup.bam \
  M=./rnaseq_analysis/rnaseq_qc/dedup/$(awk -F"\t" '{print $2}'./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p).metric.txt VALIDATION_STRINGENCY=SILENT 
  samtools index ./rnaseq_analysis/rnaseq_qc/dedup/$(awk -F"\t" '{print $2}' ./rnaseq_analysis/tmp_files/input_final.txt | sed -n "$i"p).dup.bam
done

'''], shell=True)
