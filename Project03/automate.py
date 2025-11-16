# extract email address
import re

def find_emails(text):
  """
  Finds all email addresses in a given string.
  """

  email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
 
  return re.findall(email_pattern, text)

def check_all_email():
    valid_email=[]
    # file location
    
    with open("Project03/data.txt","+r") as f:
        data=f.read()
        # reading
        x=find_emails(data)
        # validiating
        valid_email.extend(x)
        
            
            # file creating
    with open("Project03/email.txt","x") as f:
        f.write(f"\n".join(valid_email))
    
            
check_all_email()