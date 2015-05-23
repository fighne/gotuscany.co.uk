#!/usr/bin/perl

# $Id: store_stats.cgi 6 2007-07-04 12:12:35Z CallumCampbell $
# To Use: <!--#exec cgi="/cgi-bin/store_stats.cgi" -->

use strict;
use LWP::UserAgent;

my $ua = LWP::UserAgent->new;
my $response = $ua->post(
	'http://rapidstats.iomartinternet.com/cgi-bin/rapidstats.cgi',
	[ %ENV ]
);

#my $status = $response->status_line;
#my $domain = $ENV{SERVER_NAME};
#my $server = $ENV{SERVER_ADDR};
#
#$response = $ua->post(
#	'http://62.128.193.70/cgi-bin/stat_status.cgi', [ 
#		REQ_STATUS => $status ,
#		REQ_DOMAIN => $domain,
#		REQ_SERVER => $server
#		]);
exit;
