import os
import argparse
import time


def uuidv4():
    raw_bytes = bytearray(os.urandom(16))

    raw_bytes[6] = (raw_bytes[6] & 0x0F) | 0x40  # Set version to 4
    raw_bytes[8] = (raw_bytes[8] & 0x3F) | 0x80  # Set variant to 0b10

    h = raw_bytes.hex()
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def uuidv7():
    timestamp_ms = int(time.time_ns() / 1_000_000)  # Convert to milliseconds
    random_bytes = bytearray(os.urandom(10))

    raw_bytes = bytearray(timestamp_ms.to_bytes(6, "big"))
    raw_bytes.extend(random_bytes)

    raw_bytes[6] = (raw_bytes[6] & 0x0F) | 0x70  # Set version to 7
    raw_bytes[8] = (raw_bytes[8] & 0x3F) | 0x80  # Set variant to 0b10

    h = raw_bytes.hex()
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", type=int, choices=[4, 7], default=4)
    args = parser.parse_args()

    if args.version == 4:
        print(uuidv4())
    elif args.version == 7:
        print(uuidv7())
    else:
        print(f"Unsupported version: {args.version}")
        return


if __name__ == "__main__":
    main()
