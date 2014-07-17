httpget_incremental
===================

Little proof of concept, it sends multiple HTTP GET requests by increasing the number of params within the GET.
The params value is a random integer.
My first Python script. Perhaps you find out some rookie mistakes.

Usage:
$ python httpget_incremental.py [URL] [num_requests]

Example:
$ python httpget_incremental.py http://target.com/path/ 4

Output:
Req:1: http://target.com/path/?id1=8206
Req:2: http://target.com/path/?id1=8206&id2=9153
Req:3: http://target.com/path/?id1=8206&id2=9153&id3=8656
Req:4: http://target.com/path/?id1=8206&id2=9153&id3=8656&id4=862
