from kafka import KafkaProducer, KafkaConsumer
import json

KAFKA_BROKERS: str = (
    "strimzi-kafka-bootstrap.kafka:9092"  # <service name>.<namepsace>:<port>
)

DEFAULT_TOPIC: str = "INGESTION"
DEFAULT_ENCODING: str = "utf-8"
DEFAULT_CONSUMER: str = "DEFAULT_CONSUMER"


def get_producer() -> KafkaProducer:
    return KafkaProducer(bootstrap_servers=[KAFKA_BROKERS])


def get_consumer(topic: str, group_id: str = None) -> KafkaConsumer:
    if group_id is None:
        group_id = DEFAULT_CONSUMER
    return KafkaConsumer(
        topic,
        bootstrap_servers=[KAFKA_BROKERS],
        group_id=group_id,
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

def send_avro_msg(value, topic: str, producer: KafkaProducer):
    producer.send(topic, value)

def send_msg(value, key: str, topic: str, producer: KafkaProducer) -> None:
    producer.send(
        topic=topic,
        key=key.encode(DEFAULT_ENCODING),
        value=json.dumps(value).encode(DEFAULT_ENCODING),
    )