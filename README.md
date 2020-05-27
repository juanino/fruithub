# fruithub

A small flask app to accept a device checkin for an arduino device
such as the esp8266 and specifically the adafruit huzzah feather esp8266
but should work with any device that can post HTTP.

Sample arduino code from: https://learn.adafruit.com/adafruit-feather-huzzah-esp8266?view=all
You should be able to start the flask app and run the sketch with minor mods.
It does nothing yet, but you can make it read a sensor and pass that value into the post.

For a more complete sensor see https://github.com/juanino/wetfeather

Also inspired by this: https://www.hackster.io/glowascii/getting-started-with-the-feather-huzzah-81fe61
