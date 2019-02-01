#!/usr/bin/python3


'''
 -- Web interface for reading all the Data Matrix codes an image

@author:    Pål Ellingsen
@deffield:  updated: Updated
'''
import os
import io
import sys
import cgi
import cgitb
import numpy as np
import cv2
import base64
from pylibdmtx.pylibdmtx import decode
from PIL import Image

__updated__ = '2019-02-01'
cgitb.enable()

method = os.environ.get("REQUEST_METHOD", "GET")


# Write header of html file
sys.stdout.flush()
sys.stdout.buffer.write(b"Content-Type: text/html\n\n")

def warn(message,color='red'):
    'Method for sending a warning message to the page'
    message = bytes(message,"utf-8")
    sys.stdout.buffer.write(b'<p style="color:'+bytes(color,"utf-8")+b'">'+message+b'</p>')

if method == "POST":
    
    sys.stdout.buffer.write(b"<!doctype html>\n<html>\n <meta charset='utf-8'>")
    form = cgi.FieldStorage()
    warn("<h2>Result from file: "+ form['myfile'].filename+'</h2>',color='black')
    im2 = Image.open(io.BytesIO(form['myfile'].value))
    im = np.array(im2)[:,:,:].copy()
    A = decode(im2)
    C = []
    for ii, a in enumerate(A):
        C.append(a.rect.left + 10*(im.shape[0]-a.rect.top))

    idx = np.argsort(C)
    
    # Writing a table with the returned data matrix codes, hyperlinked to the
    # sios page
    sys.stdout.buffer.write(b'<table><tr>')
    sys.stdout.buffer.write(b'<th>Number</th><th>UUID</th></tr>')
    for ii, idx in enumerate(idx):
        a = A[idx]
        # Write row 
        sys.stdout.buffer.write(b'<tr><td>'+str(ii).encode('utf-8')+b'</td>')
        sys.stdout.buffer.write(b'<td><a href="https://sios-svalbard.org/reports/ind_sample/?eventid='+a.data+b'">'+a.data+b'</a> </td></tr>')
        # Find box in image
        lefttop = (a.rect.left, im.shape[0]-a.rect.top)
        rightbottom = (a.rect.left+a.rect.width,
                       im.shape[0]-(a.rect.top+a.rect.height))
        # Draw rectangle on image
        im = cv2.rectangle(im, lefttop, rightbottom, (0, 0, 255), 4)
        textsize = cv2.getTextSize(str(ii), cv2.FONT_HERSHEY_SIMPLEX, 4, 7)[0]
        # get coords based on boundary
        textX = a.rect.left + int((a.rect.width - textsize[0]) / 2)
        textY = im.shape[0]-a.rect.top - int((a.rect.height - textsize[1]) / 2)
        # Draw number on image
        im = cv2.putText(im, str(ii), (textX, textY),
                     cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 207), 7)


    sys.stdout.buffer.write(b'</table>') # End table
    # Get a base64 string representing the image
    byte_im=base64.b64encode(cv2.imencode('.jpg',im)[1]) 
    # Add the image to the page
    sys.stdout.buffer.write(b'</br></br>Index image. (Right click "Save Image as" to save full version)</br>')
    sys.stdout.buffer.write(b'<img style="max-width:600px;width=100%" id="profileImage" src="data:image/jpg;base64,')
    sys.stdout.buffer.write(byte_im)
    sys.stdout.buffer.write(b'">') 
        
    # Write final html tag
    sys.stdout.buffer.write(b'</html>')

elif method == "GET":
    # Write the default landing page with a file reader.
    sys.stdout.buffer.write(b"<!doctype html>\n<html>\n <meta charset='utf-8'>")
    sys.stdout.buffer.write(b'''
<main>
<h1>Nansen Legacy Data Matrix code reader</h1>
<a href="../index.html">Back to index</a><br>
<p>Choose the image to be read. Analysing takes up to 1 minute.  </p>
<form method="post" enctype="multipart/form-data">
    <input id="fileupload" name="myfile" type="file" />
    <input type="submit" value="Analyse" id="submit" />
</form>
</main>
</html>
''')
