import modules


class Configuration(object):
    event_id = ""
    owner_id = ""


gchotels_config = Configuration()


def create_config_object(config):
    gchotels_config.event_id = (config["target-config"])["event-id"]
    gchotels_config.owner_id = (config["target-config"])["owner-id"]
    gchotels_config.housing_token = (config["account-config"])["housing-token"]
    gchotels_config.housing_authstring = (config["account-config"])["housing-authstring"]
    gchotels_config.check_frequency = int((config["account-config"])["check-frequency"])
    gchotels_config.check_in = (config["search-filters"])["check-in"]
    gchotels_config.check_out = (config["search-filters"])["check-out"]
    gchotels_config.search_skywalk = modules.string_to_bool((config["search-filters"])["search-skywalk"])
    gchotels_config.search_blocks = modules.string_to_bool((config["search-filters"])["search-blocks"])
    if gchotels_config.search_blocks:
        gchotels_config.search_blocks_max = int((config["search-filters"])["max-blocks"])
    gchotels_config.search_miles = modules.string_to_bool((config["search-filters"])["search-miles"])
    if gchotels_config.search_miles:
        gchotels_config.search_miles_max = int((config["search-filters"])["max-miles"])
    gchotels_config.filter_hotelname = modules.string_to_bool((config["search-filters"])["hotel-name-filter-enabled"])
    if gchotels_config.filter_hotelname:
        gchotels_config.filter_hotelname_keyword = (config["search-filters"])["hotel-name-filter-keyword"]
    gchotels_config.filter_room = modules.string_to_bool((config["search-filters"])["hotel-room-filter-enabled"])
    if gchotels_config.filter_room:
        gchotels_config.filter_room_include = (config["search-filters"])["hotel-room-filter-include"]
        gchotels_config.filter_room_exclude = (config["search-filters"])["hotel-room-filter-exclude"]
    gchotels_config.alerts_email = modules.string_to_bool((config["alerts-config"])["send-email"])
    if gchotels_config.alerts_email:
        gchotels_config.email_from_user = (config["email-send-config"])["from-user"]
        gchotels_config.email_from_password = (config["email-send-config"])["from-password"]
        gchotels_config.email_send_to = modules.string_to_list((config["email-send-config"])["send-to"])
        gchotels_config.email_smtp_server = (config["email-send-config"])["smtp-server"]
        gchotels_config.email_smtp_port = (config["email-send-config"])["smtp-port"]
    gchotels_config.alerts_sms = modules.string_to_bool((config["alerts-config"])["send-sms"])
    if gchotels_config.alerts_sms:
        gchotels_config.sms_twilio_sid = (config["sms-send-config"])["twilio-account-sid"]
        gchotels_config.sms_twilio_auth = (config["sms-send-config"])["twilio-account-auth"]
        gchotels_config.sms_from_number = (config["sms-send-config"])["from-number"]
        gchotels_config.sms_to_numbers = modules.string_to_list((config["sms-send-config"])["to-numbers"])
    gchotels_config.alerts_twitter = modules.string_to_bool((config["alerts-config"])["send-twitter"])
    if gchotels_config.alerts_twitter:
        gchotels_config.twitter_consumer_key = (config["twitter-send-config"])["twitter-consumer-key"]
        gchotels_config.twitter_consumer_secret = (config["twitter-send-config"])["twitter-consumer-secret"]
        gchotels_config.twitter_access_token = (config["twitter-send-config"])["twitter-access-token"]
        gchotels_config.twitter_access_token_secret = (config["twitter-send-config"])["twitter-access-token-secret"]
    return gchotels_config
