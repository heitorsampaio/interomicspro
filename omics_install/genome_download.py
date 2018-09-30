from subprocess import call
import os
import sys


path = "./Genomes/"

os.mkdir( path, 0o755 );

print("Genome path is created")

os.chdir( path )

retval = os.getcwd()

print("Directory changes successfully %s" % retval)


#variables
homChoice = ['H.sapiens', 'human']
musChoice = ['M.musculus']
ratChoice = ['R.norvegicus']
droChoice = ['D.melanogaster']

genome = input('''
Which reference genome you want to download? [H.sapiens/M.musculus/R.norvegicus/D.melanogaster]

Enter:''' )



if genome in homChoice:
    print("Downloading Homo sapiens reference genome! This could take a while")
    call([
        "wget",
        "ftp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Homo_sapiens/NCBI/build37.2/Homo_sapiens_NCBI_build37.2.tar.gz"
    ])

    print("Extracting the Homo sapiens reference genome! This could take a while")
    
    call([
        "tar",
        "-xzvf",
        "Homo_sapiens_NCBI_build37.2.tar.gz"
    ])
    call([
        "rm",
        "Homo_sapiens_NCBI_build37.2.tar.gz"
    ])
elif genome in musChoice:
    print("Downloading Mus musculus reference genome! This could take a while")
    call([
        "wget",
        "ftp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Mus_musculus/NCBI/build37.2/Mus_musculus_NCBI_build37.2.tar.gz"
    ])

    print("Extracting the Mus musculus reference genome! This could take a while")

    call([
        "tar",
        "-xzvf",
        "Mus_musculus_NCBI_build37.2.tar.gz"
    ])
    call([
        "rm",
        "Mus_musculus_NCBI_build37.2.tar.gz"
    ])
if genome in ratChoice:
    print("Downloading Rattus norvegicus reference genome! This could take a while")
    call([
        "wget",
        "ftp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Rattus_norvegicus/NCBI/Rnor_6.0/Rattus_norvegicus_NCBI_Rnor_6.0.tar.gz"
    ])

    print("Extracting the Rattus norvegicus reference genome! This could take a while")

    call([
        "tar",
        "-xzvf",
        "Rattus_norvegicus_NCBI_Rnor_6.0.tar.gz"
    ])

    call([
        "rm",
        "Rattus_norvegicus_NCBI_Rnor_6.0.tar.gz"
    ])
elif genome in droChoice:
    print("Downloading Drosophila melanogaster reference genome! This could take a while")
    call([
        "wget",
        "ftp://igenome:G3nom3s4u@ussd-ftp.illumina.com/Drosophila_melanogaster/NCBI/build5.41/Drosophila_melanogaster_NCBI_build5.41.tar.gz"
    ])

    print("Extracting the Drosophila melanogaster reference genome! This could take a while")

    call([
        "tar",
        "-xzvf",
        "Drosophila_melanogaster_NCBI_build5.41.tar.gz"
    ])

    call([
        "rm",
        "Drosophila_melanogaster_NCBI_build5.41.tar.gz"
    ])