
print ('!!! The encryption process !!!')

'''>>>> MESSAGE--->>>ASCII BINARY VALUE <<<<'''
m_word = input("Enter the message: ")                 # Input the message 
for char in m_word:
    ascii = ord(char)
    msg_binary = (str(bin(ascii)[2:]))           # message(ASCII) to binary conversion  
    # print (">>>Message binary: ", msg_binary)
'''>>>> KEY--->>>ASCII BINARY VALUE <<<<'''
k_word = input("Enter the key: ")                    # Input the key
for char in k_word:
    key = ord(char)
    key_binary = (str(bin(key)[2:]))              # key(ASCII) to binary conversion  
    # print (">>>Key binary: " , key_binary) 


'''>>>> XOR OPERATION (MESSAGE & KEY) <<<<'''
# Python3 implementation of the approach
# Function to insert n 0s in the
# beginning of the given string
def addZeros(strr, n):                     # zero padding function 
    for i in range(n):
        strr = "0" + strr
    return strr
# Function to return the XOR
# of the given strings
def getXOR(a, b):                                 # xor function
    # Lengths of the given strings
    aLen = len(msg_binary)
    bLen = len(key_binary)
    # Make both the strings of equal lengths
    # by inserting 0s in the beginning
    if (aLen > bLen):                             # equal the both strings length
        b = addZeros(key_binary, aLen - bLen)
    elif (bLen > aLen):
        a = addZeros(msg_binary, bLen - aLen)
    # Updated length
    lenn = max(aLen, bLen)
    # To store the resultant XOR
    res = ""
    for i in range(lenn):
        if (a[i] == b[i]):
            res += "0"
        else:
            res += "1"
    return res
# Driver code
xor1 = (getXOR(msg_binary,key_binary))            # xor operation
xor = (xor1.zfill(8))                             # zero pad with xor value 
# print (">>>The XOR value is: ", xor)    


'''>>>> SUBSTITUTING BINARY ----->>> DNA BASE(ATGC) <<<<'''
def slice(s):                # slice function 
    ans = " " 
   # s1, s2, s3, s4
    s1 = (s[ :2])
    s2 = (s[2:4:1])
    s3 = (s[4:6:1])
    s4 = (s[6:8:1])
    return(s1, s2, s3, s4)
#DNA bases marked as binary values 
def numbase(B):              # Base numbering function 
   ans = ""
   #  "A"='00', "C"='01', "G"='10', "T"='11'
   if(B == '00'):
     ans = "A"
   elif(B == '01'):
     ans = "C"
   elif(B == '10'):
     ans = "G"
   elif(B == '11'):
     ans = "T"
   return ans
# for XOR binary
message_base1 = slice (xor)                   # slice the XOR binary code
# print ("Sliced xor is ", message_base1)       # The xor code
dna_msg = [] 
for i in message_base1:                       
  message_base1 = numbase (i)                  # base numbering for the XOR binary code
  dna_msg.append(message_base1)
#   print (dna_msg)                                # list of xor substituted in dna bases
# for key_binary
key_binary1 = (key_binary.zfill(8))               # slice the key binary code
key_base1 = slice (key_binary1)
# print ("Sliced key value is ",key_base1)
dna_key = [] 
for i in key_base1:
  key_base1 = numbase (i)                          # base numbering for the key binary code
  dna_key.append (key_base1)
#   print (dna_key)                                  # list of key values substituted in dna bases
y_estr = dna_key + dna_msg
E_DNA = ''.join (str(x) for x in y_estr)              # encrypted DNA string 
# print ('>>>Encrypted DNA bases: ', E_DNA)


'''>>>> FROM TEXT WORDS ---->>> ASCII DECIMAL <<<<'''
def toDecimal(a):                    # ASCII to Decimal conversion 
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(i))
  return m
# open file texts
f = open ("lines.txt", "r")        # call the ,txt file
data = f.read ()                     # read the file
# print (data)
P1 = toDecimal(data)                  # Converted ASCII to Decimal
P = P1[ :8]
# print ('>>>Decimal Index values:', P)        
f.close ()


'''>>>> HIDING THE MESSAGE IN DNA BASE <<<<'''

# NOTE: string indexing is taken as 0 [default]
# Assumption:
  # |X|>|Y|
  # |Y|=|P|
# X: Given String
# Y: Given Encrypted string
# P: Position Index to insert Y at X
def rep(X,Y,P)->str:
  prev = 0
  # since python string is immutable
  Xnew = list(X)

  for i in range(0, len(P)):
    Xnew[P[i]+prev] = Y[i]
    prev += P[i]
  ans = ''.join([str(x) for x in Xnew])
  return ans

def result_test():
  X_test = '''GTTAATGTAGCTTAATAACAAAGCAAAGCACTGAAAATGCTTAGATGGATAATTGT\n
  ATCCCATAAACACAAAGGTTTGGTCCTGGCCTTATAATTAATTAGAGGTAAAATTACACATGCAAACCT\n
  CCATAGACCGGTGTAAAATCCCTTAAACATTTACTTAAAATTTAAGGAGAGGGTATCAAGCACATTAAAA\n
  TAGCTTAAGACACCTTGCCTAGCCACACCCCCACGGGACTCAGCAGTGATAAATATTAAGCAATAAACGAA\n
  AGTTTGACTAAGTTATACCTCTTAGGGTTGGTAAATTTCGTGCCAGCCACCGCGGTCATACGATTAACCCAA\n
  ACTAATTATCTTCGGCGTAAAACGTGTCAACTATAAATAAATAAATAGAATTAAAATCCAACTTATATGTGAA\n
  AATTCATTGTTAGGACCTAAACTCAATAACGAAAGTAATTCTAGTCATTTATAATACACGACAGCTAAGACCCA\n
  AACTGGGATTAGATACCCCACTATGCTTAGCCATAAACCTAAATAATTAAATTTAACAAAACTATTTGCCAGAGA\n
  ACTACTAGCCATAGCTTAAAACTCAAAGGACTTGGCGGTACTTTATATCCATCTAGAGGAGCCTGTTCTATAATCG\n
  ATAAACCCCGCTCTACCTCACCATCTCTTGCTAATTCAGCCTATATACCGCCATCTTCAGCAAACCCTAAAAAGGTA\n
  TTAAAGTAAGCAAAAGAATCAAACATAAAAACGTTAGGTCAAGGTGTAGCCAATGAAATGGGAAGAAATGGGCTACAT\n
  TTTCTTATAAAAGAACATTACTATACCCTTTATGAAACTAAAGGACTAAGGAGGATTTAGTAGTAAATTAAGAATAGAG\n
  AGCTTAATTGAATTGAGCAATGAAGTACGCACACACCGCCCGTCACCCTCCTCAAATTAAATTAAACTTAACATAATTAA\n
  TTTCTAGACATCCGTTTATGAGAGGAGATAAGTCGTAACAAGGTAAGCATACTGGAAAGTGTGCTTGGAATAATCATAGTG\n
  TAGCTTAATATTAAAGCATCTGGCCTACACCCAGAAGATTTCATGACCAATGAACACTCTGAACTAATCCTAGCCCTAGCCC\n
  TACACAAATATAATTATACTATTATATAAATCAAAACATTTATCCTACTAAAAGTATTGGAGAAAGAAATTCGTACATCTAGG\n
  AGCTATAGAACTAGTACCGCAAGGGAAAGATGAAAGACTAATTAAAAGTAAGAACAAGCAAAGATTAAACCTTGTACCTTTTGC\n
  ATAATGAACTAACTAGAAAACTTCTAACTAAAAGAATTACAGCTAGAAACCCCGAAACCAAACGAGCTACCTAAAAACAATTTTA\n
  TGAATCAACTCGTCTATGTGGCAAAATAGTGAGAAGATTTTTAGGTAGAGGTGAAAAGCCTAACGAGCTTGGTGATAGCTGGTTAC\n
  CCAAAAAATGAATTTAAGTTCAATTTTAAACTTGCTAAAAAAACAACAAAATCAAAAAGTAAGTTTAGATTATAGCCAAAAGAGGGA\n
  CAGCTCTTCTGGAACGGAAAAAACCTTTAATAGTGAATAATTAACAAAACAGCTTTTAACCATTGTAGGCCTAAAAGCAGCCACCAAT\n
  AAAGAAAGCGTTCAAGCTCAACATAAAATTTCAATTAATTCCATAATTTACACCAACTTCCTAAACTTAAAATTGGGTTAATCTATAAC\n
  TTTATAGATGCAACACTGTTAGTATGAGTAACAAGAATTCCAATTCTCCAGGCATACGCGTATAACAACTCGGATAACCATTGTTAGTTA\n
  ATCAGACTATAGGCAATAATCACACTATAAATAATCCACCTATAACTTCTCTGTTAACCCAACACCGGAATGCCTAAAGGAAAGATCCAAA\n
  AAGATAAAAGGAACTCGGCAAACAAGAACCCCGCCTGTTTACCAAAAACATCACCTCTAGCATTACAAGTATTAGAGGCACTGC'''
  
  print (">>>Original DNA: ", X_test)              # Original DNA sequence

  # Y_test = E_DNA
  Y_test = E_DNA.lower()
  print (">>>Encoded DNA codes: ", Y_test)          # Encoded DNA bases

  P_test = P
  print (">>>Decimal Index values: ", P_test)       # Decimal values

  X_new = rep (X_test,Y_test,P_test)
  return X_new

print (">>>Cipher text: ",result_test())                         # Encrypted DNA or cipher text


print ('!!! The decryption process !!!')

'''>>>!!! @ THE DECRYPTION PROCESS!!! @ <<<'''
# ------------------------------------------------------------------------

'''>>>> FROM TEXT WORDS ---->>> ASCII DECIMAL <<<<'''
def toDecimal(a):                    # ASCII to Decimal conversion 
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l: 
    m.append(int(i))
  return m
# open file texts
f = open ("lines.txt", "r")        # call the ,txt file
data1 = f.read ()                     # read the file
print(data1)
data = data1[ :8]
# print (data)
P = toDecimal(data)                  # Converted ASCII to Decimal
print ('>>>Decimal Index values:', P)        
f.close ()

l = result_test()            # the encrypted DNA or cipher text
string = []
value = P                    # the index values of the text file  
index = 0
for i in value:              # for loop 
    index = index + i
    # print(index)           # index values        
    x = l[index]
    string.append(x)
print(string)

b = string                  # DNA bases 
# print ('Encrypted DNA bases', b)

Bb = ''.join(str(x) for x in b).upper()            # decrypted DNA string
print ('Encrypted DNA bases', Bb)

'''>>>> SUBSTITUTING DNA BASE(ATGC) ----->>> BINARY VALUE <<<<'''
# DNA bases marked as binary values 
def numbase(B):      
   ans= ""
   #  "A"='00', "C"='01', "G"='10', "T"='11'
   if(B == 'A'):
     ans= "00"
   elif(B == 'C'):
     ans= "01"
   elif(B == 'G'):
     ans= "10"
   elif(B == 'T'):
     ans= "11"
   return ans
#  for key bases
kb = (Bb[ :4])                   # splited the key bases
print ('Key bases is:', kb)
keyb = []   # null string
for i in kb:
  kb1 = numbase(i)              # use numbase function 
  keyb.append(kb1)
  keyb1 = ''.join(str(x) for x in keyb)   # converted list to string form 
  # print(keyb1)
# for XOR bases
xb = (Bb[4:8])                   # splited the XOR bases
print ('XOR bases is:', xb)
xorb = []  # null string
for i in xb:
  xb1 = numbase(i)              # use numbase function
  xorb.append(xb1)
  xorb1 = ''.join(str(x) for x in xorb)     # converted list to string form
  # print(xorb1)

'''>>>> XOR OPERATION (KEY & XOR VALUE) <<<<'''
# XOR of the two Binary Strings
def xor(a, b, l):
    ans = ""
    # Loop to iterate over the
    # Binary Strings
    for i in range(l):
        # If the Character matches
      if (a[i] == b[i]):
        ans += "0"
      elif (a[i] != b[i]):
        ans += "1"
      else:
        ans += None
    return ans
# the KEY & XOR values
# Driver Code 
a = keyb1    # xor_binary
print ('The key value is: ', a)
b = xorb1    # key_binary
l = 8        # length of the binary bases
XOR = xor(a, b, l)
print("The message value is:", XOR)

'''>>>> ASCII BINARY VALUE ----->>> ORIGINAL KEY <<<<'''
# Python program to illustrate the conversion of Binary to ASCII
# Initializing a binary string in the form of 0 and 1, with base of 2
o_key = int(a, 2);
or_key = o_key.bit_length() + 7 // 8
org_key = o_key.to_bytes(or_key, "big")
original_key = org_key.decode()
# Getting the ASCII value
print('The original key is:', original_key)

'''>>>> ASCII BINARY VALUE ----->>> ORIGINAL MESSAGE <<<<'''
# Python program to illustrate the conversion of Binary to ASCII
# Initializing a binary string in the form of 0 and 1, with base of 2
o_msg = int(XOR, 2);
or_msg = o_msg.bit_length() + 7 // 8
org_msg = o_msg.to_bytes(or_msg, "big")
original_message = org_msg.decode()
# Getting the ASCII value
print('The original message is:', original_message)