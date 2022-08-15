import time

from .message import MessageType


# of course this code looks dumb, but imagine some real implementations of each method here
class HueLightDevice:
    def connect(self) -> None:
        print("Connecting Hue Light.")
        time.sleep(0.5)
        print("Hue Light connected.")

    def disconnect(self) -> None:
        print("Disconnecting Hue Light.")
        time.sleep(0.5)
        print("Hue Light disconnected.")

    def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Hue Light handling message of type {message_type.name} with data [{data}]."
        )
        time.sleep(0.5)
        print("Hue Light received message.")


class SmartSpeakerDevice:
    def connect(self) -> None:
        print("Connecting to Smart Speaker.")
        time.sleep(0.5)
        print("Smart Speaker connected.")

    def disconnect(self) -> None:
        print("Disconnecting Smart Speaker.")
        time.sleep(0.5)
        print("Smart Speaker disconnected.")

    def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Smart Speaker handling message of type {message_type.name} with data [{data}]."
        )
        time.sleep(0.5)
        print("Smart Speaker received message.")


class SmartToiletDevice:
    def connect(self) -> None:
        print("Connecting to Smart Toilet.")
        time.sleep(0.5)
        print("Smart Toilet connected.")

    def disconnect(self) -> None:
        print("Disconnecting Smart Toilet.")
        time.sleep(0.5)
        print("Smart Toilet disconnected.")

    def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Smart Toilet handling message of type {message_type.name} with data [{data}]."
        )
        time.sleep(0.5)
        print("Smart Toilet received message.")
