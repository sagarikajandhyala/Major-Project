# embed.py
# Prediction Error Expansion (PEE) embedding

import numpy as np
from predictor import predict_pixel

def embed_payload(image, bitstream):
    """
    Embed a binary payload into the image using Prediction Error Expansion.
    Returns the stego image and number of bits embedded.
    """
    stego = image.copy()
    bit_index = 0
    h, w = image.shape

    # Skip border pixels to avoid index issues
    for i in range(1, h):
        for j in range(1, w):

            if bit_index >= len(bitstream):
                return stego, bit_index

            pred = predict_pixel(image, i, j)
            error = image[i, j] - pred
            bit = bitstream[bit_index]

            # PEE embedding rule
            new_error = 2 * error + bit
            stego_pixel = pred + new_error

            # Safety check (avoid overflow)
            if 0 <= stego_pixel <= 255:
                stego[i, j] = stego_pixel
                bit_index += 1
            else:
                stego[i, j] = image[i, j]

    return stego, bit_index
