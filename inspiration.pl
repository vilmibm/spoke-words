#!/usr/bin/perl -w

# what inspiration.pl
# who  nate smith
# when april 2009
# why  this program, for now, gets "inspiration" for other events by pulling a random topic from Wikipedia.
#        inspiration is printed to STDOUT, for piping.
#

use WWW::Mechanize;
use strict;

my $mech = WWW::Mechanize->new();
$mech->agent_alias( 'Windows Mozilla' );

my $url = 'http://en.wikipedia.org/wiki/Special:Random';
my $inspiration;

$mech->get( $url );
$mech->content() =~ m/<h1 id="firstHeading" class="firstHeading">(.*?)<\/h1>/m;
$inspiration = $1;
print $inspiration;
 
