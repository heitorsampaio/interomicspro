#!/usr/bin/env python3
'''
#######################################
# File name: run.py                   #
# Author: Heitor Sampaio              #
# Date created: 13/12/2018            #
# Date last modified: 21/03/2019      #
# Python Version: 3.7                 #
#######################################
'''
###########Import Modules################
from subprocess import call
import subprocess
import os
import sys
import argparse
import errno
import shutil
import tarfile
import glob
import datetime
###########################################

########Prepare environment STARTs HERE#############
yes = set(['yes','y','Y','Yes','YES'])
no = set(['N','n','NO','no'])

GLOBAL_PATH='/Users/heitorsampaio/Documents/interomicspro/'
no_raw_dir = input('Insert the files PATH (ex: path/to/files/): \n')

os.chdir(no_raw_dir)

print("Change dir")
retval = os.getcwd()
print(retval)

raw_dir = GLOBAL_PATH+'raw_data/'

try:
    os.mkdir(raw_dir)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass
    
os.chdir(raw_dir)

retval = os.getcwd()

print(retval)

raw_cp = os.listdir(no_raw_dir)

try:
    for files in raw_cp:
        fullpath = os.path.join(no_raw_dir, files)
        shutil.move(fullpath, raw_dir)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass

raw = os.listdir(raw_dir)
print('Files Moved!')

untar_cmd = 'tar -xzvf *.gz'

os.system(untar_cmd)


for remove in os.listdir(raw_dir):
    if remove.endswith('.tar.gz'):
        os.remove(remove)
        print('Raw files removed!')

#############Ends Here##################

###############def functions starts here###################
def logo():
    print('''
██╗███╗   ██╗████████╗███████╗██████╗  ██████╗ ███╗   ███╗██╗ ██████╗███████╗    ██████╗ ██████╗  ██████╗ 
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗████╗ ████║██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██║   ██║██╔████╔██║██║██║     ███████╗    ██████╔╝██████╔╝██║   ██║
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║   ██║██║╚██╔╝██║██║██║     ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║
██║██║ ╚████║   ██║   ███████╗██║  ██║╚██████╔╝██║ ╚═╝ ██║██║╚██████╗███████║    ██║     ██║  ██║╚██████╔╝
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
                                                                                                          
====================================================================
**                WebSite : patgen.com.br                         **
**           Organization : PatGen - UFPE                         **
**             Developer  : Heitor Sampaio                        **
**           Description  : InterOmics Pro suite                  **
**               Licence  : MIT                                   **
====================================================================
    ''')

def menu():
    print('''
██╗███╗   ██╗████████╗███████╗██████╗  ██████╗ ███╗   ███╗██╗ ██████╗███████╗    ██████╗ ██████╗  ██████╗ 
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗████╗ ████║██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██║   ██║██╔████╔██║██║██║     ███████╗    ██████╔╝██████╔╝██║   ██║
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║   ██║██║╚██╔╝██║██║██║     ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║
██║██║ ╚████║   ██║   ███████╗██║  ██║╚██████╔╝██║ ╚═╝ ██║██║╚██████╗███████║    ██║     ██║  ██║╚██████╔╝
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
                                                                                                          
====================================================================
**                WebSite : patgen.com.br                         **
**           Organization : PatGen - UFPE                         **
**             Developer  : Heitor Sampaio                        **
**           Description  : InterOmics Pro suite                  **
**               Licence  : MIT                                   **
====================================================================
    Select from the menu:
    1 : Genomics
    2 : Transcriptomics
    3 : Proteomics
    4 : All
    99: Exit
    ''')
    choice = input("Enter Your Choice: ")
    if choice == "1":
        genomics()
    elif choice == "2":
        transcriptomics()
    elif choice == "3":
        proteomics()
    elif choice == "4":
        all()
    elif choice == "99":
        clearSrc(),sys.exit()
    elif choice == "":
        menu()
    else:
        menu()

def question_pat():
    other_files = input('Do you want to use diferent patient? (Y/N):  ')
    if other_files == 'Y' or other_files == 'y':
        new_patiante_F = input('Select FOWARD file to rename: ')
        new_patiante_R = input('Select REVERSE file to rename: ')
        rename = input('Unique Sample identifier: ')
        sample = input('Unique Patiant identifier: ')
        lab = input('Lab identifier: ')
        time = datetime.datetime.now()
        os.rename(new_patiante_F, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_' + 'F' + ".fasta")
        os.rename(new_patiante_R, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_'+ 'R' + ".fasta")
    elif other_files == 'N' or other_files == 'n':
        return

def question_control():
    control = input("There is a control sample? (Y/N):  ")
    if control == 'Y' or control == 'y':
        control_patiante_F = input('Select FOWARD file to rename: ')
        control_patiante_R = input('Select REVERSE file to rename: ')
        rename = input('Unique Sample identifier: ')
        sample = input('Unique Patiant identifier: ')
        lab = input('Lab identifier: ')
        time = datetime.datetime.now()
        os.rename(control_patiante_F, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + "_CONTROL" + '_' + 'F' + ".fasta")
        os.rename(control_patiante_R, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + "_CONTROL" +'_'+ 'R' + ".fasta") 
    elif control == 'N' or control == 'n':
        return

def genomics():
    foward_to_rename = input('Select FOWARD file to rename: ')
    reverse_to_rename = input('Select REVERSE file to rename: ')
    rename = input('Unique Sample identifier: ')
    sample = input('Unique Patiant identifier: ')
    lab = input('Lab identifier: ')
    time = datetime.datetime.now()
    os.rename(foward_to_rename, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_' + 'F' + ".fasta")
    os.rename(reverse_to_rename, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_'+ 'R' + ".fasta")
    question_pat()
    question_control()
    fastq1 = input("Select the Foward renamed fastq: ")
    fastq2 = input("Select the Reverse renamed fastq: ")
    rgName = input("Insert your Read Group name [Ex.:L001] : ")
    sampName = input("Insert your Sample Name [Ex.:SRR] : ")
    outName = input("Insert your Output name [Ex.:Filename.bam]: ")
    call ([
        "python3",
        GLOBAL_PATH+"omics_scripts/Genomics.py",
        "-f1",(fastq1),
        "-f2",(fastq2),
        "-rg",(rgName),
        "-s",(sampName),
        "-o",(outName)
    ])
    return

def transcriptomics():
    foward_to_rename = input('Select FOWARD file to rename: ')
    reverse_to_rename = input('Select REVERSE file to rename: ')
    rename = input('Unique Sample identifier: ')
    sample = input('Unique Patiant identifier: ')
    lab = input('Lab identifier: ')
    time = datetime.datetime.now()
    os.rename(foward_to_rename, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_' + 'F' + ".fasta")
    os.rename(reverse_to_rename, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_'+ 'R' + ".fasta")
    question_pat()
    question_control()
    #fastq1 = input("Select the Foward renamed fastq: ")
    #fastq2 = input("Select the Reverse renamed fastq: ")
    #rgName = input("Insert your Read Group name [Ex.:L001] : ")
    #sampName = input("Insert your Sample Name [Ex.:SRR] : ")
    #outName = input("Insert your Output name [Ex.:Filename.bam]: ")
    call([
        'python3',
        GLOBAL_PATH+'omics_scripts/Transcriptomics.py',
        
    ])

def proteomics():
    call([
        'python3',
        GLOBAL_PATH+'omics_scripts/Proteomics.py'
    ])

def all():
    foward_to_rename = input('Select FOWARD file to rename: ')
    reverse_to_rename = input('Select REVERSE file to rename: ')
    rename = input('Unique Sample identifier: ')
    sample = input('Unique Patiant identifier: ')
    lab = input('Lab identifier: ')
    time = datetime.datetime.now()
    os.rename(foward_to_rename, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_' + 'F' + ".fasta")
    os.rename(reverse_to_rename, rename + '_' + sample + '_'+ lab + '_' + time.strftime('%Y%m%d%H%M%S') + '_'+ 'R' + ".fasta")
    question_pat()
    question_control()
    fastq1 = input("Select the Foward renamed fastq: ")
    fastq2 = input("Select the Reverse renamed fastq: ")
    rgName = input("Insert your Read Group name [Ex.:L001] : ")
    sampName = input("Insert your Sample Name [Ex.:SRR] : ")
    outName = input("Insert your Output name [Ex.:Filename.bam]: ")

    call ([
        "python3",
        GLOBAL_PATH+"omics_scripts/Genomics.py",
        "-f1",(fastq1),
        "-f2",(fastq2),
        "-rg",(rgName),
        "-s",(sampName),
        "-o",(outName)
    ])
    call([
        'python3',
        GLOBAL_PATH+'omics_scripts/Transcriptomics.py',
        
    ])
    call([
        'python3',
        GLOBAL_PATH+'omics_scripts/Proteomics.py'
    ])


def clearSrc():
    os.system('clear')
##################END OF FUNC######################

###################BEGIND :D#############################
if __name__ == "__main__":
    menu()
###################END OF BEGIND#######################