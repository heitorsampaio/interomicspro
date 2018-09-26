from subprocess import call
import os
import sys
import argparse

#Map and clean up short read sequence data http://gatkforums.broadinstitute.org/gatk/discussion/6483/how-to-map-and-clean-up-short-read-sequence-data-efficiently#step1

parser = argparse.ArgumentParser()
parser.add_argument("-i", dest="BAMFILE", required=True,
                    help=".bam Filename")
parser.add_argument("-o", dest="OUTPUT", required=True,
                    help="Output Filename")
parser.add_argument("-m", dest="METRICS", required=True,
                    help="Metrics Filename")
args = parser.parse_args()


print(args.BAMFILE)
print(args.OUTPUT)
print(args.METRICS)

run2 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    "../Software/picard.jar", 
    "MarkIlluminaAdapters", 
    "I=",(args.BAMFILE),
    "O=",(args.OUTPUT),
    "M=",(args.METRICS),
    "TMP_DIR=./tmp"
    ])

