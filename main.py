from CoreMSG import CoreMSG
from weather import Weather
from datetime import datetime
from threading import Timer
import time

user = CoreMSG('email', 'passwd')


cr_weather = Weather('city', 'API')

target_ = 'Target FBID'

print(cr_weather.weather_wind())


def check_conditions():
    active_emoji = 'none'

    if cr_weather.weather_temp() and active_emoji != 'temp' >= 30.0:
        user.change_emoji(CoreMSG.emoji['sun'], target_, 'The temperature outside is over 30degrees celsius')
        active_emoji = 'temp'

    elif cr_weather.is_it_night() and active_emoji != 'night':
        user.change_emoji(CoreMSG.emoji['night'], target_, 'It''s night time right now, so have a nice emoji')
        active_emoji = 'night'

    elif cr_weather.weather_snow() and active_emoji != 'snow':
        user.change_emoji(CoreMSG.emoji['snow'], target_, 'It''s snowing outside!')
        active_emoji = 'snow'

    elif cr_weather.weather_rain() and active_emoji != 'rain':
        user.change_emoji(CoreMSG.emoji['rain'], target_, 'It looks like it''s raining outside')
        active_emoji = 'rain'

    elif cr_weather.weather_rain() and active_emoji != 'wind':
        user.change_emoji(CoreMSG.emoji['wind'], target_, 'It looks like it''s a little bit windy outside')
        active_emoji = 'wind'

    elif active_emoji != 'nice':
        user.change_emoji(CoreMSG.emoji['rainbow'], target_, 'It''s a nice day outside!')
        active_emoji = 'nice'


class MultiTime:
    def __init__(self, time_, func):
        self.time_ = time_
        self.func = func
        self.thread = Timer(self.time_, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.time_, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


thread_ = MultiTime(1800, check_conditions)
thread_.start()
