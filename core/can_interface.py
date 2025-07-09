import random

def send_frame(can_id, data):
    print(f"[CAN SEND] ID: {hex(can_id)}, Data: {data}")


def read_frame(can_id):
    # Simulate reading a CAN frame
    return {
        'id': can_id,
        'data': [random.randint(0, 255) for _ in range(8)]
    }