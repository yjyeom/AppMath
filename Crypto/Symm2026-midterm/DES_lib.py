#initail permutation
ip_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
# PC1 permutation table
pc1_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]
# Define the left shift schedule for each round
shift_schedule = [1, 1, 2, 2,
                  2, 2, 2, 2,
                  1, 2, 2, 2,
                  2, 2, 2, 1]

# PC2 permutation table
pc2_table = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]
#expension
e_box_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# S-box tables for DES
s_boxes = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
p_box_table = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]
ip_inverse_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# ASCII문자열을 64비트 이진수로 변환하는 함수
def str_to_bin(user_input):
    
        # Convert the string to binary
        binary_representation = ''
        
        for char in user_input:
            # Get ASCII value of the character and convert it to binary
            binary_char = format(ord(char), '08b')
            binary_representation += binary_char
            binary_representation = binary_representation[:64]
        
        # Pad or truncate the binary representation to 64 bits
        binary_representation = binary_representation[:64].ljust(64, '0')
        
        # Print the binary representation
        # print("Binary representation of input string: ", binary_representation)
        # print(len(binary_representation), 'bits of input string')
        
        return binary_representation

def binary_to_ascii(binary_str):
    ascii_str = ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])
    return ascii_str

def ip_on_binary_rep(binary_representation):
    
    ip_result = [None] * 64
    
    for i in range(64):
        ip_result[i] = binary_representation[ip_table[i] - 1]

    # Convert the result back to a string for better visualization
    ip_result_str = ''.join(ip_result)
    
    return ip_result_str

def key_in_binary_conv():
    # Original key (can be changed but it should be 8 char)
    original_key = 'abcdefgh'
    binary_representation_key = ''
    
    for char in original_key:
    # Convert the characters to binary and concatenate to form a 64-bit binary string
        binary_key = format(ord(char), '08b') 
        binary_representation_key += binary_key

    
    return binary_representation_key

def generate_round_keys():
    
    # Key into binary
    binary_representation_key = key_in_binary_conv()
    pc1_key_str = ''.join(binary_representation_key[bit - 1] for bit in pc1_table)

    
    # Split the 56-bit key into two 28-bit halves
    c0 = pc1_key_str[:28]
    d0 = pc1_key_str[28:]
    round_keys = []
    for round_num in range(16):
        # Perform left circular shift on C and D
        c0 = c0[shift_schedule[round_num]:] + c0[:shift_schedule[round_num]]
        d0 = d0[shift_schedule[round_num]:] + d0[:shift_schedule[round_num]]
        # Concatenate C and D
        cd_concatenated = c0 + d0

        # Apply the PC2 permutation
        round_key = ''.join(cd_concatenated[bit - 1] for bit in pc2_table)

        # Store the round key
        round_keys.append(round_key)
    return round_keys

def encryption(user_input):
    binary_rep_of_input = str_to_bin(user_input)

    print("Binary representation of input string: ", binary_rep_of_input)
    # Initialize lists to store round keys
    round_keys = generate_round_keys()
    print("Round keys generated for each round:")
    for i, key in enumerate(round_keys):
        print(f"Round {i + 1}: {key}")

    ip_result_str = ip_on_binary_rep(binary_rep_of_input)
    print("Binary representation of input: ", ip_result_str)

    # the initial permutation result is devided into 2 halfs
    lpt = ip_result_str[:32]
    rpt = ip_result_str[32:]

    print("Left half (LPT): ", lpt)
    print("Right half (RPT): ", rpt)

    # Assume 'rpt' is the 32-bit right half, 'lpt' is the 32-bit left half, and 'round_keys' is a list of 16 round keys

    for round_num in range(16):
        # Perform expansion (32 bits to 48 bits)
        expanded_result = [rpt[i - 1] for i in e_box_table]

        # Convert the result back to a string for better visualization
        expanded_result_str = ''.join(expanded_result)

        # Round key for the current round
        round_key_str = round_keys[round_num]


        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))


        # Split the 48-bit string into 8 groups of 6 bits each
        six_bit_groups = [xor_result_str[i:i+6] for i in range(0, 48, 6)]

        # Initialize the substituted bits string
        s_box_substituted = ''

        # Apply S-box substitution for each 6-bit group
        for i in range(8):
            # Extract the row and column bits
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)

            # Lookup the S-box value
            s_box_value = s_boxes[i][row_bits][col_bits]
            
            # Convert the S-box value to a 4-bit binary string and append to the result
            s_box_substituted += format(s_box_value, '04b')

        # Apply a P permutation to the result
        p_box_result = [s_box_substituted[i - 1] for i in p_box_table]

        # # Convert the result back to a string for better visualization
        # p_box_result_str = ''.join(p_box_result)


        # Convert LPT to a list of bits for the XOR operation
        lpt_list = list(lpt)

        # Perform XOR operation
        new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]

        # Convert the result back to a string for better visualization
        new_rpt_str = ''.join(new_rpt)

        # Update LPT and RPT for the next round
        lpt = rpt
        rpt = new_rpt_str

        # Print or use the RPT for each round

    print('\n')
    # At this point, 'lpt' and 'rpt' contain the final left and right halves after 16 rounds

    # After the final round, reverse the last swap
    final_result = rpt + lpt

    # Perform the final permutation (IP-1)
    final_cipher = [final_result[ip_inverse_table[i] - 1] for i in range(64)]

    # Convert the result back to a string for better visualization
    final_cipher_str = ''.join(final_cipher)

    # Print or use the final cipher(binary)
    # print("Final Cipher binary:", final_cipher_str, len(final_cipher_str))


    # Convert binary cipher to ascii
    final_cipher_ascii = binary_to_ascii(final_cipher_str)
    print("Final Cipher text:", final_cipher_ascii , len(final_cipher_ascii))
    
    return final_cipher_ascii

# decryption of cipher to origional

def decryption(final_cipher):
    
    
    # Initialize lists to store round keys
    round_keys = generate_round_keys()
    
    # Apply Initial Permutation
    ip_dec_result_str = ip_on_binary_rep(final_cipher)
    
    lpt = ip_dec_result_str[:32]
    rpt = ip_dec_result_str[32:]

    for round_num in range(16):
        # Perform expansion (32 bits to 48 bits)
        expanded_result = [rpt[i - 1] for i in e_box_table]
    
        # Convert the result back to a string for better visualization
        expanded_result_str = ''.join(expanded_result)
        # print(expanded_result_str)
        # Round key for the current round
        round_key_str = round_keys[15-round_num]
    
        # XOR between key and expanded result 
        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))
    
    
        # Split the 48-bit string into 8 groups of 6 bits each
        six_bit_groups = [xor_result_str[i:i+6] for i in range(0, 48, 6)]
    
        # Initialize the substituted bits string
        s_box_substituted = ''
    
        # Apply S-box substitution for each 6-bit group
        for i in range(8):
            # Extract the row and column bits
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)
    
            # Lookup the S-box value
            s_box_value = s_boxes[i][row_bits][col_bits]
            
            # Convert the S-box value to a 4-bit binary string and append to the result
            s_box_substituted += format(s_box_value, '04b')
    
        # Apply a P permutation to the result
        p_box_result = [s_box_substituted[i - 1] for i in p_box_table]
    
        # Convert the result back to a string for better visualization
        # p_box_result_str = ''.join(p_box_result)
    
        # Convert LPT to a list of bits for the XOR operation
        lpt_list = list(lpt)
    
        # Perform XOR operation
        new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]
    
        # Convert the result back to a string for better visualization
        new_rpt_str = ''.join(new_rpt)
    
        # Update LPT and RPT for the next round
        lpt = rpt
        rpt = new_rpt_str
    
        # Print or use the RPT for each round
    
    print('\n')
    final_result = rpt + lpt
    # Perform the final permutation (IP-1)
    final_cipher = [final_result[ip_inverse_table[i] - 1] for i in range(64)]

    # Convert the result back to a string for better visualization
    final_cipher_str = ''.join(final_cipher)

    # Print or use the final cipher

    # binary cipher string to ascii
    final_cipher_ascii = binary_to_ascii(final_cipher_str)
    print("Decryption of Cipher :", final_cipher_ascii)

    return final_cipher_ascii

# Start test run (original ver) ===========================

# 입력한 ASCII 문자열을 암호화하고 다시 복호화하는 전체 과정 테스트
def Original_run():
    # user input (ascii string) --> binary conversion --> initial permutation --> 16 rounds of DES --> final permutation --> cipher text (ascii)
    user_input = input("Enter a string: ")


    # Encryption
    enc = encryption(user_input)


    # Decyption

    # First we'll convert Final Cipher text into binary 
    enc_to_binary = str_to_bin(enc)

    # we'll call the decryption function 
    dec = decryption(enc_to_binary)


# 여기까지는 DES library 파일
#=================================    

#=================================    
# 여기부터 salt 작성 내용

#--[데이터 변환용]-----------------
# (64비트) 16진수(문자열)을 64비트 이진수(문자열)로 변환하는 함수 
def hex_to_binary(hex_string, bits=64):
    #print('hex => ', hex_string)
    #print('int => ', int(hex_string, 16))
    binary_string = bin(int(hex_string, 16))[2:]  # Convert hex to binary and remove '0b' prefix
    return binary_string.zfill(bits)  # Pad with leading zeros to ensure it's the specified number of bits long

# 64비트 이진수(문자열)를 64비트 16진수(문자열)로 변환하는 함수
def binary_to_hex(binary_string, bits=64):
    hex_string = hex(int(binary_string, 2))[2:]  # Convert binary to hex and remove '0x' prefix
    hex_string = hex_string.upper()  # Convert to uppercase for standard hex representation
    return hex_string.zfill(bits // 4)  # Pad with leading zeros to ensure it's the specified number of characters long

# 문자열의 s간격마다 공백을 추가하는 함수
def add_spaces(input_string, s):
    return ' '.join(input_string[i:i+s] for i in range(0, len(input_string), s))

# 16진수 문자열 두개의 XOR 연산을 수행하는 함수
def hex_xor(hex1, hex2, bits=32):
    # Convert hex strings to integers, perform XOR, and convert back to hex
    xor_result = int(hex1, 16) ^ int(hex2, 16)
    return hex(xor_result)[2:].zfill(bits // 4)  # Remove '0x' prefix and pad with zeros
#---------------------------------


# DES 라운드 함수 동작 (중간과정 출력)
def round_function_step_by_step(hex_in, hex_rk):

    # 입력과 라운드키를 16진수와 이진수로 출력
    binary_in = hex_to_binary(hex_in, 32)
    binary_rk = hex_to_binary(hex_rk, 48)
    print("Input(hex, binary): ", hex_in, add_spaces(binary_in,8))
    print("Round Key(hex, binary): ", hex_rk, add_spaces(binary_rk,8))

    # Perform expansion (32 bits to 48 bits)
    expanded_result = [binary_in[i - 1] for i in e_box_table]
    expanded_result_str = ''.join(expanded_result)
    print("(A) After E: ", binary_to_hex(expanded_result_str, 48), add_spaces(expanded_result_str, 8))
    # XOR between key and expanded result 
    xor_result_str = ''
    for i in range(48):
        xor_result_str += str(int(expanded_result_str[i]) ^ int(binary_rk[i]))

    print("After RK-XOR: ", binary_to_hex(xor_result_str, 48), add_spaces(xor_result_str, 8))
    print("(B) Sbox IN: ", add_spaces(xor_result_str, 6))

    # Split the 48-bit string into 8 groups of 6 bits each
    six_bit_groups = [xor_result_str[i:i+6] for i in range(0, 48, 6)]

    # Initialize the substituted bits string
    s_box_substituted = ''

    # Apply S-box substitution for each 6-bit group
    for i in range(8):
        row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
        col_bits = int(six_bit_groups[i][1:-1], 2)
        s_box_value = s_boxes[i][row_bits][col_bits]
        s_box_substituted += format(s_box_value, '04b')

    print("(C) Sbox OUT : ", binary_to_hex(s_box_substituted, 32), add_spaces(s_box_substituted, 4))
    
    # Apply a P permutation to the result
    p_box_result = [s_box_substituted[i - 1] for i in p_box_table]
    
    print("(OUTPUT) After P: ", binary_to_hex(''.join(p_box_result), 32), add_spaces(''.join(p_box_result), 8))

    return p_box_result

# 단일 라운드함수의 세부동작을 확인하는 테스트 코드
def test_round_function():
    hex_in = "1EFC7384"
    hex_rk = "7289D2A58257"
    correct_out = "B4D764C9"
    binary_in = hex_to_binary(hex_in, 32)
    binary_rk = hex_to_binary(hex_rk, 48)
    print("== Test Round Function (start) ==")
    #print("Input(hex, binary): ", hex_in, add_spaces(binary_in,8))
    #print("Round Key(hex, binary): ", hex_rk, add_spaces(binary_rk,8))

    round_out = round_function_step_by_step(hex_in, hex_rk)

    print("Round Function Output: ", add_spaces(''.join(round_out), 8))
    print("Round Function Output (hex): ", binary_to_hex(''.join(round_out), 32))
    print("Correct Output (hex): ", correct_out)
    if binary_to_hex(''.join(round_out), 32) == correct_out:
        print("Round function output: TEST PASSED!!!")
    print("== Test Round Function (end) ==\n\n")

# 라운드함수의 차분특성과 세부동작을 확인하는 테스트 코드
def round_ftn_difference():
    # 0번째는 테스트 벡터로 출제에는 사용하지 않음
    hex_in_list = ["1EFC7384", "FC73841E", "73841EFC", "841EFC73", "8473FC1E" ] 
    hex_rk_list = ["7289D2A58257", "577289D2A582", "82577289D2A5", "A582577289D2", "D2A582577289"]
    for i in range(len(hex_in_list)):
        print(f"== Test Case {i} ==")
        
        #-- Y1 = F(X1, RK) 계산 --
        X1 = hex_in_list[i]
        RK = hex_rk_list[i]      
        
        round_out = round_function_step_by_step(X1, RK)

        Y1 = binary_to_hex(''.join(round_out), 32)        
        print(f"Round Function Output {i} (hex): ", Y1)
        print()

        #-- Y2 = F(X2, RK) = F(X1^Delta, RK) 계산 --
        Delta = "04000000"  # 입력의 차분
        X2 = hex_xor(X1, Delta).upper()  # X1과 Delta의 XOR 결과

        round_out = round_function_step_by_step(X2, RK)

        Y2 = binary_to_hex(''.join(round_out), 32)
        print(f"Round Function Output {i} (hex): ", Y2)
        print()

        print(f"({X1}, {RK}) --[F]--> {Y1}")
        print(f"({X2}, {RK}) --[F]--> {Y2}")

        CL = X2
        CR = Y2
        XL = hex_xor(Y2, CR).upper()
        XR = CL

        print(f"(CL, CR) = ({CL}, {CR}) --> (XL, XR) = ({XL}, {XR})")


        print('\n')


if __name__ == "__main__":
    #Original_run()

    '''
    # Test run with hex input
    hex_input = input("Enter a hexadecimal string (16 characters for 64 bits): ")
    binary_input = hex_to_binary(hex_input)
    print("Binary representation of input string: ", binary_input)
    hex_recovered = binary_to_hex(binary_input)
    print("Recovered hexadecimal string: ", hex_recovered)
    '''

    #라운드 함수의 동작을 테스트벡터로 확인
    test_round_function()

    # 문제 유형을 만든다
    round_ftn_difference()


