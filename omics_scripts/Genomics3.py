from subprocess import call
import os
import sys
import argparse

#Map and clean up short read sequence data http://gatkforums.broadinstitute.org/gatk/discussion/6483/how-to-map-and-clean-up-short-read-sequence-data-efficiently#step1

parser = argparse.ArgumentParser()
parser.add_argument("-i", dest="BAMFILE", required=True,
                    help="Bam_Adapmark Filename")
parser.add_argument("-o", dest="OUTPUT", required=True,
                    help="FASTAQ Output Filename")
parser.add_argument("-b", dest="BAM", required=True,
                    help="***_fastqtosam.bam Filename")
parser.add_argument("-s", dest="SAMPLE", required=True,
                    help="Sample name:ex L00*")
args = parser.parse_args()


print(args.BAMFILE)
print(args.OUTPUT)
print(args.METRICS)
print(args.BAM)
print(args.SAMPLE)

run3 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    "../Software/picard.jar", 
    "SamToFastq", 
    "I=",(args.BAMFILE),
    "FASQ=",(args.OUTPUT),
    "CLIPPING_ATTRIBUTE=XT",
    "CLIPPING_ACTION=2",
    "INTERLEAVE=true",
    "NON_PF=true",
    "TMP_DIR=./tmp"
    ])

run4 = call([
    "bwa",
    "mem",
    "-M",
    "-t 20",
    "-p genome.fa",
    "/dev/stdin"
])

run5 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    "../Software/picard.jar",
    "MergeBamAlignment",
    "ALIGNED_BAM=/dev/stdin",
    "UNMAPPED_BAM=",(args.BAM),
    "OUTPUT=",(args.SAMPLE),"_piped.bam",
    "R= genome.fa",
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
