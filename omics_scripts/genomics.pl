#!/usr/bin/perl -w

use strict;
use warnings;
use Archive::Extract;
use Archive::Tar;
use File::Copy;
use IO::Uncompress::Unzip qw(unzip $UnzipError) ;
use Term::ANSIColor qw(:constants);

print BLUE, "
██████╗  █████╗ ████████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝ ██╔════╝████╗  ██║
██████╔╝███████║   ██║   ██║  ███╗█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║   ██║   ██║   ██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║   ██║   ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝
       Patologia Molecular e Medicina Genômica
                                                coded by Heitor Sampaio;\n", RESET;



print "+++ This script will install all necessary Genomics softwares for InterOmics PRO \n";

print "Do you want to proceed? (Yes(1)/No(0)) ";
my $yn = <STDIN>;
if ($yn == '0') {
    print "Exiting\n";
    exit;
} else {
    if ($yn == "1") {
        
    }
}

my $SoftwareDir = './Software/';
mkdir($SoftwareDir, 0700) unless(-d $SoftwareDir);
chdir($SoftwareDir) or die "can't chdir $SoftwareDir\n";

#FastX-Toolkit download and install

print "\n[+] Installing FastX-Toolkit ...\n\n";

my $FastX = 'sudo apt-get install fastx-toolkit';
system($FastX);

#Picard download and install

print "\n[+] Installing Picard ...\n\n";

my $Picard = 'https://github.com/broadinstitute/picard/releases/download/2.18.14/picard.jar';
system "wget $Picard";

#FastQC download and install

print "\n[+] Installing FastQC ...\n\n";

my $FastQC = 'https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip';
system "wget $FastQC";

my $FastQCzip = Archive::Extract->new( archive => 'fastqc_v0.11.7.zip' );
    $FastQCzip->is_zip;
    my $FastQCunzip = $FastQCzip->extract or die $FastQCzip->error;

my $FastQCFile = 'fastqc_v0.11.7.zip';
unlink $FastQCFile;

#GATK download and install

print "\n[+] Installing GATK ...\n\n";

my $GATK = 'https://github.com/broadinstitute/gatk/releases/download/4.0.8.1/gatk-4.0.8.1.zip';
system "wget $GATK";

my $GATKzip = Archive::Extract->new( archive => 'gatk-4.0.8.1.zip' );
    $GATKzip->is_zip;
    my $GATKunzip = $GATKzip->extract or die $GATKzip->error;

my $GATKfile = 'gatk-4.0.8.1.zip';
unlink $GATKfile;

#SAMtools download and install

print "\n[+] Installing SAMtools ...\n\n";

my $SAMtools = 'sudo apt-get install samtools';
system($SAMtools);

#IGV download and install

print "\n[+] Installing IGVtools ...\n\n";

my $IGV = 'http://data.broadinstitute.org/igv/projects/downloads/2.4/igvtools_2.4.14.zip';
system "wget $IGV";

my $IGVzip = Archive::Extract->new( archive => 'igvtools_2.4.14.zip');
    $IGVzip->is_zip;
my $IGVunzip = $IGVzip->extract or die $IGVzip->error;

my $IGVfiles = 'igvtools_2.4.14.zip';
unlink $IGVfiles;

#VCFtools download and install

print "\n[+] Installing VCFtools ...\n\n";

my $VCFtools = 'sudo apt-get install vcftools';
system($VCFtools);

my $ZLIB = 'sudo apt-get install zlib1g-dev';
system($ZLIB);

#my $autoconf = 'sudo apt-get install autoconf';
#system ($autoconf);

#my $VCFautogen = 'bash ./vcftools-0.1.16/autogen.sh';
#system($VCFautogen);

#my $VCFconfig = './vcftools-0.1.16/configure';
#system($VCFconfig);

#my $VCFmake = 'sudo make';
#system($VCFmake);

#my $VCFmake_install = "sudo make install";
#system($VCFmake_install);

#BWA download and install

print "\n[+] Installing BWA ...\n\n";

my $BWA = 'sudo apt-get install bwa';
system($BWA);