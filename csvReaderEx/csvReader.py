import csvReaderEx

with open('/home/yatraonline.local/prem.bharti/movie_metadata.csv', 'rb') as csvfile:
    spamreader = csvReaderEx.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print ', '.join(row)