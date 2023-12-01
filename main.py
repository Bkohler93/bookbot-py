def get_book_text(book_path):
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		return file_contents

def get_num_words(text):
	words = text.split()
	return len(words)

ALPHABET = [
	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]

def get_letter_totals(text):
	letter_map = {}
	for l in ALPHABET:
		letter_map[l] = 0
	for c in text:
		lower_c = c.lower()
		if lower_c not in ALPHABET:
			continue
		letter_map[c.lower()] += 1
	return letter_map

def print_report(num_words, letter_totals):
	print("-- Begin report of books/frankenstein.txt --")
	print(f"{num_words} words found in the document!\n")
	sorted_letter_totals = sorted(letter_totals.items(), key=lambda x:x[1], reverse=True)	
	for s in sorted_letter_totals:
		print(f"Character {s[0]} found {s[1]} times")

def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	letter_totals = get_letter_totals(text)
	print_report(num_words, letter_totals)

main()