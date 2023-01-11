from twilio.rest import Client 

def sendText(phoneNum, message):
    account_sid = 'AC4516245caef9cb20ffffe78a3f264402' 
    auth_token = '744969fa9fae703b3e9a5af3863b29f1' 
    client = Client(account_sid, auth_token) 

    editedNum = "+1" + phoneNum
 
    message = client.messages.create(from_='+17208159342', body=message, to=editedNum) 
 







import mysql.connector
from mysql.connector import errorcode

def executeStmt(query):
    
    print("recieved executeStmt")
    # Establish a connection to the MySQL server
    cnx = mysql.connector.connect(
        host="boulder.ch3d33yazhdx.us-west-2.rds.amazonaws.com",
        user="admin",
        password="Password",
        database="boulder"
    )

    # Create a cursor object
    cursor = cnx.cursor()

    # Execute the query
    cursor.execute(query)

    # Commit the changes
    cnx.commit()
    print("query committed")

    # Close the cursor and connection
    cursor.close()
    cnx.close()


def obtainNumbers(sportid):
    numbersList = []
    return numbersList

phrasee = {"MBH": "The Men's basketball team will be playing in 1 hour. Head to the Boulder High gym to support them against "}


def start(id, opponent):

    messageBody = phrasee[id] + opponent

    numbers = obtainNumbers(id)

    for x in numbers:
        sendText(x, messageBody)
