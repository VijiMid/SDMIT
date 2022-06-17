import pyqrcode 
from pyqrcode import QRCode

s="SDMIT"

url=pyqrcode.create(s)

url.svg("myqr.svg",scale=8) 
