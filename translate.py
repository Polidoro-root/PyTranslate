import http.client
import json
from dotenv import load_dotenv
import os

load_dotenv()

text = str(input("What word do you want to translate?\n"))

spaceReplace = text.replace(" ", "%20")
commaReplace = spaceReplace.replace(",", "%2C")
formatedText = commaReplace.replace('"', "%22")

HOST = os.getenv("X_RAPIDAPI_HOST")
API_KEY = os.getenv("X_RAPIDAPI_KEY")

conn = http.client.HTTPSConnection(HOST)

payload = f"q={formatedText}&source=en&target=pt"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': HOST
    }

conn.request("POST", "/language/translate/v2", payload, headers)

res = conn.getresponse()
data = res.read()
dictData = json.loads(data.decode("utf-8"))
translatedText = dictData['data']['translations'][0]['translatedText']

print(translatedText)
