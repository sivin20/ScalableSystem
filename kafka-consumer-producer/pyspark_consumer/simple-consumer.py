from client import get_consumer, DEFAULT_TOPIC, DEFAULT_CONSUMER
import avro.schema
from kafka import KafkaConsumer
import io
from datetime import datetime
from avro.io import DatumWriter, DatumReader, BinaryDecoder, BinaryEncoder
import sys

SCHEMA = ''


def main():
    args = sys.argv[1:]
    group_id = args[0] if len(args) == 1 else DEFAULT_CONSUMER

    print(f"group_id={group_id}")
    print(group_id)
    consumer = get_consumer(DEFAULT_TOPIC, group_id=group_id)
    print("consumer:" + str(consumer))
    try:
        recive_msg(consumer)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

def recive_msg(consumer: KafkaConsumer) -> None:
    print('msg')
    for msg in consumer:
        print(datetime.now())
        print('------------MSG1------------ \n' + str(deserialize_record(msg.value)))

def parse_schema(path="weatherSchema.avsc"):
    with open(path, 'rb') as data:
        return avro.schema.parse(data.read())

def deserialize_record(bytes):
    print('----TRYING TO DESERIALIZE-----\n ')
    bytes_reader = io.BytesIO(bytes)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(SCHEMA)
    return reader.read(decoder)

if __name__ == "__main__":
    SCHEMA = parse_schema("avroschema.avsc")
    main()