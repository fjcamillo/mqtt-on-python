import paho.mqtt.publish as publish

publish.single('wiznet/topic', 'Hello', hostname='test.mosquitto.org')
publish.single('wiznet/test', 'World', hostname='test.mosquitto.org')
print('Done')