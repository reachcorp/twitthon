import os

# KAFKA
#kafka_endpoint = str(os.environ["KAFKA_IP"]) + ":" + str(os.environ["KAFKA_PORT"])
#topic_in = os.environ["TOPIC_IN"]
#topic_to_colissithon = os.environ["TOPIC_TO_COLISSITHON"]
kafka_endpoint = "192.168.0.31:8092"
topic_in = "tweethon_in"
topictweet_out="topictweet_out"
topicmedia_out="topicmedia_out"
limit=10

#chemin
#outputtweet_user = os.environ["OUTPUTTWEET_USER"]
#outputmedia_user = os.environ["OUTPUTMEDIA_USER"]
#outputtweet_keywords = os.environ["OUTPUTTWEET_KEYWORDS"]
#outputmedia_keywords = os.environ["OUTPUTMEDIA_KEYWORDS"]
outputtweet_user = "timeline/json"
outputmedia_user = "timeline/media"
outputtweet_keywords = "keywords/json",
outputmedia_keywords = "keywords/media"

# LOGS LEVEL
#debug_level = os.environ["DEBUG_LEVEL"]
debug_level = "INFO"