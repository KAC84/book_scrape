import urllib
import urllib2
import re
import time
#url1 ='http://newyork.craigslist.org/search/sss?zoomToPosting=&catAbb=sss&query='

# queryurl = 'blues+junior+amp'

# min1 = '&minAsk='
# minVal = '400'
# max1 = '&maxAsk='
# maxVal = '1000'
# url2 = '&sort=rel&excats='

# url = url1 + queryurl + min1 + minVal + max1 + maxVal + url2

urls = ['http://www.amazon.com/One-Perfect-Night-Contemporary-Romance-ebook/dp/B00AXTM8G2/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1396394146&sr=1-1&keywords=romance',
'http://www.amazon.com/It-Must-Your-Love-Sullivans-ebook/dp/B00GGRBCNU/ref=pd_sim_kstore_2?ie=UTF8&refRID=160YE9QDX1RRVH7Z1AJW',
'http://www.amazon.com/Ruined-Ethan-Frost-Loveswept-Romance-ebook/dp/B00EGMV24G/ref=sr_1_1?s=digital-text&ie=UTF8&qid=1396395687&sr=1-1&keywords=ruined',
'http://www.amazon.com/Tie-Me-Down-Loveswept-Contemporary-ebook/dp/B00DTEMWQY/ref=pd_sim_kstore_4?ie=UTF8&refRID=0G9XQ6XHQA35XPKRNXM3',
'http://www.amazon.com/Addicted-Ethan-Frost-Loveswept-Romance-ebook/dp/B00IHMEBR6/ref=pd_cp_kstore_1',
'http://www.amazon.com/George-Martins-Thrones-5-Book-Boxed-ebook/dp/B00957T6X6/ref=sr_1_3?s=digital-text&ie=UTF8&qid=1396397396&sr=1-3&keywords=george+rr+martin',
]


#Kim should be nicer to Danny 



#print url 

#f = urllib.urlretrieve(url,'query_'+queryurl+'min'+minVal+'max'+maxVal+'.html') 
#fe = urllib.urlretrieve(url,'stupid_romance_book.html') 

kimsfuckingdatabase = []

i = 0
for url in urls:

	iString = str(i)

	stupidbook = "my_file_"+iString+".txt"

	file(stupidbook, "w").write(urllib2.urlopen(url).read())

	with open(stupidbook, 'r') as f:
		for line in f:
			#print line 
			matchLatNW = re.search(r'name="displayedPrice" value="(\d+.\d+)', line)
			if matchLatNW:

				goingin = matchLatNW.group(0).strip(r'name="displayedPrice" value="')

				print goingin

				kimsfuckingdatabase.append(goingin)

				time.sleep(0.0005)
	i = i + 1

print urls
print kimsfuckingdatabase	