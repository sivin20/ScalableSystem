import threading
from client import get_producer, DEFAULT_TOPIC, send_avro_msg
import io
import os
import csv
import avro.schema
from avro.io import DatumWriter
from collections import namedtuple

class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

TAXIDATA = "./data/yellow_tripdata_2016-03.csv"
fields = ("VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count", "trip_distance", "pickup_longitude", "pickup_latitude", "RatecodeID", "store_and_fwd_flag", "dropoff_longitude", "dropoff_latitude", "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount")
taxiRecord = namedtuple('taxiRecord', fields)

def read_taxi_data(path):
    with open(path, 'rU') as data:
        data.readline()
        reader = csv.reader(data, delimiter = ",")
        for row in map(taxiRecord._make, reader):
            yield(row)


def parse_schema(path="avroschema.avsc"):
    with open(path, 'rb') as data:
        return avro.schema.parse(data.read())
    
def serialize_records(records, outpath="taxi.avro"):
    schema = parse_schema()
    writer = DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    for record in records:
        record = dict((f, getattr(record, f)) for f in record._fields)
        writer.write(record, encoder)
        raw_bytes=bytes_writer.getvalue()
        send_avro_msg(raw_bytes, DEFAULT_TOPIC, get_producer())


if __name__ == "__main__":
    serialize_records(read_taxi_data(TAXIDATA))