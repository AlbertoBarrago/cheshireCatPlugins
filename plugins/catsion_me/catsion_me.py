from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
import random


class MySettings(BaseModel):
    humor: str = "Funny"


@plugin
def settings_schema():
    return MySettings.schema()


@hook(priority=0)
def agent_prompt_prefix(prefix, cat):
    prefix = """You are the magic hatter of laughter, your every action aimed at ensuring a sympathetic yet 
    productive experience. as first ask what language the user wants to use whether Italian . then you ask for make a 
    social media post or a joga post for telegram"""
    return prefix


@tool
def create_social_media_post_caption(when, where, what):
    """ Triggered by "creare una caption per un social media" or "make a social media caption" """
    adjectives = ["enthusiastic", "excited", "happy", "thrilled"]
    events = ["an unmissable event", "a magical evening", "an incredible show"]
    activities = ["a night of music and fun", "an unforgettable experience", "an extraordinary concert"]
    greetings = ["Join us", "Participate with us", "Enjoy with us"]

    summary = (f"🎵 {where} {random.choice(adjectives)} to present {random.choice(events)} - {what}! "
               f"🎤 {random.choice(greetings)} {when} for {random.choice(activities)}."
               f"The entry is free, so there's no reason to miss out! 🎉 To reserve your spot,"
               f"follow the link in our bio. We look forward to seeing you there! 🙌 #LiveMusic")

    result_by_humor = MySettings.humor + summary

    return result_by_humor


@tool
def create_a_yoga_telegram_post(argument):
    """ Triggered by "create a post for telegram" or "make a post for telegram" """
    message = f"(Create a post for telegram with this {argument} and add icon)"

    return MySettings.humoer + message
