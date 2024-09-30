Encryption Algorithm:-
Algorithm using DNA data hiding using hybrid approach.
Input: Message (m), key (k), texts file (Tf), original DNA sequence (ODNA).
Output: DNA base with encryption data (EDNA).
Initialization:
1. M2 ← ASCII (m); K2 ← ASCII (k)
2. X2 ← 𝑀2 ⊕ 𝐾2
3. B2 ← K2 + X2
4. BDNA ← B2
5. Data(d) ← Read(Tf)
6. T[] ← d10
7. ODNA ← Read(Dn)
8. For i, s in T & Dn
     ODNA[s] = T[i]
     T[i] = BDNA[j]
     ODNA[s] = BDNA[j]
   Do
9. EDNA

---------------------------------------------------------------------------------------------

Decryption Algorithm:- 
Algorithm for finding data from the encrypted DNA sequence.
Input: Text file (Tf), encrypted DNA sequence (EDNA).
Output: Original message (m), original key (k).
Initialization:
1. Data(d) ← Read(Tf)
2. T[] ← d10
3. EDNA ← Read(EDNA)
4. For i, s in EDNA & T
    EDNA[s] = T[i]
    BDNA[] = T[i]
Do
5. KDNA == [j][1-4], XDNA == [j][5-8]
6. K2 ← KDNA, X2 ← XDNA
7. M2 ← 𝑋2 ⊕ 𝐾2
8. m ← ASCII (M2); k ← ASCII (K2)
--------------------------------------------------------------------------------------------
