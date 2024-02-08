import requests

from access_token import generate_access_token
from encode import generate_password
from utils import get_timestamp
import keys



def lipa_na_mpesa(): 
    access_token=generate_access_token()
    formatted_time=get_timestamp()
    decoded_password = generate_password(formatted_time)
    api_url="https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"


    headers={"Authorization": "Bearer %s" % access_token}
    print(f"Headers: {headers}")

    request = {
                "BusinessShortCode": keys.business_short_code,
                "Password": decoded_password,
                "Timestamp": formatted_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": "1",
                "PartyA": keys.phone_number,
                "PartyB": keys.business_short_code,
                "PhoneNumber": keys.phone_number,
                "CallBackURL": "https://fsdj.vercel.app/api/payments/lnm/",
                "AccountReference": " BQ001",
                "TransactionDesc": "Pay Bwana Q"
            }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)

lipa_na_mpesa()