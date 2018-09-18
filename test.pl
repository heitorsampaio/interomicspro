#!/usr/bin/perl -w

use strict;
use warnings;
use Archive::Extract;
use Archive::Tar;
use File::Copy;
use IO::Uncompress::Unzip qw(unzip $UnzipError) ;



print "Do you want to proceed? ";
my $yn = <STDIN>;
if ($yn eq 'n') {
    print "Exiting\n";
    exit;
} else {
    if ($yn eq 'y') {
        #next;
    }
}