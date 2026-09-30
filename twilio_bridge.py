#!/usr/bin/env python3
import sys, json, os
from twilio.rest import Client
from dotenv import load_dotenv

# Load .env from the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, ".env")) 

# .env: TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER

def outbound_call(phone, msg):
    try:
        sid = os.getenv("TWILIO_SID")
        token = os.getenv("TWILIO_TOKEN")
        number = os.getenv("TWILIO_NUMBER")
        
        if not all([sid, token, number]):
            print("Error: Missing Twilio credentials in .env")
            return

        client = Client(sid, token)
        call = client.calls.create(
            twiml=f'<Response><Say voice="Polly.Joanna">{msg}</Say></Response>',
            to=phone,
            from_=number
        )
        print(f"Call SID: {call.sid}")
    except Exception as e:
        print(f"Error making call: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--call":
        try:
            data = json.loads(sys.argv[2])
            phone = data.get("phone")
            msg = data.get("msg")
            if phone and msg:
                outbound_call(phone, msg)
            else:
                print("Error: Missing phone or msg in payload")
        except json.JSONDecodeError:
            print("Error: Invalid JSON payload")
    else:
        # Fallback/Test mode if just running script directly?
        # Or just print usage
        pass
