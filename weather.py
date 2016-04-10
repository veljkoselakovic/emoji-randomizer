import pyowm
from datetime import datetime, time


def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


class Weather(object):
    def __init__(self, place, API):
        self.place = place
        self.API = API

    def connect_to_weather(self):
        owm = pyowm.OWM(self.API)
        observation = owm.weather_at_place(self.place)
        weather = observation.get_weather()
        return weather

    def weather_status(self):
        weather_ = self.connect_to_weather()
        status = weather_.get_status()
        return status

    def weather_city(self):
        return self.place

    def weather_wind(self):
        weather_ = self.connect_to_weather()
        wind = weather_.get_wind()
        if wind['speed'] > 30.0:
            return True
        else:
            return False

    def weather_temp(self):
        weather_ = self.connect_to_weather()
        temp = weather_.get_temperature('celsius')
        return temp['temp']

    def weather_rain(self):
        weather_ = self.connect_to_weather()
        rain = weather_.get_rain()
        if rain['3h'] == 0:
            return False
        else:
            return True
    def weather_snow(self):
        weather_ = self.connect_to_weather()
        snow = weather_.get_snow()
        if snow:
            return True
        else:
            return False

    def sunset_time(self):
        weather_ = self.connect_to_weather()
        sunset = weather_.get_sunset_time('iso')
        return sunset

    def sunrise_time(self):
        weather_ = self.connect_to_weather()
        sunrise = weather_.get_sunrise_time('iso')
        return sunrise

    def is_it_night(self):
        now = datetime.now()
        now_time = now.time()
        sunset_time_ = self.sunset_time()
        sunrise_time_ = self.sunrise_time()

        hours_sunset = int(sunset_time_[11]) * 10 + int(sunset_time_[12]) + 2
        minutes_sunset = int(sunset_time_[14]) * 10 + int(sunset_time_[15])

        hours_sunrise = int(sunrise_time_[11]) * 10 + int(sunrise_time_[12]) + 2
        minutes_sunrise = int(sunrise_time_[14]) * 10 + int(sunrise_time_[15])

        if time_in_range(time(hours_sunset, minutes_sunset), time(hours_sunrise, minutes_sunrise), now_time):
            return True
        else:
            return False
