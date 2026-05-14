def reverse_string(text):
	reversed_text = ""

	for character in text:
		reversed_text = character + reversed_text

	return reversed_text


if __name__ == "__main__":
	sample = "hello"
	print(reverse_string(sample))
