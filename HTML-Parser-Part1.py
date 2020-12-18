''' Sample input '''
#2
#<html><head><title>HTML Parser - I</title></head>
#<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
''' Sample output '''
#Start : html
#Start : head
#Start : title
#End   : title
#End   : head
#Start : body
#-> data-modal-target > None
#-> class > 1
#Start : h1
#End   : h1
#Empty : br
#End   : body
#End   : html


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))

''' ========= Also a slightly different version of the above with an alternative output for a different challenge ======= '''
from html.parser import HTMLParser

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
htmlStr = ""
for i in range(N):
    htmlStr += input().strip()
    
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print (tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
           
    # def handle_endtag(self, tag):
    #     print (tag)
        
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
    
MyParser = MyHTMLParser()
MyParser.feed(htmlStr)
