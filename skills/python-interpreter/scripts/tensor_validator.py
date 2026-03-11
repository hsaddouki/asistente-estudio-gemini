import torch
import torch.nn as nn
import sys

def check_conv2d_shape(input_shape, out_channels, kernel_size, stride=1, padding=0, dilation=1):
    """
    Simula una capa Conv2D para validar el output shape.
    input_shape: (Batch, Channels, Height, Width)
    """
    try:
        dummy_input = torch.randn(input_shape)
        conv = nn.Conv2d(
            in_channels=input_shape[1],
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            dilation=dilation
        )
        output = conv(dummy_input)
        return f"✅ Success: Input {list(input_shape)} -> Output {list(output.shape)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    # Ejemplo de uso desde CLI: python tensor_validator.py conv2d 1,3,224,224 64 3 1 1
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == "conv2d":
            input_shape = tuple(map(int, sys.argv[2].split(',')))
            out_channels = int(sys.argv[3])
            kernel_size = int(sys.argv[4])
            stride = int(sys.argv[5]) if len(sys.argv) > 5 else 1
            padding = int(sys.argv[6]) if len(sys.argv) > 6 else 0
            print(check_conv2d_shape(input_shape, out_channels, kernel_size, stride, padding))
