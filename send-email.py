import base64
import httplib2
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools
import xlrd


#Path of excel sheet
EXCEL_SHEET_PATH = ("test.xlsx")

#work book of excel
WorkBook = xlrd.open_workbook(EXCEL_SHEET_PATH) 

#excel sheet
Excel_Sheet = WorkBook.sheet_by_index(0) 
Excel_Sheet.cell_value(0, 0)

# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = 'credentials.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.compose'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
  credentials = tools.run_flow(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)


for i in range(0, Excel_Sheet.nrows):
  name_of_candidate = Excel_Sheet.row_values(i)[0]
  print(name_of_candidate)
  text_msg = """\
Hey """+ name_of_candidate +""" ,

Thanks.

Regards,
Ravi    
"""

  # create a message to send
  message = MIMEText(text_msg)
  message['to'] = Excel_Sheet.row_values(i)[1] #replace to email Id
  message['from'] = "Zauba Cloud <akarsh@zauba.company>" #replace from email Id
  message['subject'] = "Zauba Cloud Interview - Schedule Request" #replace the subject
  body = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

  # send it
  try:
    message = (gmail_service.users().messages().send(userId="me", body=body).execute())
    print('Message Id: %s' % message['id'])
    print(message)
  except Exception as error:
    print('An error occurred: %s' % error)
