This script polls the Gencon housing portal, displays available hotel rooms, and send alerts based upon user preferences.

This is written using Python 3.8, so please make sure you're using a modern version of [Python](https://www.python.org/)

## Getting The Token and Auth String
After logging in to the housing portal via your Gencon profile, you will have a link that looks something like this:

```https://book.passkey.com/reg/32ZABCD-1234/01234567890abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqr```


This section is the value you should use for "housing-token"

```32ZABCD-1234```


This section is the value you should use for "housing-authstring"

```01234567890abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqr```

## Setup
Either clone the script
```bash
git clone https://github.com/overallcoma/gencon-hotels-lite.git
```
Or download the [zip file](https://github.com/overallcoma/gencon-hotels-lite/archive/master.zip)

Or download and run the pre-compiled .exe for Windows users

## Install required packages
```bash
pip install -r requirements.txt
```

## Config File Setup
####You must create your own config file!
####Copy 'gencon-hotels-lite.cfg.example' to 'gencon-hotels-lite.cfg'

Modify the contents of gencon-hotels-lite.cfg to your requirements and save to gencon-hotes-lite.cfg
The parameters do the following:


* `housing-token` - This is your housing token value
* `housing-authstring` = This is your housing auth string
* `check-frequency` = This is how often the script updates the data.  Default is 60.  I highly recommend you don't drop it below 10 or you will likely get errors after a while.
* `check-in` - The date you would like to check in (YYYY-MM-DD)
* `check-out` - The date you would like to check out (YYYY-MM-DD)
* `search-skywalk` - Set the filter to accept the word "Skywalk" for a desired room.  Set to 'true' or 'false'.
* `search-blocks` - Set the filter to accept "Blocks" as an acceptable distance measure.  Set to 'true' or 'false'.
* `max-blocks` - Maximum measure of blocks to have included in the results.  Required if 'search-blocks' is 'true'.
* `search-miles` - Return results that have 'miles' in their distance measure.  Set to 'true' or 'false'. 
* `max-miles` - Maximum measure of miles to have included in the results.  Required if 'search-blocks' is set to 'true'.
* `hotel-name-filter-enabled` - Enable or disable filtering based on name of hotel.  Set to 'true' or 'false'.
* `hotel-name-filter-keyword` - If 'hotel-name-filter-enabled' is set to true, this is required and provided the same to include in the filtered results.
* `hotel-room-filter-enabled` - Enable or disable filtering based on keyword in the room type.  Set to 'true' or 'false'.
* `hotel-room-filter-include` - If 'hotel-room-filter-enabled' is set to 'true', this is required and provides the keyword that is required for a room to be included in search results.
* `hotel-room-filter-exclude` = If 'hotel-room-filter-enabled' is set to 'true', this provides the keyword that excludes a room from search results.

* `send-email` - Enables or Disables the sending of email alerts.  Set to 'true' or 'false'.
* `send-sms` - Enables or Disables the sending of SMS messages.  Set to 'true' or 'false'.
* `send-twitter` - Enables or Disables the sending of Twitter Alerts.  Set to 'true' or 'false'.

* `from-user` - if send-email is set to "true", this is the source from which the alert email will be sent
* `from-password` - if send-email is set to "true", this is the password required for sending email from the "from-user" address
* `send-to` - if send-email is set to "true", this is a list of emails which will receive the alerts.  Please add additional emails seperated with a comman and no spaces.
* `smtp-server` - if send-email is set to "true", this is the smtp server that will be used to send emails.  Gmail is smtp.gmail.com.
* `smtp-port` - if send-email is set to "true", this is the port to use when communicating with the smtp server.  I'd suggest 465.

* `twilio-account-sid` - if "send-sms" is set to true, this is your Twilio Account SID
* `twilio-account-auth` - if "send-sms" is set to true, this is your Twilio Auth Token
* `from-number` - if "send-sms" is set to true, this is the phone number from which the SMS messages will be sent
* `to-numbers` - if "send-sms" is set to true, this is a list of target phone numbers seperated with a comma and no spaces.
For example - "+15555555555,+11231234567"

* `twitter-consumer-key` = if "send-twitter" is set to true, this is your Twitter API Consumer Key
* `twitter-consumer-secret` = if "send-twitter" is set to true, this is your Twitter API Consumer Secret
* `twitter-access-token` = if "send-twitter" is set to true, this is your Twitter API Access Token
* `twitter-access-token-secret` = 	if "send-twitter" is set to true, this is your Twitter API Access Token Secret

Modify this file and save to gencon-hotels-lite.cfg in the same folder as gencon-hotels-lite.py
If you are not using email and/or sms, you can leave the fields blank with the exception of the "true" or "false" values which much be filled in.

## Running the Script

To run the script, open a terminal (Linux, Mac) / command prompt (Windows) and run:

```sh
python gencon-hotels-lite.py
```

Alternatively - a Windows Binary is included
```sh
gencon-hotels-lite.exe
```

## Output

The columns in the script's output are:

* `Hotel Name` -- The name of the hotel found that meets supplied search filters
* `Distance` -- How far away the hotel is. "Skywalk" means the hotel is connected to the ICC by a skywalk.
* `DistancUnit` -- The unit type of the 'Distance' measure.  Usually either '*' for Skywahlk rooms, 'Blocks', or 'Miles'.
* `Room Type` -- The type of room - probably something like "Double/Double" or "King"
* `Price` -- The total price, before taxes/fees. Essentially the nightly rate times the number of nights.
* `Inventory` -- The number of rooms of this type that are available