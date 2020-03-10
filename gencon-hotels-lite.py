from configparser import ConfigParser
import time
import modules


try:
    configfilename = "./gencon-hotels-lite.cfg"
    config = ConfigParser()
except Exception as e:
    print("Unable to load config file - please verify it exists and is named 'gencon-hotels-lite.cfg'")
    print(e)
    exit(1)

try:
    config.read(configfilename)
except Exception as e:
    print("Unable to read config file")
    print(e)
    exit(1)

alerts_triggered = 0


while True:
    try:
        gchotels_config = modules.create_config_object(config)
        date_range = modules.all_dates_list(gchotels_config.check_in, gchotels_config.check_out)
        hotel_room_json = modules.get_hotel_room_objects(gchotels_config)
        hotel_room_objects = modules.hotel_room_parser(hotel_room_json, gchotels_config)
        hotel_room_objects = modules.filter_hotel_room_objects(hotel_room_objects, gchotels_config)
        if (gchotels_config.alerts_email or gchotels_config.alerts_sms or gchotels_config.alerts_twitter) \
                and hotel_room_objects:
            modules.send_alerts(hotel_room_objects, gchotels_config)
            alerts_triggered = 1
        modules.clear()
        print(modules.table_creation(hotel_room_objects))
        if alerts_triggered == 1:
            time.sleep(60)
            alerts_triggered = 0
        else:
            time.sleep(gchotels_config.check_frequency)
    except Exception as e:
        print(e)
        exit(1)
