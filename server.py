from flask import Flask, render_template
import urllib2
import json

server=Flask(__name__)

def  flickr(query='<search>'):
    print query
    url='https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=9ec60a6f3b8f6c88b1d05f386106ae5e&tags=%s&format=json&nojsoncallback=1'%query
    u = urllib2.urlopen(url)
    result=u.read()
    w=json.loads(result)
    return w['photos']['photo']

@server.route('/<search>')
def Pickles(search):
    return render_template('Pickles.html',image=flickr(search))


if __name__=='__main__':
    server.debug=True
    server.run()
    
