
from subprocess import call
import os
import sys
import argparse
import errno

GLOBAL_PATH='/Users/heitorsampaio/Documents/interomicspro/'

#Generate an unmapped BAM from FASTQ or aligned BAM using PICARD

#TODO buscar dentro da pasta todos os .fastq


parser = argparse.ArgumentParser()
parser.add_argument("-f1", dest="FASTQ", required=True,
                    help="FastQ filename")

parser.add_argument("-f2", dest="FASTQ2", required=True,
                    help="FastQ2 filename")

parser.add_argument("-o", dest="OUTPUT", required=True,
                    help="Output filename")

parser.add_argument("-rg", dest="READ_GROUP", required=True,
                    help="Read Group name")

parser.add_argument("-s", dest="SAMPLE_NAME", required=True,
                    help="Sample Name")
parser.add_argument("-lib", dest="LIB_NAME", required=False,
                    help="Library Name")
parser.add_argument("-p", dest="PLATFORM", required=False,
                    help="Platform Name")
args = parser.parse_args()


print(args.FASTQ)
print(args.FASTQ2)
print(args.OUTPUT)
print(args.READ_GROUP)
print(args.SAMPLE_NAME)
print(args.LIB_NAME)
print(args.PLATFORM)

anal = GLOBAL_PATH+"Analysis/"

try:
    os.mkdir(anal)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass


os.chdir( anal )

retval = os.getcwd()

print("Directory changes successfully %s" % retval)

##Generate an unmapped BAM from FASTQ or aligned BAM

#TODO Rodar controle de qualidade

#TODO FastqC
#

print('''
[+][+][+]
Generate an unmapped BAM from FASTQ or aligned BAM!!
[+][+][+]
''')

run1 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    GLOBAL_PATH+"Software/picard.jar", 
    "FastqToSam", 
    "FASTQ=",(args.FASTQ) , 
    "FASTQ2=", (args.FASTQ2), 
    "OUTPUT=",(args.OUTPUT), 
    "READ_GROUP_NAME=",(args.READ_GROUP),
    "SAMPLE_NAME=",(args.SAMPLE_NAME),
    "LIBRARY_NAME=SureSelectXT_Human_All_Exon_V6+UTRs",
    "PLATFORM=ILLUMINA",
   # call([">" "log.log"])
    ])

print('''
[+][+][+]
Map and clean up short read sequence data!!
[+][+][+]
''')

run2 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    GLOBAL_PATH+"Software/picard.jar", 
    "MarkIlluminaAdapters", 
    "I=",(args.OUTPUT),
    "O=",(args.SAMPLE_NAME+"_adapmark.bam"),
    "M=",(args.SAMPLE_NAME+"_adapmark_metrics.txt"),
    "TMP_DIR=./tmp"
    ])


run3 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    GLOBAL_PATH+"Software/picard.jar", 
    "SamToFastq", 
    "I=",(args.SAMPLE_NAME+"_adapmark.bam"),
    "FASTQ=",(args.SAMPLE_NAME+"_alignedBam.fq"),
    "CLIPPING_ATTRIBUTE=XT",
    "CLIPPING_ACTION=2",
    "INTERLEAVE=true",
    "NON_PF=true",
    ])


#TODO Controle de qualidade

#TODO Excluir sequencias, antes do alinhamento

homChoice = ['H.sapiens', 'human']
musChoice = ['M.musculus']
ratChoice = ['R.norvegicus']
droChoice = ['D.melanogaster']

genome = input('''
Which reference genome you want to use? [H.sapiens/M.musculus/R.norvegicus/D.melanogaster]

:''' )

if genome in homChoice:
    path = (GLOBAL_PATH+"Genomes/Homo_sapiens/NCBI/build37.2/Sequence/BWAIndex/genome.fa")
elif genome in musChoice:
    path = (GLOBAL_PATH+"Genomes/Mus_musculus/NCBI/build37.2/Sequence/BWAIndex/genome.fa")
elif genome in ratChoice:
    path = (GLOBAL_PATH+"Genomes/Rattus_norvegicus/NCBI/Rnor_6.0/Sequence/BWAIndex/genome.fa")
elif genome in droChoice:
    path = (GLOBAL_PATH+"Genomes/Drosophila_melanogaster/NCBI/build5.41/Sequence/BWAIndex/genome.fa")

run4 = call([
    "bwa",
    "mem",
    "-M",
    "-t 20",
    "-p",(path),
    (args.SAMPLE_NAME+"_alignedBam.fq"),
    ">",(args.SAMPLE_NAME+"_aligned.sam")
])

print('''
[+][+][+]
Merge files of the same sample!!
[+][+][+]
''')

run5 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    GLOBAL_PATH+"Software/picard.jar",
    "MergeBamAlignment",
    "ALIGNED_BAM=",(args.SAMPLE_NAME+"_aligned.sam"),
    "UNMAPPED_BAM=",(args.OUTPUT),
    "OUTPUT=",(args.SAMPLE_NAME+"_merged.bam"),
    "R=",(path),
    "CREATE_INDEX=true",
    "ADD_MATE_CIGAR=true",
    "CLIP_ADAPTERS=false",
    "CLIP_OVERLAPPING_READS=true",
    "INCLUDE_SECONDARY_ALIGNMENTS=true",
    "MAX_INSERTIONS_OR_DELETIONS=-1",
    "PRIMARY_ALIGNMENT_STRATEGY=MostDistant",
    "ATTRIBUTES_TO_RETAIN=XS",
    "TMP_DIR=./temp"
])

run6 = call([
    "java",
    "-Xmx64g",
    "-jar",
    GLOBAL_PATH+"Software/picard.jar",
    "MarkDuplicates",
    "INPUT=",(args.SAMPLE_NAME+"_merged.bam"),
    "OUTPUT=",(args.SAMPLE_NAME+"_markDuplicates.bam"),
    "METRICS=",(args.SAMPLE_NAME+"_markDuplicates_metrics.txt"),
    "OPTICAL_DUPLICATE_PIXEL_DISTANCE=2500",
    "CREATE_INDEX=true",
    "TMP_DIR=./tmp"
])

print('''
[+][+][+]
Recalibrate base quality scores!!
[+][+][+]
''')

run7 = call([
    "python3",
    GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T BaseRecalibrator",
    "-nct 20",
    "-R",(path),
    "-I",(args.SAMPLE_NAME+"_markDuplicates.bam"),
<<<<<<< HEAD
    "-knownSites ",GLOBAL_PATH+"dbSNP/00-All.vcf",
    "-knownSites ",GLOBAL_PATH+"dbSNP/hsa_indels_hg38.vcf",
    "-knownSites ",GLOBAL_PATH+"dbSNP/Mills_1kg_indels_hg38.vcf",
=======
    "-knownSites ../dbSNP/00-All.vcf",
    "-knownSites ../dbSNP/hsa_indels_hg38.vcf",
    "-knownSites ../dbSNP/Mills_1kg_indels_hg38.vcf",
>>>>>>> a8d8c2af05c51273f950755f29f5a9c803ac7c10
    "-o",(args.SAMPLE_NAME+"_recal_table.table")
])

run8 = call([
    "python3",
    GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T BaseRecalibrator",
    "-nct 20",
    "-R",(path),
    "-I",(args.SAMPLE_NAME+"_markDuplicates.bam"),
<<<<<<< HEAD
    "-knownSites ",GLOBAL_PATH+"dbSNP/00-All.vcf.gz",
    "-knownSites ",GLOBAL_PATH+"dbSNP/hsa_indels_hg38.vcf",
    "-knownSites ",GLOBAL_PATH+"dbSNP/Mills_1kg_indels_hg38.vcf",
=======
    "-knownSites ../dbSNP/00-All.vcf.gz",
    "-knownSites ../dbSNP/hsa_indels_hg38.vcf",
    "-knownSites ../dbSNP/Mills_1kg_indels_hg38.vcf",
>>>>>>> a8d8c2af05c51273f950755f29f5a9c803ac7c10
    "-BQSR",(args.SAMPLE_NAME+"_recal_data.table")
])

run9 = call([
    "python3",
    GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T AnalyzeCovariates",
    "-nct 20",
    "-R",(path),
    "-before",(args.SAMPLE_NAME+"_recal_date.table"),
    "-after",(args.SAMPLE_NAME+"_post_recal_data.table"),
    "-plots",(args.SAMPLE_NAME+"_recalibration_plots.pdf")
])

run10 = call([
    "python3",
    GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T PrintReads",
    "-R",(path),
    "-I",(args.SAMPLE_NAME+"_markDuplicates.bam"),
    "-BQSR",(args.SAMPLE_NAME+"_recal_data.table"),
    "-o",(args.SAMPLE_NAME+"_recal_reads.bam")
])

print('''
[+][+][+]
Perform local realignment around indels!!
[+][+][+]
''')

run11 = call([
    "python3",
    GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T RealignerTargetCreator",
    "-R",(path),
    "-I",(args.SAMPLE_NAME+"_recal_reads.bam"),
<<<<<<< HEAD
    "--known",GLOBAL_PATH+"dbSNP/hsa_indels_hg38.vcf",
    "--known",GLOBAL_PATH+"dbSNP/Mills_1kg_indels_hg38.vcf",
=======
    "--known ../dbSNP/hsa_indels_hg38.vcf",
    "--known ../dbSNP/Mills_1kg_indels_hg38.vcf",
>>>>>>> a8d8c2af05c51273f950755f29f5a9c803ac7c10
    "-o",(args.SAMPLE_NAME+"_forIdelRealigner.intervals")
])

run12 = call([
    "python3",
   GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T IndelRealigner",
    "-R",(path),
    "-I",(args.SAMPLE_NAME+"_recal_reads.bam"),
    "--known",GLOBAL_PATH+"dbSNP/hsa_indels_hg38.vcf",
    "--known",GLOBAL_PATH+"dbSNP/Mills_1kg_indels_hg38.vcf",
    "-targetIntervals",(args.SAMPLE_NAME+"_forIdelRealigner.intervals"),
    "-o",(args.SAMPLE_NAME+"_recal_realigned.bam")
])

print('''
[+][+][+]
Check for sample cross-contamination!!
[+][+][+]
''')

run13 = call([
    "python3",
   GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T ContEst",
    "-R",(path),
    "-I",(args.SAMPLE_NAME+"_recal_realigned.bam"),
    "--genotypes ",GLOBAL_PATH+"dbSNP/1000G_omni2.5.hg38.vcf",
    "-pf ",GLOBAL_PATH+"dbSNP/1000G_phase1.snps.high_confidence.hg38.vcf",
    "-isr INTERSECTION",
    "-br",(args.SAMPLE_NAME+"_contamination_full_report"),
    "-o",(args.SAMPLE_NAME+"_contamination_report.txt")
])

print('''
[+][+][+]
Call variants with HaplotypeCaller!!
[+][+][+]
''')

run14 = call([
    "python3",
   GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T HaplotypeCaller",
    "-nct 20",
    "-R",(path),
    "-I",(args.SAMPLE_NAME+"_recal_realigned.bam"),
    "--genotyping_mode DISCOVERY",
    "-stand_emit_conf 10",
    "-stand_call_conf 30",
    "-maxAltAlleles 10",
    "-o",(args.SAMPLE_NAME+"_raw_variants.vcf")
])

print('''
[+][+][+]
Calculate Depth and Coverage!!
[+][+][+]
''')

run15 = call([
    "python3",
   GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T SelectVariants",
    "-R",(path),
    "-V",(args.SAMPLE_NAME+"_raw_variants.vcf"),
    "-selectType SNP",
    "-o",(args.SAMPLE_NAME+"_raw_snps.vcf")
])

run16 = call([
    "python3",
   GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T VariantFiltration",
    "-R",(path),
    "-V",(args.SAMPLE_NAME+"_raw_variants.vcf"),
    "--filterExpression"'''"QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0"''',
    "--filterName"'''""my_snp_filter"''',
    "-G_filter"'''"GQ < 20.0"''',
    "G_filterName"'''"lowGQ"''',
    "-o",(args.SAMPLE_NAME+"AUT01_filtered_snps.vcf")
])

run17 = call([
    "python3",
   GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T SelectVariants",
    "-R",(path),
    "-V",(args.SAMPLE_NAME+"_raw_variants.vcf"),
    "-selectType INDEL",
    "-o",(args.SAMPLE_NAME+"_raw_indels.vcf")
])

run18 = call([
    "python3",
   GLOBAL_PATH+"Software/gatk-4.0.9.0/gatk",
    "-T VariantFiltration",
    "-R",(path),
    "-V",(args.SAMPLE_NAME+"_raw_variants.vcf"),
    "--filterExpression"'''"QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0"''',
    "--filterName"'''""my_indel_filter"''',
    "-G_filter"'''"GQ < 20.0"''',
    "G_filterName"'''"lowGQ"''',
    "-o",(args.SAMPLE_NAME+"AUT01_filtered_indels.vcf")
])

print('''
[+][+][+]
Generate files with only PASSED variants!!
[+][+][+]
''')

run19 = call([
    "vcftools",
    "--vcf",(args.SAMPLE_NAME+"_filtered_snps.vcf"),
    "--keep-filtered",'''"PASS"''',
    "--recode",
    "--out",(args.SAMPLE_NAME+"_passed_snps")
])

run20 = call([
    "vcftools",
    "--vcf",(args.SAMPLE_NAME+"_filtered_indels.vcf"),
    "--keep-filtered",'''"PASS"''',
    "--recode",
    "--out",(args.SAMPLE_NAME+"_passed_indels")
])

print('''
[+][+][+]
Remover call with low Genotype Quality (GQ < 20.0)!!
[+][+][+]
''')

run21 = call([
    "sed",
    "--in-place=.bak",
    "/lowGQ/d",
    (args.SAMPLE_NAME+"_passed_snps.recode.vcf")
])  

run22 = call([
    "sed",
    "--in-place=.bak",
    "/lowGQ/d",
    (args.SAMPLE_NAME+"_passed_indels.recode.vcf")
])

print('''
[+][+][+]
create index for vcf files with IGV!!
[+][+][+]
''')

run23 = call([
    "java",
    "-Xmx64g",
    "-jar",
   GLOBAL_PATH+"Software/picard.jar",
    "CollectVariantCallingMetrics",
    "INPUT=",(args.SAMPLE_NAME+"_passed_snps.recode.vcf"),
    "OUTPUT=",(args.SAMPLE_NAME+"_passed_snps.recode.vcf"),
    "DBSNP=dbsnp_147.vcf"
])

run24 = call([
    "java",
    "-Xmx64g",
    "-jar",
   GLOBAL_PATH+"Software/picard.jar",
    "CollectVariantCallingMetrics",
    "INPUT=",(args.SAMPLE_NAME+"_passed_indels.recode.vcf"),
    "OUTPUT=",(args.SAMPLE_NAME+"_passed_indels.recode.vcf"),
    "DBSNP=dbsnp_147.vcf"
])
