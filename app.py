from flask import Flask, request
import json
import pytesseract
from PIL import Image
import re
import datefinder

app = Flask(__name__)

@app.route('/image_to_text', methods=['POST'])
def image_to_text():
    if request.method == 'POST':
        # check if the post request has the file part
        if ('media' in request.files):    
            file1 = request.files.get('media')
            image = Image.open(file1)
            image_to_text = pytesseract.image_to_string(image, lang='eng')
            matches = datefinder.find_dates(image_to_text)
            dates = []
            for i in matches:
                dates.append(i)
            # m = re.search('\b(\d{2}-\d{2}-\d{4})\.', image_to_text)                           
            return dates     
    
# When debug = True, code is reloaded on the fly while saved
if __name__ =='__main__':
    app.run()
