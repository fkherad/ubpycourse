from flask import *
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('image.html')

@app.route('/result',methods=['GET','POST'])
def upload():
    file= request.files['image']
    file.save(file.filename)
    k="acc_bdfd475b5395d99"
    s="88b509008ffbcf09bf65f21ea4ed0d27"
    image_path=file.filename
    req= requests.post('https://api.imagga.com/v2/uploads',auth=(k,s),files={'image': open(image_path, 'rb')})
    req_json=req.json()
    upload_id=req_json['result']['upload_id']
    req= requests.get('https://api.imagga.com/v2/tags',auth=(k,s),params={'image_upload_id': upload_id})
    req_json = req.json()
    tags = req_json['result']['tags']
    confidence=[]
    for i in range(0,10):
        confidence.append(tags[i]['confidence'])
    maxconf=confidence.index(max(confidence))
    name=tags[maxconf]['tag']['en']
    req= requests.get('https://api.giphy.com/v1/gifs/search',params={'q': name, 'api_key':'QYYx4OgVDKhwddFQ7pTnBlMEhgQWI46N'})
    req_json=req.json()
    url=[]
    for i in range(0,10):
        url.append(req_json['data'][i]['images']['fixed_height']['url'])
    return render_template('result.html',name=url)
if __name__ == '__main__':
   app.run(debug=True)