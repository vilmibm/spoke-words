#!/usr/bin/perl -w
use strict;

use Yahoo::Search;
use WWW::Mechanize;

my $mech = WWW::Mechanize->new();
$mech->agent_alias('Windows Mozilla');

my $num_src = 20;
my $query = 'william s burroughs';
my $final = '';
my $min_len = 100;
my $max_len = 350;

my @results = Yahoo::Search->Results(Doc=>$query, Count=>50);
warn $@ if $@;

my @urls; my @sources; my $url; my $data;
foreach my $result (@results) { push @urls, $result->Url; }

while ( $#sources < $num_src && @urls ) {
  $index = int rand $#urls;
  $url = $urls[$index];
  delete $urls[$index];
  $mech->get($url);
  if ( $mech->success() ) {
    $data = $mech->content();
    $data =~ s/<script.*?>.*<\/script>//s;
    $data =~ s/<style.*>.*<\/style>//s; 
    $data =~ s/<.*?>//s;
    $data =~ s/&.*?//s;
  }
}
