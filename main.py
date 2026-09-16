import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "YOURgsk_AWmVuCpCOzk2kzsju8GMWGdyb3FY09E7xB7dWaOGRL7butJ4Rw6L_NEW_API_KEY"

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

print("Client created successfully!")