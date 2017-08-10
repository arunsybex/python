import MySQLdb as mdb
import sys
from PIL import Image
import base64
import cStringIO
import PIL.Image
import urllib

db = mdb.connect('localhost', 'root', 'root', 'test')
URL = "http://phishtank-screenshots.e1.usw1.opendns.com.s3-website-us-west-1.amazonaws.com/5146405.jpg";
image_content = urllib.urlopen(URL).read();
save_dir = "C://Users/arunkumar.2160/Desktop/pixm/"+URL.split(".com/")[1];
f = open(save_dir,'wb')
f.write(image_content)
f.close()
image = Image.open(save_dir)

blob_value = open(save_dir, 'rb').read()
sql = 'INSERT INTO img(images) VALUES(%s)'    
args = (blob_value, )
cursor=db.cursor()
cursor.execute(sql,args)
sql1='select * from img'
db.commit()
cursor.execute(sql1)
data=cursor.fetchall()
print data
file_like=cStringIO.StringIO(data[0][1])
img=PIL.Image.open(file_like)
img.show()

db.close()