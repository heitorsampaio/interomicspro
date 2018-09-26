from subprocess import call
import os
import sys
import argparse

#Marking duplicates http://gatkforums.broadinstitute.org/gatk/discussion/6747/how-to-mark-duplicates-with-markduplicates-or-markduplicateswithmatecigar

parser = argparse.ArgumentParser()
parser.add_argument("-i", dest="INPUT1", required=True,
                    help="Input sample, output from MergeSamFile")
parser.add_argument("-m", dest="METRICS", required=True,
                    help="Markduplicates metrics file")
parser.add_argument("-o", dest="OUTPUT", required=True,
                    help="BAM markduplicates output name")
args = parser.parse_args()


print(args.INPUT1)
print(args.METRICS)
print(args.OUTPUT)

run3 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    "../Software/picard.jar", 
    "MarkDuplicates",
    "I=",(args.INPUT1),
    "OUTPUT=",(args.OUTPUT),
    "METRICS_FILE=",(args.METRICS),
    "OPTICAL_DUPLICATE_PIXEL_DISTANCE=2500",
    "CREATE_INDEX=true",
    "TMP_DIR=./tmp"
    ])