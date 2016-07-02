
## Web Crawler Udacity. ## 


menu = """ 
Welcome to my web Clawer. 
1. For single page || 2. Entire website || 3. Exit.
"""

#procedure coding. 
def get_next_target(s):
	start_link = page.find('<a href=') 
	start_quote = page.find('"', start_link)
	end_quote = page.find ('"', start_quote+1)
	url = s[start_quote+1:end_quote
	return url, end_quote


 
print url
page = page[end_quote:]

