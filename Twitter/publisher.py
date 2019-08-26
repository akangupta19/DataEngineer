import argparse
import  pandas
import twitter_real as tw
import teststreaming as t
project_id = "serene-vehicle-247610"
topic_name = "FiTopic"
subscription_name = "FiSubc"


from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_name}`
topic_path = publisher.topic_path(project_id, topic_name)


def publish_messages(project_id, topic_name):




    data =str(t.on_data())
    print(type(data))

        # Data must be a bytestring
    data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data)
    print(future.result())


print('Published messages.')
    # [END pubsub_quickstart_publisher]
    # [END pubsub_publish]

publish_messages('serene-vehicle-247610', 'FiTopic')

