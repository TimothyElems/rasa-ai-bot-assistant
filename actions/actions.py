# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"
# from typing import Text, List, Any, Dict, Union

# from rasa_sdk import Tracker, FormValidationAction, Action
# from rasa_sdk.events import EventType
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
# from rasa_sdk.events import SlotSet, UserUtteranceReverted


# # class RedirectWebsiteAction(Action):
# #     def name(self) -> Text:
# #         return "action_redirect_website"

#     # def run(
#     #     self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
#     # ) -> List[Dict[Text, Any]]:
#     #     # Extract the payload from the latest user message
#     #     payload = tracker.latest_message.get("payload")

#     #     if payload == "/visit_amazon":
#     #         # Redirect the user to the desired webpage
#     #         website_url = "https://www.amazon.com"
#     #         dispatcher.utter_message("Redirecting you to Amazon website...")
#     #         dispatcher.utter_message({"redirect_to_website": website_url})

#     #     elif payload == "/visit_lowes":
#     #         # Redirect the user to the desired webpage
#     #         website_url = "https://www.lowes.com"
#     #         dispatcher.utter_message("Redirecting you to Lowe's website...")
#     #         dispatcher.utter_message({"redirect_to_website": website_url})

#     #     # Return an empty list to finish the action
#     #     return []
       
     
# ALLOWED_PIZZA_SIZES = [
#     "small",
#     "medium",
#     "large",
#     "extra-large",
#     "extra large",
#     "s",
#     "m",
#     "l",
#     "xl",
# ]
# ALLOWED_PIZZA_TYPES = ["mozzarella", "fungi", "veggie", "pepperoni", "hawaii"]
# VEGETARIAN_PIZZAS = ["mozzarella", "fungi", "veggie"]
# MEAT_PIZZAS = ["pepperoni", "hawaii"]


# class ValidateSimplePizzaForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_simple_pizza_form"

#     def validate_pizza_size(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `pizza_size` value."""
           
#         if slot_value.lower() not in ALLOWED_PIZZA_SIZES:
#             dispatcher.utter_message(text=f"We only accept pizza sizes: s/m/l/xl.")
#             return {"pizza_size": None}
#         dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
#         return {"pizza_size": slot_value}

#     def validate_pizza_type(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `pizza_type` value."""

#         if slot_value not in ALLOWED_PIZZA_TYPES:
#             dispatcher.utter_message(
#                 text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}."
#             )
#             return {"pizza_type": None}
#         dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
#         return {"pizza_type": slot_value}


# class AskForVegetarianAction(Action):
#     def name(self) -> Text:
#         return "action_ask_vegetarian"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
        



#         dispatcher.utter_message(
#             text="Would you like to order a vegetarian pizza?",
#             buttons=[
#                 {"title": "yes", "payload": "/affirm"},
#                 {"title": "no", "payload": "/deny"},
#             ],
#         )
#         return []


# class AskForPizzaTypeAction(Action):
#     def name(self) -> Text:
#         return "action_ask_pizza_type"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         if tracker.get_slot("vegetarian"):
#             dispatcher.utter_message(
#                 text=f"What kind of pizza do you want?",
#                 buttons=[{"title": p, "payload": p} for p in VEGETARIAN_PIZZAS],
#             )
#         else:
#             dispatcher.utter_message(
#                 text=f"What kind of pizza do you want?",
#                 buttons=[{"title": p, "payload": p} for p in MEAT_PIZZAS],
#             )
#         return []


# class ValidateFancyPizzaForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_fancy_pizza_form"

#     def validate_vegetarian(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `pizza_size` value."""
#         if tracker.get_intent_of_latest_message() == "affirm":
#             dispatcher.utter_message(
#                 text="I'll remember you prefer vegetarian."
#             )
#             return {"vegetarian": True}
#         if tracker.get_intent_of_latest_message() == "deny":
#             dispatcher.utter_message(
#                 text="I'll remember that you don't want a vegetarian pizza."
#             )
#             return {"vegetarian": False}
#         dispatcher.utter_message(text="I didn't get that.")
#         return {"vegetarian": None}

#     def validate_pizza_size(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `pizza_size` value."""

#         if slot_value not in ALLOWED_PIZZA_SIZES:
#             dispatcher.utter_message(text=f"We only accept pizza sizes: s/m/l/xl.")
#             return {"pizza_size": None}
#         dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
#         return {"pizza_size": slot_value}

#     def validate_pizza_type(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `pizza_type` value."""

#         if slot_value not in ALLOWED_PIZZA_TYPES:
#             dispatcher.utter_message(
#                 text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}."
#             )
#             return {"pizza_type": None}
#         if not slot_value:
#             dispatcher.utter_message(
#                 text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}."
#             )
#             return {"pizza_type": None}
#         dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
#         return {"pizza_type": slot_value}