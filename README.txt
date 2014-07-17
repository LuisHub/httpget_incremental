httpget_incremental
===================

Mi primer script en python. Mini prueba de concepto, envía múltiples peticiones HTTP GET incrementando el número de parámetros dentro del GET.
El valor de los parámetros es un entero aleatorio.
Quizás encuentres algún error de novato o malas prácticas. ;-P

My first Python script. Mini proof of concept, it sends multiple HTTP GET requests by increasing the number of params within the GET.
The params value is a random integer.(first alpha version)
Perhaps you find out some rookie mistakes.

Usage:
$ python httpget_incremental.py [URL] [num_requests]

Example:
$ python httpget_incremental.py http://target.com/path/ 4

Output:
Req:1: http://target.com/path/?id1=8206
Req:2: http://target.com/path/?id1=8206&id2=9153
Req:3: http://target.com/path/?id1=8206&id2=9153&id3=8656
Req:4: http://target.com/path/?id1=8206&id2=9153&id3=8656&id4=862
