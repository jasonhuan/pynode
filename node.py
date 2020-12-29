import hashlib
import asyncio
import sys

async def main():
	if(len(sys.argv) > 0):
		pass #implement mining function

	# block header is 80 bytes total; for now, these are dummy values
	# 4 byte field – change upon version upgrade (BIP implementation)
	version = 0b00000000000000000000000000000001

	# 32 byte field – SHA256 output of previous block header
	hashPrevBlock = 0b0000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111

	# 32 byte field – merkle root of the merkle tree of transactions in the block
	hashMerkleRoot = 0b0000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111
	
	# 4 byte field – in production, the unix epoch time
	time = 0b00000000000000000000000000000001
	
	# 4 byte field – adjust this to change tolerance of number of leading zeroes that is considered a successful block
	difficulty = 0b00000000000000000000000000000010 # currently set to 2 leading zeroes
	
	# 4 byte field – change this for each guess
	nonce = 0b00000000000000000000000000001111
	
	
	isValid = hashBlock(version, hashPrevBlock, hashMerkleRoot, time, difficulty, nonce)
	
	print("Difficulty:", difficulty)
	print("Mined block is valid:", isValid)

	return



def hashBlock(version, hashPrevBlock, hashMerkleRoot, time, difficulty, nonce):
	# check field sizes; 1 byte = 8 bits = 2^8 binary values = 256
	# buggy for now
	if(version > (2^8)^4):
		print("version number out of range")
	if(hashPrevBlock > (2^8)^32): 
		print("hashPrevBlock out of range")
	if(hashMerkleRoot > (2^8)^32): # 32 byte field
		print("hashMerkleRoot out of range")
	if(time > (2^8)^4): # 4 byte field
		print("time out of range")
	if(difficulty > (2^8)^4): # 4 byte field
		print("difficulty out of range")
	if(nonce > (2^8)^4): # 4 byte field
		print("nonce out of range")

	blockHeader = version + hashPrevBlock + hashMerkleRoot + time + difficulty + nonce
	#print("blockHeader:", blockHeader)
	encodedBH = bytes(str(blockHeader), 'ascii', errors = 'replace')
	m = hashlib.sha256()
	m.update(encodedBH)
	#print("hexdigest:", m.hexdigest())
	binaryHash = int(m.hexdigest(), 16)
	#print("binaryHash:", binaryHash)
	binaryRepHash = str(bin(binaryHash))
	#print("str(binaryRepHash):", str(binaryRepHash))

	zeroCounter = 0
	i = 2
	
	while(len(binaryRepHash) < 258): # 256 bits plus '0b' prefix
		binaryRepHash = '0b0' + binaryRepHash[2:]

	print("SHA256 hash output:", binaryRepHash)
	while(int(binaryRepHash[i]) != 1):
		#print("brh loop:", binaryRepHash[i])
		zeroCounter += 1
		i += 1

	print("Leading Zeroes:", zeroCounter)
	
	if(zeroCounter >= difficulty):
		return True
	else:
		return False

if __name__ == "__main__":
    asyncio.run(main())