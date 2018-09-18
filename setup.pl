#!/usr/bin/perl -w

use Archive::Tar;
use File::Copy;

my $SoftwareDir = './Software/';
mkdir($SoftwareDir, 0700) unless(-d $SoftwareDir);
chdir($SoftwareDir) or die "can't chdir $SoftwareDir\n";

#FastX-Toolkit download and install

my $FastXtar = Archive::Tar->new;
my $FastX = 'http://hannonlab.cshl.edu/fastx_toolkit/fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2';
system "wget $FastX";

$FastXtar->read('fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2');
$FastXtar->extract();

my $source_dir = "./Sofware/bin/";
my $target_dir = "/usr/local/bin";

opendir(my $DIR, $source_dir) || die "can't opendir $source_dir: $!";
my @files = readdir($DIR);

foreach my $t (@files)
{
   if(-f "$source_dir/$t" ) {
      #Check with -f only for files (no directories)
      copy "$source_dir/$t", "$target_dir/$t";
   }
}

closedir($DIR);

#Picard download and install

my $Picard = 'https://github.com/broadinstitute/picard/releases/download/2.18.14/picard.jar';
system "wget $Picard";
