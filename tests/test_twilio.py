from unittest.mock import Mock
from unittest.mock import Mock, call, ANY
from lib.twilio import TwilioService


def test_confirmation_message():
    twilio = TwilioService(account_sid="your_account_sid", auth_token="your_auth_token", twilio_phone_number="your_twilio_number")
    twilio_client_mock = Mock()
    message_mock = Mock()
    message_mock.sid = "mock_sid"
    twilio_client_mock.messages.create.return_value = message_mock
    twilio.client = twilio_client_mock
    result = twilio.send_confirmation(customer_phone_number="customer_phone_number")
    assert result == "mock_sid"

    twilio_client_mock.messages.create.assert_called_once_with(
        body=ANY,
        from_="your_twilio_number",
        to="customer_phone_number"
    )