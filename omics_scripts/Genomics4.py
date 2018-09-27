from subprocess import call
import os
import sys
import argparse

#Merge files of the same sample

parser = argparse.ArgumentParser()
parser.add_argument("-i", dest="INPUT1", required=True,
                    help="Input sample 1 piped")
parser.add_argument("-i2", dest="INPUT2", required=True,
                    help="Input sample 2 piped")
parser.add_argument("-i3", dest="INPUT3", required=True,
                    help="Input sample 3 piped")
parser.add_argument("-i4", dest="INPUT4", required=True,
                    help="Input sample 4 piped*")
parser.add_argument("-o", dest="OUTPUT", required=True,
                    help="BAM output name")
args = parser.parse_args()


print(args.INPUT1)
print(args.INPUT2)
print(args.INPUT3)
print(args.INPUT4)
print(args.OUTPUT)

run3 = call([
    "java", 
    "-Xmx64G", 
    "-jar", 
    "../Software/picard.jar", 
    "MergeSamFiles",
    "I=",(args.INPUT1),
    "I=",(args.INPUT2),
    "I=",(args.INPUT3),
    "I=",(args.INPUT4),
    "O=",(args.OUTPUT),
    "SORT_ORDER=coordinate",
    "USE_THREADING=true"
    ])