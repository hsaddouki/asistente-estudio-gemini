import torch
import torch.nn as nn
from typing import Tuple, List, Optional

def validate_attention_dims(q_shape: Tuple[int, ...], 
                            k_shape: Tuple[int, ...], 
                            v_shape: Tuple[int, ...]) -> bool:
    """
    Valida las dimensiones para una operación de atención escalada por producto punto.
    Esperado: (batch, n_heads, seq_len, head_dim)
    """
    if len(q_shape) != 4 or len(k_shape) != 4 or len(v_shape) != 4:
        print(f"Error: Se esperaban tensores de 4 dimensiones (B, H, L, D). Recibido: {len(q_shape)}, {len(k_shape)}, {len(v_shape)}")
        return False
        
    b1, h1, l1, d1 = q_shape
    b2, h2, l2, d2 = k_shape
    b3, h3, l3, d3 = v_shape
    
    # Comprobar consistencia de Batch y Heads
    if not (b1 == b2 == b3) or not (h1 == h2 == h3):
        print("Error: Inconsistencia en Batch Size o Número de Cabezales.")
        return False
        
    # Comprobar dimensión de proyección (d_k)
    if d1 != d2:
        print("Error: Dimensiones de Query y Key deben coincidir para el producto punto.")
        return False
        
    # Comprobar longitud de secuencia de Value
    if l2 != l3:
        print("Error: Longitud de secuencia de Key y Value deben coincidir.")
        return False
        
    print("✅ Dimensiones de atención validadas correctamente.")
    return True

def check_conv_output_shape(in_shape: Tuple[int, int, int], 
                           kernel_size: int, 
                           stride: int = 1, 
                           padding: int = 0, 
                           dilation: int = 1) -> Tuple[int, int, int]:
    """
    Calcula la dimensión de salida de una capa convolucional 2D.
    in_shape: (C, H, W)
    """
    c_in, h_in, w_in = in_shape
    
    h_out = ((h_in + 2 * padding - dilation * (kernel_size - 1) - 1) // stride) + 1
    w_out = ((w_in + 2 * padding - dilation * (kernel_size - 1) - 1) // stride) + 1
    
    return (c_in, h_out, w_out)

if __name__ == "__main__":
    # Test simple
    q = (1, 8, 128, 64)
    k = (1, 8, 128, 64)
    v = (1, 8, 128, 64)
    validate_attention_dims(q, k, v)
