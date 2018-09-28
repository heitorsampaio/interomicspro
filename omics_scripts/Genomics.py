
from subprocess import call
import os
import sys
import argparse

#Generate an unmapped BAM from FASTQ or aligned BAM using PICARD

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

##Generate an unmapped BAM from FASTQ or aligned BAM
print('''
[+][+][+]
Generate an unmapped BAM from FASTQ or aligned BAM!!
[+][+][+]
''')

run1 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    "../Software/picard.jar", 
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
    "../Software/picard.jar", 
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
    "../Software/picard.jar", 
    "SamToFastq", 
    "I=",(args.SAMPLE_NAME+"_adapmark.bam"),
    "FASTQ=",(args.SAMPLE_NAME+"_samtofastq.bam"),
    "CLIPPING_ATTRIBUTE=XT",
    "CLIPPING_ACTION=2",
    "INTERLEAVE=true",
    "NON_PF=true",
    ])

run4 = call([
    "bwa",
    "mem",
    "-M",
    "-t 20",
    "-p genome.fa",
    (args.SAMPLE_NAME+"_samtofastq.bam")
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
    "../Software/picard.jar",
    "MergeBamAlignment",
    "ALIGNED_BAM=",(args.SAMPLE_NAME+"_samtofastq.bam"),
    "UNMAPPED_BAM=",(args.OUTPUT),
    "OUTPUT=",(args.SAMPLE_NAME+"_piped.bam"),
    "R=genome.fa",
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