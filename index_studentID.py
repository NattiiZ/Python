stID = input('Enter Student ID : ')
add = '-'
idFormat = stID[0:2] + add + stID[2:8] + add + stID[8:12] + add + stID[12]

print("Student Format ID :", idFormat)