from collections import namedtuple

SensorData = namedtuple("SensorData",["sensor_id", "temperature", "humidity", "pressure"])
sensors = (
    SensorData(1, 22.5, 45.2, 1013.1),
    SensorData(2, 24.0, 50.1, 1012.8),
    SensorData(3, 21.8, 48.5, 1013.5),
    SensorData(4, 23.2, 46.7, 1012.9),
    SensorData(5, 25.1, 49.3, 1013.0)
)

for x in sensors:
    if x.temperature > 25:
        print(f"sensor id: {x.sensor_id}, temperature: {x.temperature}")