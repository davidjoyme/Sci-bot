


# This is a simple example for a custom action which utters "Hello World!"
import wikipedia
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
#
#

wiki_wiki = wikipediaapi.Wikipedia('en')

class ActionGetInfo(Action):
#
     def name(self) -> Text:
         return "action_get_info"
#
     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
           
        topic_name = tracker.get_slot('topic')
        print(type(topic_name))
        print(topic_name + "+science")
        print(wikipedia.summary(topic_name + "+science", sentences=4))
        info=wikipedia.summary(topic_name + "+(science)")
        dispatcher.utter_message(info)

        return [SlotSet('topic', topic_name)]


