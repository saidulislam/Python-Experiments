import gzip
with gzip.open('out.log.gz', mode='wb') as z_file:                                      #①
   z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))
 
exit()