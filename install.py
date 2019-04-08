#!/usr/bin/env python3
from subprocess import call
import os
import sys

GLOBAL_PATH='/Users/heitorsampaio/Documents/interomicspro/';


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
        "sudo",
        "apt-get",
        "install",
        "wget",
        "unzip",
        "tar",
        "perl",
        "libarchive-extract-perl"
    ])
    call([
        "perl",
        GLOBAL_PATH+"omics_install/genomics.pl"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "2":
    call([
        "sudo",
        "apt-get",
        "install",
        "wget",
        "unzip",
        "tar",
        "perl",
        "libarchive-extract-perl"
    ])
    call([
        "perl",
        GLOBAL_PATH+"omics_install/transcriptomics.pl"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "3":
    call([
        "sudo",
        "apt-get",
        "install",
        "wget",
        "unzip",
        "tar",
        "perl",
        "libarchive-extract-perl"
    ])
    call([
        "perl",
        GLOBAL_PATH+"omics_install/proteomics.pl"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "4":
    call([
        "sudo",
        "apt-get",
        "install",
        "wget",
        "unzip",
        "tar",
        "perl",
        "libarchive-extract-perl"
    ])
    call([
        "python3",
        GLOBAL_PATH+"omics_install/genome_download.py"
    ])
    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "5":
    call([
        "sudo",
        "apt-get",
        "install",
        "wget",
        "unzip",
        "tar",
        "perl",
        "libarchive-extract-perl"
    ])
    dbSnp = GLOBAL_PATH+"dbSNP/"
    home = GLOBAL_PATH
    os.mkdir( dbSnp, 0o755 )

    print("dbSNP path is created")

    os.chdir( dbSnp )

    retval = os.getcwd()

    print("Directory changes successfully %s" % retval)
    call([
    "wget",
    "ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/VCF/GATK/00-All.vcf.gz"
    ])

    call ([
    "gzip",
    "-d",
    "00-All.vcf.gz"
    ])

    call ([
    "rm",
    "00-All.vcf.gz"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
    ])

    call([
        "rm",
        "Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
    ])

    call([
        "mv",
        "Mills_and_1000G_gold_standard.indels.hg38.vcf",
        "Mills_1kg_indels_hg38.vcf"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/Homo_sapiens_assembly38.known_indels.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "Homo_sapiens_assembly38.known_indels.vcf.gz"
    ])

    call([
        "rm",
        "Homo_sapiens_assembly38.known_indels.vcf.gz"
    ])

    call([
        "mv",
        "Homo_sapiens_assembly38.known_indels.vcf",
        "hsa_indels_hg38.vcf"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/1000G_phase1.snps.high_confidence.hg38.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "1000G_phase1.snps.high_confidence.hg38.vcf.gz"
    ])

    call([
        "rm",
        "1000G_phase1.snps.high_confidence.hg38.vcf.gz"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/1000G_omni2.5.hg38.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "1000G_omni2.5.hg38.vcf.gz"
    ])

    call([
        "rm",
        "1000G_omni2.5.hg38.vcf.gz"
    ])

    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "6":
    call([
        "sudo",
        "apt-get",
        "install",
        "wget",
        "unzip",
        "tar",
        "perl",
        "libarchive-extract-perl"
    ])
    call([
        "perl",
        GLOBAL_PATH+"omics_install/genomics.pl"
    ])
    call([
        "perl",
        GLOBAL_PATH+"omics_install/transcriptomics.pl"
    ])
    call([
        "perl",
        GLOBAL_PATH+"omics_install/proteomics.pl"
    ])
    call([
        "python3",
        GLOBAL_PATH+"omics_install/genome_download.py"
    ])

    dbSnp = GLOBAL_PATH+"dbSNP/"
    os.mkdir( dbSnp, 0o755 )

    print("dbSNP path is created")

    os.chdir( dbSnp )

    retval = os.getcwd()

    print("Directory changes successfully %s" % retval)

    call([
    "wget",
    "ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/VCF/GATK/00-All.vcf.gz"
    ])

    call ([
    "gzip",
    "-d",
    "00-All.vcf.gz"
    ])

    call ([
    "rm",
    "00-All.vcf.gz"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
    ])

    call([
        "rm",
        "Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
    ])

    call([
        "mv",
        "Mills_and_1000G_gold_standard.indels.hg38.vcf",
        "Mills_1kg_indels_hg38.vcf"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/Homo_sapiens_assembly38.known_indels.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "Homo_sapiens_assembly38.known_indels.vcf.gz"
    ])

    call([
        "rm",
        "Homo_sapiens_assembly38.known_indels.vcf.gz"
    ])

    call([
        "mv",
        "Homo_sapiens_assembly38.known_indels.vcf",
        "hsa_indels_hg38.vcf"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/1000G_phase1.snps.high_confidence.hg38.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "1000G_phase1.snps.high_confidence.hg38.vcf.gz"
    ])

    call([
        "rm",
        "1000G_phase1.snps.high_confidence.hg38.vcf.gz"
    ])

    call([
        "wget",
        "https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/1000G_omni2.5.hg38.vcf.gz"
    ])

    call([
        "gzip",
        "-d",
        "1000G_omni2.5.hg38.vcf.gz"
    ])

    call([
        "rm",
        "1000G_omni2.5.hg38.vcf.gz"
    ])

    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == "7":
    print ("\n")
    quit()

else:
    print ("[!] Please Enter a Number")
    input ("[*] Back To Menu (Press Enter...) ")
