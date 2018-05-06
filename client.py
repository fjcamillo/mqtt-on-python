import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print('Connected with result code', str(rc))

    client.subscribe('wiznet/topic')
    client.subscribe('wiznet/test')

def on_message(client, userdata, msgs):
    print(msgs.topic +' '+ str(msgs.payload))

    if str(msgs.payload, 'utf8') == 'Hello':
        print('Received message #1. Do Something')

    if str(msgs.payload, 'utf8') == 'World':
        print('Received message #2: Do Something Else')



client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('test.mosquitto.org', 1883, 60)
client.loop_forever()
