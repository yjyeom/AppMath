# 선형 암호함수와 Affine 암호함수


# nibble을 0과 1의 비트 배열로 변환하는 함수
# B = [b3 b2 b1 b0] --> [b3, b2, b1, b0]
def nibble2bits(byte):
    return [(byte >> i) & 1 for i in range(3, -1, -1)]

# 0과 1의 비트 배열을 nibble로 변환하는 함수
# [b3, b2, b1, b0] --> B = [b3 b2 b1 b0]
def bits2nibble(bits):
    byte = 0
    for i in range(4):
        byte |= (bits[i] << (3   - i))
    return byte

# 4x4 이진 행렬과 4비트 벡터의 곱셈
def Ax(A, x):
    result = 0
    for i in range(4):
        bit_sum = 0
        for j in range(4):
            bit_sum ^= (A[i][j] & x[j]) # XOR 연산
        result |= (bit_sum << (3 - i)) # 결과를 다시 nibble로 조합
    return result


R0, R1, R2, R3 = [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0] 

A0 = [R0, R1, R2, R3]
A1 = [R1, R2, R3, R0]
A2 = [R2, R3, R0, R1]
A3 = [R3, R0, R1, R2]

A = [A0, A1, A2, A3]   

#선형 암호함수 EL
def EL(idx, pt):
    x = nibble2bits(pt)
    return Ax(A[idx], x)

#숫자를 주어진 자리수의 이진문자열로 만들기
def num2bin(num, bits):
    return bin(num)[2:].zfill(bits)

# 선형 암호함수 테스트
def EL_test():
    plaintext = 0xA # 1010
    ciphertext = EL(0, plaintext)
    print(f"Plaintext: {plaintext:01X} = {num2bin(plaintext, 4)}, Ciphertext: {ciphertext:01X} = {num2bin(ciphertext, 4)}")

# 선형 암호 문제 만들기
def EL_linear_test():
 
     for idx in range(4): 
        print(f"== Test Case {idx+1} ==")
        print("Matrix A =", A[idx])
        print("Plaintext | Ciphertext")
        for pt in range(16):
            ct = EL(idx, pt)
            print(f"{num2bin(pt, 4)} | {num2bin(ct, 4)}")

        print('\n')

#===================================
# Affine 암호함수 EA
Affine_b = [ 0x3, 0x6, 0x5, 0x9 ] # Affine 암호함수의 상수 벡터 b
def EA(idx, pt):
    x = nibble2bits(pt)
    w = Ax(A[idx], x) # 선형 변환
    return w ^ Affine_b[idx] # 선형 변환 결과에 상수 벡터 b를 XOR

# Affine 암호함수 테스트
def EA_test():
    plaintext = 0xA # 1010
    ciphertext = EA(0, plaintext)
    print("Affine A =", A[0])
    print("Affine b =", num2bin(Affine_b[0], 4))
    print(f"Plaintext: {plaintext:01X} = {num2bin(plaintext, 4)}, Ciphertext: {ciphertext:01X} = {num2bin(ciphertext, 4)}")

# Affine 암호 문제 만들기
def EA_affine_test():
 
     for idx in range(4): 
        print(f"== Test Case {idx+1} ==")
        print("Matrix A =", A[idx])
        print("Affine b =", num2bin(Affine_b[idx], 4))
        print("Plaintext | Ciphertext")
        for pt in range(16):
            ct = EA(idx, pt)
            print(f"{num2bin(pt, 4)} | {num2bin(ct, 4)}")

        print('\n')


if __name__ == "__main__":
    #EL_test()
    #EL_linear_test()
    #EA_test()
    EA_affine_test()
