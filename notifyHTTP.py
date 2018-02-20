import os, sys, datetime
import notify_robot as n

path_dir = "/grafometria/out"
hora_agora = datetime.datetime.today().strftime('%Y%m%d%H%M%S')

def list_files_on_directory(path_dir):
	lista = []
	for root, directories, filenames in os.walk(path_dir):
	    for filename in filenames:
	    	lista.append(filename)       
	        print (filename)
	return lista

print (' --- Starting Notify [%s]--- ' % hora_agora)

lista = list_files_on_directory(path_dir)
for zip_file in lista:
	notify = n.notify_robot(zip_file.split(".")[0], ('\\\\123.151.221.36\\grafo\\out\\%s' % zip_file))
	print ('['+ hora_agora + ']--'+  zip_file,'notify => %s' % notify)

print ' --- Notify concluido --- '
print ''
