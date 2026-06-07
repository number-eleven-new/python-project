sequence_1 = list(input("Enter a DNA sequence: "))
sequence_2 = list(input("Enter a DNA sequence: "))
sequence_3 = list(input("Enter a DNA sequence: "))
sequence_4 = list(input("Enter a DNA sequence: "))

def add(sequence, base):
	_ = 0
	for u in sequence:
		if u == base:
		_ += 1
	return _

nucleotide = "C"
result = add(sequence_1, nucleotide)