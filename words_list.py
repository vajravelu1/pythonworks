'''this module will fetch words from url and list it
the url is hard coded as of now,
this message is just to check working of docstrings'''

from urllib.request import urlopen                                                       

def w1():
	'''This function runs automatically when called as a OS script ,
	when imported as a function it this method has to be invoked w1()'''
##fdjkfhdksj fsdkjbnjkfdsh kfjsdjkfdsh
##jkfdhjkfsdhkjdfsh kjlfdhkfsds
	file_words=[]
	with urlopen('https://www.sample-videos.com/text/Sample-text-file-10kb.txt') as url_obj:
	    for line in url_obj:                                                                 
	            line_words=line.split()                                                      
	            for word in line_words:                                                      
	                    file_words.append(word.decode('utf-8'))                              
	                                                                                         
	
	for w1 in file_words:
		print(w1)

if __name__=='__main__':
	w1()

