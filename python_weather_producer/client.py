from kafka import KafkaProducer, KafkaConsumer
import json

KAFKA_BROKERS: str = (
    "strimzi-kafka-bootstrap.kafka:9092"  # <service name>.<namepsace>:<port>
)

DEFAULT_TOPIC: str = "WEATHER"
DEFAULT_ENCODING: str = "utf-8"
DEFAULT_CONSUMER: str = "DEFAULT_CONSUMER"


def get_producer() -> KafkaProducer:
    return KafkaProducer(bootstrap_servers=[KAFKA_BROKERS])


def get_consumer(topic: str, group_id: str = None) -> KafkaConsumer:
    if group_id is None:
        group_id = DEFAULT_CONSUMER
    return KafkaConsumer(topic, bootstrap_servers=[KAFKA_BROKERS], group_id=group_id)

def send_avro_msg(value, topic: str, producer: KafkaProducer):
    producer.send(topic, value)