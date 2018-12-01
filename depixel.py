import subprocess,os,sys
#input=("")
#print (sys.argv[0])
Command="potrace "+ sys.argv[1] +" -b pdf"
os.system(Command)
