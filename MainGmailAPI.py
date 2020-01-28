import base64
import pickle
import os.path
import View
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def mainConnect():
    global service, ErrorCounter
    ErrorCounter=0
    try:
        creds = None
        if os.path.exists('token.key'):
            with open('token.key', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.key', 'wb') as token:
                pickle.dump(creds, token)
        service = build('gmail', 'v1', credentials=creds)
        print("Connection : Success")
    except:
        print("Cannot Connected To Gmail Quckstart API")
        ErrorCounter=1
            
def getLabel():
    if ErrorCounter!=1:    
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        print (labels)
        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'],end='\t')

def getInfo():
    if ErrorCounter!=1:    
        t=service.users().getProfile(userId='me').execute()
        print ("\t\tinformation\t\t")
        for i in t:
            print ("%s \t\t : %s" % (i,t[i]))
        
def MessageRetrive(From=0,To=0,label=None):
    if ErrorCounter!=1:    
        listMessageId=service.users().messages().list(userId='me',
                                                      labelIds=label,
                                                      includeSpamTrash=False).execute()
        listMessageId=listMessageId["messages"]
        for counterId in range(From,To):
            print("\n\t\tMessages\n")
            Ids=listMessageId[counterId]
            jsonGetMessage=service.users().messages().get(userId='me',
                                                          id=Ids['id'],
                                                          format='metadata',
                                                          metadataHeaders=["To","From","Subject"]).execute()
            
            messageHeaders=jsonGetMessage['payload']['headers']
            
            for counter in range(len(messageHeaders)):
                print("%s\t\t:%s"%(messageHeaders[counter]['name'],
                                   messageHeaders[counter]['value']))
            print("Status\n\tBaca\t\t:%s"%(jsonGetMessage['labelIds'][0]))
            print("\tKategori\t:%s"%(jsonGetMessage['labelIds'][1]))
            print("\tLabel\t\t:%s\n"%(jsonGetMessage['labelIds'][2]))
            pesan=None
            try:
                pesan = SelectedMessage(ids=Ids['id'])
                print("=====message=====\n%s"%SelectedMessage(ids=Ids['id']))
            except:
                pass
            finally:
                print("end")
            iSubject     = messageHeaders[0]['value']
            iFrom        = messageHeaders[1]['value']
            iTo          = messageHeaders[2]['value']
            iBaca        = jsonGetMessage['labelIds'][0]
            iKategori    = jsonGetMessage['labelIds'][1]
            iLabel       = jsonGetMessage['labelIds'][2]
            iMail        =pesan
            View.vp_start_gui(iFrom,iTo,iSubject,iBaca,iKategori,iLabel,iMail)
def SelectedMessage(ids=None):
    if ErrorCounter!=1:    
        jsonGetMessage=service.users().messages().get(userId='me',
                                                      id=ids,
                                                      format='full',
                                                      metadataHeaders=["To","From","Subject"]).execute()
        message=(base64.urlsafe_b64decode(jsonGetMessage['payload']['parts'][0]['body']['data'].encode('ASCII'))).decode('utf-8')
        return message

def logout():
    import os
    os.remove("token.key")

if __name__ == '__main__':
    mainConnect()
    getInfo()
    MessageRetrive(From=0,To=2,label="SPAM")
    getLabel()
    
