__author__ = 'xiangyuzhang'
from subprocess import call

camlist = ["c499-mux4-1.v", "c499-mux4-11.v", "c499-mux4-21.v", "c499-mux4-31.v", "c499-mux4-41.v", "c499-mux4-51.v",
           "c499-mux4-61.v", "c880-mux4-1.v", "c880-mux4-11.v","c880-mux4-21.v", "c880-mux4-31.v","c880-mux4-41.v",
           "c880-mux4-51.v", "c880-mux4-61.v"]
for i in camlist:
    camd = "python XOR_Cam.py " + i
    call(camd, shell = True)