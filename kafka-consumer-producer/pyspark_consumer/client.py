from kafka import KafkaProducer, KafkaConsumer
import json
from data_model import generate_sample, PackageObj

KAFKA_BROKERS: str = (
    "localhost:9092"  # <service name>.<namepsace>:<port>
)

DEFAULT_TOPIC: str = "INGESTION"
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

def send_msg(value, key: str, topic: str, producer: KafkaProducer) -> None:
    producer.send(
        topic=topic,
        key=key.encode(DEFAULT_ENCODING),
        value=json.dumps(value).encode(DEFAULT_ENCODING),
    )


def produce_msg(sensor_id: int, topic: str, producer: KafkaProducer) -> None:
    key, value = generate_sample(sensor_id=sensor_id)
    print(value)
    send_msg(key=str(key), value=value, topic=topic, producer=producer)


def recive_msg(consumer: KafkaConsumer) -> None:
    print('msg')
    for msg in consumer:
        print(msg)