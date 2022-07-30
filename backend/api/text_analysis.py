from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def azure_analysis(text):
    subscription_key = '579dc05cf2784bb1bfc6e9490f593cdc'
    credential = AzureKeyCredential(subscription_key)
    text_analytics_client = TextAnalyticsClient(endpoint="https://eastus.api.cognitive.microsoft.com/", credential=credential)

    entities = {}
    customers = []
    #text = open('customers.txt', encoding='utf8').read()
    customers.append(text)
    print(customers)


    response = text_analytics_client.recognize_entities(customers, language="en")
    result = [doc for doc in response if not doc.is_error]

    for doc in result:
        print(len(doc.entities))
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("...Category: {}".format(entity.category))
            entities[entity.text] = entity.category
            #print("...Confidence Score: {}".format(entity.confidence_score))
            #print("...Offset: {}".format(entity.offset))
    return entities

