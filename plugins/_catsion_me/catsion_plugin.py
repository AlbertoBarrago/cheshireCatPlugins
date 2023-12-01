from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date
import random


class MySettings(BaseModel):
    required_int: int
    optional_int: int = 69
    required_str: str
    optional_str: str = "meeeoww"
    required_date: date
    optional_date: date = 1679616000


@plugin
def settings_schema():
    return MySettings.schema()


@tool
def instagram_post_summary(when, where, what):
    """ Triggered by "create an Instagram caption" or "make captions for Instagram" """
    adjectives = ["enthusiastic", "excited", "happy", "thrilled"]
    events = ["an unmissable event", "a magical evening", "an incredible show"]
    activities = ["a night of music and fun", "an unforgettable experience", "an extraordinary concert"]
    greetings = ["Join us", "Participate with us", "Enjoy with us"]

    summary = (f"🎵 {where} {random.choice(adjectives)} to present {random.choice(events)} - {what}! "
               f"🎤 {random.choice(greetings)} {when} for {random.choice(activities)}."
               f"The entry is free, so there's no reason to miss out! 🎉 To reserve your spot,"
               f"follow the link in our bio. We look forward to seeing you there! 🙌 #LiveMusic")
    return summary
