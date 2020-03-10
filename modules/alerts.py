import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import tweepy
import datetime


def send_alerts(hotel_room_objects, config):
    for hotel_room in hotel_room_objects:
        if config.alerts_email:
            send_email_alert(hotel_room, config)
        if config.alerts_sms:
            send_sms_alert(hotel_room, config)
        if config.alerts_twitter:
            send_twitter_alert(hotel_room, config)


def send_email_alert(hotel_room, config):
    for sendto_target in config.email_send_to:
        message = """\
        New Hotel Found\n\n
        Hotel - {0}\n
        Distance - {1}\n
        Total Stay Price - {2}\n
        Inventory Available - {3}\n
        Type of Room - {4}""".format(hotel_room.name, hotel_room.distance, hotel_room.price, hotel_room.inventory,
                                     hotel_room.roomtype)

        msg = MIMEText(message, 'plain')
        msg['Subject'] = "Gencon Hotel Alert"
        msg['From'] = config.email_from_user
        msg['To'] = sendto_target

        try:
            server = smtplib.SMTP_SSL(config.email_smtp_server, config.email_smtp_port)
            server.ehlo()
            server.login(config.email_from_user, config.email_from_password)
            server.sendmail(config.email_from_user, sendto_target, msg.as_string())
            server.quit()
        except Exception as e:
            print("Can't send email to {0}".format(sendto_target))
            print(e)


def send_sms_alert(hotel_room, config):
    message = "Hotel Alert\n{0}\n{1}\nPrice - {2}\n Avail - {3}\n Type - {4}".format(hotel_room.name,
                                                                                     hotel_room.distance,
                                                                                     hotel_room.price,
                                                                                     hotel_room.inventory,
                                                                                     hotel_room.roomtype)
    client = Client(config.sms_twilio_sid, config.sms_twilio_auth)
    for phone_number in config.sms_to_numbers:
        try:
            client.messages.create(
                from_=config.sms_from_number,
                body=message,
                to=phone_number
            )
        except Exception as e:
            print("Could not send SMS to {0}".format(phone_number))
            print(e)


def post_to_twitter(tweet_string, config):
    auth = tweepy.OAuthHandler(config.twitter_consumer_key, config.twitter_consumer_secret)
    auth.set_access_token(config.twitter_access_token, config.twitter_access_token_secret)
    api = tweepy.API(auth)
    api.update_status(tweet_string)


def send_twitter_alert(hotel_room, config):
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    message = "Gencon Hotel Alert\n{0}\n{1}\n{2}".format(date_time, hotel_room.name, hotel_room.roomtype)
    post_to_twitter(message, config)
