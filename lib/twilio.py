from datetime import datetime, timedelta
from twilio.rest import Client


class TwilioService:
    def __init__(self, account_sid, auth_token, twilio_phone_number):
        self.client = Client(account_sid, auth_token)
        self.twilio_phone_number = twilio_phone_number

    def send_confirmation(self, customer_phone_number):
        # Calculate delivery time as 1 hour after the current real-time
        delivery_time = datetime.now() + timedelta(hours=1)
        delivery_time_str = delivery_time.strftime('%H:%M')

        message = self.client.messages.create(
            body=f"Thank you! Your order was placed and will be delivered before {delivery_time_str}.",
            from_=self.twilio_phone_number,
            to=customer_phone_number
        )

        return message.sid