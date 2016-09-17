__author__ = 'shenyao'
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("<%s>" % tag)
    def handle_endtag(self, tag):
        print("</%s>" % tag)
    def handle_startendtag(self, tag, attrs):
        print("<%s>" % tag)
    def handle_data(self, data):
        print(data)
    def handle_comment(self, data):
        print('<!--',data,'-->')
    def handle_entityref(self, name):
        print('&%s;'% name)
    def handle_charref(self, name):
        print('&#%s;' % name)

parser=MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

#feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去
#利用HTMLParser，可以把网页中的文本、图像等解析出来
