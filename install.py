#!/usr/bin/env python3
from subprocess import call
import os
import sys

b = ('''
██████╗  █████╗ ████████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║   ██║   ██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║   ██║   ██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║   ██║   ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝
====================================================================
**                WebSite : patgen.com.br                         **
**             Developers : Heitor Sampaio                        **
**           Description  : Installation module for InterOmics Pro**
**                                                                **
====================================================================
    ''')

#while True:


os.system('clear')
print (b)
print ('\r')


print ("""
    1 - Genomics Module
    2 - Transcriptomics Module
    3 - Proteomics Module
    4 - Reference Genome Download
    5 - dbSNP Download
    6 - All [Recommend]
    7 - Exit
    
    
    """)

EnterOp = input("Enter : ")


if EnterOp == "1":
    call([
        "perl",
        "./omics_install/genomics.pl"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "2":
    call([
        "perl",
        "./omics_install/transcriptomics.pl"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "3":
    call([
        "perl",
        "./omics_install/proteomics.pl"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "4":
    call([
        "python3",
        "./omics_install/genome_download.py"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "5":
    dbSnp = "./dbSNP/"
    home = "../"
    os.mkdir( dbSnp, 0o755 )

    print("dbSNP path is created")

    os.chdir( dbSnp )

    retval = os.getcwd()

    print("Directory changes successfully %s" % retval)
    call([
    "wget",
    "ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/VCF/GATK/All_20180418.vcf.gz"
    ])
    call ([
    "unzip",
    "All_20180418.vcf.gz"
    ])
    call ([
    "rm",
    "All_20180418.vcf.gz"
    ])
    call ([
        "cd",
        ".."
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "6":
    call([
        "perl",
        "./omics_install/genomics.pl"
    ])
    call([
        "perl",
        "./omics_install/transcriptomics.pl"
    ])
    call([
        "perl",
        "./omics_install/proteomics.pl"
    ])
    call([
        "python3",
        "./omics_install/genome_download.py"
    ])

    dbSnp = "./dbSNP/"
    os.mkdir( dbSnp, 0o755 )

    print("dbSNP path is created")

    os.chdir( dbSnp )

    retval = os.getcwd()

    print("Directory changes successfully %s" % retval)

    call([
    "wget",
    "ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/VCF/GATK/All_20180418.vcf.gz"
    ])

    call ([
    "unzip",
    "All_20180418.vcf.gz"
    ])

    call ([
    "rm",
    "All_20180418.vcf.gz"
    ])
    call ([
        "cd",
        ".."
    ])

    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "7":
    print ("\n")
    quit()

else:
    print ("[!] Please Enter a Number")
    input ("[*] Back To Menu (Press Enter...) ")