from subprocess import call
import os
import sys

b = ('''
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
**                                                                **
====================================================================
    ''')

#while True:


os.system('clear')
print (b)
print ('\r')


print ("""
    1 - Genomics Analysis
    2 - Transcriptomics Analysis
    3 - Proteomics Analysis
    4 - All Analysis [Recommend]
    5 - Exit
    
    
    """)

EnterOp = input("Enter : ")

if EnterOp == '1':
    
    fastq1 = input("Insert your FASTQ one Location : ")
    fastq2 = input("Insert your FASTQ two Location : ")
    rgName = input("Insert your Read Group name [Ex.:L001] : ")
    sampName = input("Insert your Sample Name [Ex.:SRR] : ")
    outName = input("Insert your Output name [Ex.:Filename.bam]: ")

    call ([
        "python3",
        "./omics_scripts/Genomics.py",
        "-f1",(fastq1),
        "-f2",(fastq2),
        "-rg",(rgName),
        "-s",(sampName),
        "-o",(outName)
    ])

    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == '2':

    call([
        'python3',
        './omics_scripts/Transcriptomics.py',
        
    ])

    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == '3':

    call([
        'python3',
        './omics_scripts/Proteomics.py'
    ])

    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == '4':

    fastq1 = input("Insert your FASTQ one Location : ")
    fastq2 = input("Insert your FASTQ two Location : ")
    rgName = input("Insert your Read Group name [Ex.:L001] : ")
    sampName = input("Insert your Sample Name [Ex.:SRR] : ")

    call ([
        "python3",
        "./omics_scripts/Genomics.py",
        "-f1",(fastq1),
        "-f2",(fastq2),
        "-rg",(rgName),
        "-s",(sampName),
        "-o",(outName)
    ])
    call([
        'python3',
        './omics_scripts/Transcriptomics.py',
        
    ])
    call([
        'python3',
        './omics_scripts/Proteomics.py'
    ])

    print ("\n")
    input("[*] Back To Menu (Press Enter...) ")

elif EnterOp == '5':
    print ("\n")
    quit()

else:
    print ("[!] Please Enter a Number")
    input ("[*] Back To Menu (Press Enter...) ")