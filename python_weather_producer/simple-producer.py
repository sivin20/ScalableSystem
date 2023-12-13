import threading
from client import get_producer, DEFAULT_TOPIC, send_avro_msg
import io
import os
import csv
import avro.schema
from avro.io import DatumWriter, DatumReader, BinaryDecoder, BinaryEncoder
from avro.datafile import DataFileReader, DataFileWriter
from collections import namedtuple

class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

WEATHERDATA = "./data/Weather.csv"
fields = ("pickup_datetime", "tempm", "tempi", "dewptm", "dewpti", "hum", "wspdm", "wspdi", "wgustm", "wgusti", "wdird", "wdire", "vism", "visi", "pressurem", "pressurei", "windchillm", "windchilli", "heatindexm", "heatindexi", "precipm", "precipi", "conds", "icon", "fog", "rain", "snow", "hail", "thunder", "tornado")
weatherRecord = namedtuple('weatherRecord', fields)

def read_weather_data(path):
    with open(path, 'rU') as data:
        data.readline()
        reader = csv.reader(data, delimiter = ",")
        for row in map(weatherRecord._make, reader):
            yield(row)


def parse_schema(path="weatherSchema.avsc"):
    with open(path, 'rb') as data:
        return avro.schema.parse(data.read())
    
def serialize_records(records):
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
    serialize_records(read_weather_data(WEATHERDATA))