import requests, json
from random import randint
import xml.etree.cElementTree as xml_generator
from flask import Flask


app = Flask(__name__)

@app.route('/randomSong', methods=['GET', 'POST'])
def randomSong():

    url = 'http://api.soundcloud.com/users/338506957/playlists?client_id=x8i900C3Ub1JwHDYgZL7PpstNaqstDJ1'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.get(url, headers=headers)
    data = r.json()
    trackList = data[0]['tracks']

    trackListEndIndex = len(trackList)
    randomTrackNumberId = randint(0, trackListEndIndex-1)
    trackIdInt = trackList[randomTrackNumberId]['id']
    trackId = str(trackIdInt)
    streamTrackUrl = 'http://api.soundcloud.com/tracks/' + trackId + '/stream?client_id=x8i900C3Ub1JwHDYgZL7PpstNaqstDJ1'

    root = xml_generator.Element("Response")
    say = xml_generator.SubElement(root, "Say").text = 'Welcome to Twilio conference, joining you now'
    dial = xml_generator.SubElement(root, "Dial")
    conference = xml_generator.SubElement(dial, "Conference", waitUrl=streamTrackUrl).text = "Artems_conference"
    tree = xml_generator.ElementTree(root)
    #return tree
    xmlstr = xml_generator.tostring(root, encoding='utf8', method='xml')

    return xmlstr

if __name__ == "__main__":
    app.run(port=33507)