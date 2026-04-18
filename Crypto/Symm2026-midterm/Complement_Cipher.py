# 보수특성을 갖는 Feistel 암호

# 4비트 Sbox 
S = [0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7]

# 4비트 F 함수
def F(IN, RK):
    # IN과 RK의 XOR
    X = IN ^ RK    
    # Sbox 대체
    S_out = (S[X]) ^ 0xF    
    return S_out

#입력 8비트 (L, R), 키 4비트 K
def CEnc(plaintext, key, verbose=False):
    nRound = 8
    #RK = [ (key>>(i%4)) &0x0f for i in range(nRound) ] # 라운드 키 생성(8비트 키 용)
    RK = [ (key >> (i % 4)) | (key << (4 - (i % 4))) & 0x0f for i in range(nRound) ] # 라운드 키
    #print("Round Keys:", [f"{bin(rk)[2:].zfill(4)}" for rk in RK])
    L = (plaintext >> 4) & 0x0f
    R = plaintext & 0x0f
    if verbose:
        print(f"Round 0: L={L:01X}, R={R:01X}")
    for i in range(nRound):
        L, R = R, L ^ F(R, RK[i]) # Feistel 구조  
        if verbose:
            print(f"Round {i+1}: L={L:01X}, R={R:01X}")
    
    if verbose:
        print(f"Final: L={L:01X}, R={R:01X}")
    return (L << 4) | R


# 테스트
def CEnc_test():
    plaintext = 0xAB
    key = 0x3C
    ciphertext = CEnc(plaintext, key, True)
    print(f"Plaintext: {plaintext:02X}, Key: {key:02X}, Ciphertext: {ciphertext:02X}")

    c_plaintext = plaintext ^ 0xFF
    c_key = key ^ 0xFF
    c_ciphertext = CEnc(c_plaintext, c_key, True) # 보수 입력과 보수 키  
    print(f"Plaintext: {c_plaintext:02X}, Key: {c_key:02X}, Ciphertext: {c_ciphertext:02X}")

    print(f"Ciphertext XOR: {ciphertext ^ c_ciphertext:02X}") # 암호문 XOR 결과


    binary_string = bin(F(0xA, 0x3))[2:].zfill(4) # F 함수 테스트
    print(binary_string)
    print(F(0x5, 0xC)) # F 함수 테스트


#숫자를 주어진 자리수의 이진문자열로 만들기
def num2bin(num, bits):
    return bin(num)[2:].zfill(bits)

# 보수특성을 이용한 암호키 찾기
def CEnc_key_recovery():
    m1 = 0xAB
    m2 = m1 ^ 0xFF
    key = 0x0C #하위 4비트만 쓰자 (4비트 암호키)
    c1 = CEnc(m1, key)
    c2 = CEnc(m2, key) 
    
    #주어진 평문 암호문쌍
    print("Key =", f"{key:02X} = {num2bin(key, 4)}")
    print("(m1, c1) =", f"({m1:02X}, {c1:02X}) = ({bin(m1)[2:].zfill(8)}, {bin(c1)[2:].zfill(8)})")
    print("(m2, c2) =", f"({m2:02X}, {c2:02X}) = ({bin(m2)[2:].zfill(8)}, {bin(c2)[2:].zfill(8)})")
    print()

    print("key | CEnc(m1, key) | CEnc(m2, key)")
    for k in range(16): # 가능한 암호키로 암호화한 결과를 표로 만든다
        c1_k = CEnc(m1, k)
        c2_k = CEnc(m2, k)
        #print(f"{k:02X} | {c1_k:02X} | {c2_k:02X}")
        print(f"{num2bin(k, 4)} | {num2bin(c1_k, 8)} | {num2bin(c2_k, 8)}")
    print('\n')

# 보수특성을 이용한 암호키 찾는 문제
def CEnc_key_recovery_test():
    m1 = 0xAB
    m2 = m1 ^ 0xFF
    key = 0x0C #하위 4비트만 쓰자 (4비트 암호키)

    m1_list = [0xAB, 0x83, 0x3F, 0x5C, 0xD3]
    m2_list = [m ^ 0xFF for m in m1_list]
    key = [ 0x0C, 0x0F, 0x03, 0x0A, 0x05] #하위 4비트만 쓰자 (4비트 암호키)

    for m1, m2, key in zip(m1_list, m2_list, key):

        c1 = CEnc(m1, key)
        c2 = CEnc(m2, key) 
        
        #주어진 평문 암호문쌍
        print("Key =", f"{key:02X} = {num2bin(key, 4)}")
        print("(m1, c1) =", f"({m1:02X}, {c1:02X}) = ({bin(m1)[2:].zfill(8)}, {bin(c1)[2:].zfill(8)})")
        print("(m2, c2) =", f"({m2:02X}, {c2:02X}) = ({bin(m2)[2:].zfill(8)}, {bin(c2)[2:].zfill(8)})")
        print()

        print("key | CEnc(m1, key) | CEnc(m2, key)")
        for k in range(16): # 가능한 암호키로 암호화한 결과를 표로 만든다
            c1_k = CEnc(m1, k)
            c2_k = CEnc(m2, k)
            #print(f"{k:02X} | {c1_k:02X} | {c2_k:02X}")
            print(f"{num2bin(k, 4)} & {num2bin(c1_k, 8)} & {num2bin(c2_k, 8)}")

        print("\bar c_1 = CEnc(m2, \bar k)", f"{bin(c1^0xFF)[2:].zfill(8)} = CEnc(m2, {num2bin(key^0xF, 4)})" )
        print('\n')

    
if __name__ == "__main__":
    #CEnc_test()

    CEnc_key_recovery()

    CEnc_key_recovery_test()
