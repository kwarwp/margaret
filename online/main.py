# margaret.online.main.py
from browser import window
import urllib.request

from browser import document

def create_script_tag(src):
    _fp = urllib.request.urlopen(src)
    _data = _fp.read()

    _tag = document.createElement('script')
    _tag.type = "text/javascript"
    _tag.text = _data
    document.get(tag='head')[0].appendChild(_tag)
    
try:
    pjs = window.Peer
    with pjs:
        print(True,pjs)
except Exception as err:
    create_script_tag("https://cdn.jsdelivr.net/npm/peerjs@0.3.20/dist/peer.min.js")
    try:
        pjs = window.Peer
        print(True,pjs)
    except Exception as err:
        print(False, err)
