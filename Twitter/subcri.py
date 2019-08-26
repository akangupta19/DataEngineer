import argparse
import time
from google.cloud import pubsub_v1

project_id = "serene-vehicle-247610"
topic_name = "FiTopic"
subscription_name = "FiSubc"

def receive_messages(project_id, subscription_name):
    data_tosendto_bg = []
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
    project_id, subscription_name)
    print('Listening for messages on {}'.format(subscription_path))
    response = subscriber.pull(subscription_path, max_messages=5)

    for msg in response.received_messages:
       output=str(msg.message.data)
       print(output)

   # print("Received message:", data['Time Series (1min)'].items())
    #for item in  data['Time Series (1min)'].items():
    data_tosendto_bg.append(output[1])

    ack_ids = [msg.ack_id for msg in response.received_messages]
    subscriber.acknowledge(subscription_path, ack_ids)

    # subscriber = pubsub_v1.SubscriberClient()
    # subscription_path = subscriber.subscription_path(
    # project_id, subscription_name)
    #
    # def callback(message):
    # global mesg
    # mesg = message.data
    # print('Received message: {}'.format(message))
    # message.ack()
    #
    # future = subscriber.subscribe(subscription_path, callback=callback)
    # print('Listening for messages on {}'.format(subscription_path))
    #
    # try:
    # future.result()
    # except KeyboardInterrupt:
    # future.cancel()

    # while True:
    # time.sleep(60)
    return data_tosendto_bg

receive_messages('serene-vehicle-247610', 'FiSubc')
