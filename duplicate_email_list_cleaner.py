import csv
import os
import re
# print(csv.__file__)

def append_list(file_path,email):
	with open(file_path,'a',newline='') as newcsv:
		fieldnames = ['email']
		writer = csv.DictWriter(newcsv,fieldnames=fieldnames)
		writer.writerow(
				{
					"email": email
				}

			)



# Make a regular expression 
# for validating an Email 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
      
# Define a function for 
# for validating an Email 
def valid_email(email):  
  
    # pass the regualar expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True
    else:
    	return False
          
      


files = 'files/emails.csv'
new_file = 'files/emails_new.csv'
if os.path.isfile(new_file):
	pass
else:
	with open (new_file,'a'):
		pass


with open(files,"r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter="\n")
    i = 1
    for email in csv_reader:
    	# print(email)
    	with open(new_file,"r"):
    		reader = csv.reader(new_file)
    		list_reader = list(reader)

    		if email not in list_reader:
		    	if (len(email) > 0):
		    				email_address = email[0].strip()
				    		if (len(email_address) > 0):
						    	append_list(new_file,email_address)
						    	print(i , " ", email_address ,"...")
						    	i+=1
				    		else:
				    			print(email[0] , "not a valid email address")
				    			continue
		    	else:
		    		print(email , "index length 0")
		    		continue
    		else:
    			print(email , "duplicate email address")
    			continue


