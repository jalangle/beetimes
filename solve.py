#!python3

def main():
	count = 0
	to_find = "otiznga"
	
	with open("wordlist.txt", 'r') as f:
		for word in f:
			word = word.rstrip()
			if(len(word) < 4): #remove anything less than 4 characters as too short to be included
				continue
			if(len(word) > 10): #remove anything longer than 10 characters as unlikely to be included
				continue
			if(not word.isalpha()): #remove anything that isn't entirely alphabetic
				continue
			if(word.find(to_find[0]) == -1): #remove anything that doesn't contain the first character of the search list
				continue
			
			illegal_chars = False
			for c in word:
				if(to_find.find(c) == -1):
					illegal_chars = True
			
			if(not illegal_chars):
				print(word)
				count += 1
		
	print(str(count))
	
main()
