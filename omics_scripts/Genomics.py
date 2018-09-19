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
parser.add_argument("-lib", dest="LIB_NAME", required=True,
                    help="Library Name")
parser.add_argument("-p", dest="PLATFORM", required=True,
                    help="Platform Name")
args = parser.parse_args()


print(args.FASTQ)
print(args.FASTQ2)
print(args.OUTPUT)
print(args.READ_GROUP)
print(args.SAMPLE_NAME)
print(args.LIB_NAME)
print(args.PLATFORM)

call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    "./Software/picard.jar", 
    "FastqToSam", 
    "FASTQ=",(args.FASTQ) , 
    "FASTQ2=", (args.FASTQ2), 
    "OUTPUT=",(args.OUTPUT), 
    "READ_GROUP_NAME=", (args.READ_GROUP),
    "SAMPLE_NAME=", (args.SAMPLE_NAME),
    "LIBRARY_NAME=", (args.LIB_NAME),
    "PLATFORM=", (args.PLATFORM)
    ])