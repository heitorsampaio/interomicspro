#!/usr/bin/perl -w

use strict;
use warnings;
use Archive::Extract;
use Archive::Tar;
use File::Copy;

my $SoftwareDir = './Software/';
mkdir($SoftwareDir, 0700) unless(-d $SoftwareDir);
chdir($SoftwareDir) or die "can't chdir $SoftwareDir\n";

print "\n[+] Installing Trimmomatic ...\n\n";

my $Trimm = 'http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip';
system(wget $Trimm);

my $TrimmZip = Archive::Extract->new ( archive => 'Trimmomatic-0.38.zip' );
    $TrimmZip->is_zip;
    my $TrimmUnZip = $TrimmZip->extract or die $TrimmZip->error;

my $TrimmFile = 'Trimmomatic-0.38.zip';
unlink $TrimmFile;
