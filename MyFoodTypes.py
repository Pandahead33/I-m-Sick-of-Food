import json
import random

def lambda_handler(event, context):

    if (event["session"]["application"]["applicationId"] !=
            "amzn1.ask.skill.d04ccc49-440f-42c5-89f8-cb63b30d0884"):
        raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "GetFoodType":
        return get_food_type(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_started(session_started_request, session):
    print "Starting new session."

def on_session_ended(session_ended_request, session):
    print "Session over."

def handle_session_end_request():
    card_title = "I'm Sick of Food - Bye!"
    speech_output = "Spin again soon!"
    should_end_session = True
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))

def get_welcome_response():
    session_attributes = {}
    card_title = "I'm Sick of Food"
    speech_output = "Welcome to I'm Sick of Food, an Alexa skill! " \
                    "You can ask me for a type of food to eat! "
    reprompt_text = "Please ask me to spin!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def get_food_type(intent):
    session_attributes = {}
    card_title = "I'm Sick of Food Types"
    reprompt_text = "It's a wash! Try yelling spin instead."
    should_end_session = False


    foodtypes = []
    foodtypes.append("BBQ")
    foodtypes.append("American")
    foodtypes.append("Seafood")
    foodtypes.append("Sandwiches")
    foodtypes.append("Italian")
    foodtypes.append("Pizza")
    foodtypes.append("Burgers")
    foodtypes.append("Steakhouse")
    foodtypes.append("Diner")
    foodtypes.append("Mexican")
    foodtypes.append("at Home")
    foodtypes.append("Caribbean")
    foodtypes.append("Mediterranean")
    foodtypes.append("French")
    foodtypes.append("Indian")
    foodtypes.append("Thai")
    foodtypes.append("Chinese")
    foodtypes.append("Breakfast")

    randfoodtype = random.randrange(0, 19)
    speech_output = "You should eat " + foodtypes[randfoodtype] + "!"

    reprompt_text = ""

    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
