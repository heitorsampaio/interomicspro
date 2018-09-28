#!/usr/bin/env python3
from subprocess import call
import os
import sys

print ( '''
██████╗  █████╗ ████████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║   ██║   ██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║   ██║   ██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║   ██║   ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝
       Patologia Molecular e Medicina Genômica
                                                coded by Heitor Sampaio;\n

'''
)

#print("")
reqChoice = ['Yes', 'yes']
nopChoice = ['No', 'no']
allChoice = ['All', 'all']
genChoice = ['Genomics', 'genomics']
traChoice = ['Transcriptomics', 'transcriptomics']
proChoice = ['Proteomics', 'proteomics']
quiChoice = ['Quit', 'quit']

requirement = input('''
First we need to install all requirements to run perfectly, do you accept? [Yes(Recommend)/No]

:''' )

if requirement in reqChoice:
    print("insert your sudo passwd")
    call([
        "sudo",
        "apt-get",
        "install",
        "libarchive-extract-perl",
        "wget",
        "unzip"
    ])
elif requirement in nopChoice:
   print()

input = input('''
Which module from InterOmics do you want to install? [All/Genomics/Transcriptomics/Proteomics or Quit]

:''' )

if input in allChoice:
    call([
        "perl",
        "./all.pl"
    ])
elif input in genChoice:
    call([
        "perl",
        "./genomics.pl"
    ])
if input in traChoice:
    call([
        "perl",
        "./transcriptomics.pl"
    ])
elif input in proChoice:
    call([
        "perl",
        "./proteomics.pl"
    ])
if input in quiChoice:
    print("Exiting!")