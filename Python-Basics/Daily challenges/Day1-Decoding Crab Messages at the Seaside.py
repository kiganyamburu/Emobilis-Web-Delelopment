def decode_crab_messages(binary_messages):
    """
    Decode binary messages from crabs into decimal numbers.

    Args:
        binary_messages (list of str): List of binary strings containing only '0's and '1's

    Returns:
        list: List of integers representing decoded decimal values
    """
    decoded_messages = []

    for message in binary_messages:
        # Convert binary string to decimal integer using int(str, 2)
        decimal_value = int(message, 2)
        decoded_messages.append(decimal_value)

    return decoded_messages

# Example usage:
# messages = ["1010", "1111", "0101"]
# result = decode_crab_messages(messages)
# print(result)  # [10, 15, 5]