import argparse
import time
from google.cloud import pubsub_v1

project_id = "serene-vehicle-247610"
topic_name = "FiTopic"
subscription_name = "FiSubc"

def receive_messages(project_id, subscription_name):
    import time
    from google.cloud import pubsub_v1

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)
    def callback(message):
        print(message)
        print('Received message: {}'.format(message))
        message.ack()
    subscriber.subscribe(subscription_path, callback=callback)

    # The subscriber is non-blocking. We must keep the main thread from
    # exiting to allow it to process messages asynchronously in the background.
    print('Listening for messages on {}'.format(subscription_path))
    while True:
        time.sleep(60)

receive_messages('serene-vehicle-247610', 'FiSubc')