#problem 3, lab1
def read_fasta(filename):
    """
    Citește un fișier FASTA și întoarce un dicționar:
    {nume_secventa: secventa}
    """
    sequences = {}
    name = None
    seq_parts = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                # salvăm secvența precedentă dacă există
                if name and seq_parts:
                    sequences[name] = "".join(seq_parts).upper()
                    seq_parts = []
                # nume nou
                name = line[1:]  
            else:
                seq_parts.append(line)

        # adăugăm ultima secvență
        if name and seq_parts:
            sequences[name] = "".join(seq_parts).upper()

    return sequences


def analyze_sequence(seq):
    """
    Calculează procentajele literelor unice dintr-o secvență.
    """
    alphabet = set(seq)
    results = {}
    for letter in alphabet:
        count = seq.count(letter)
        percentage = (count / len(seq)) * 100
        results[letter] = percentage
    return results


if __name__ == "__main__":
    # citește toate secvențele din fișier
    sequences = read_fasta("C:\\Users\\Hadassah\\Desktop\\Faculty\\bioinformatics\\example.fasta")

    # analizează fiecare secvență
    for name, seq in sequences.items():
        print(f"\n>>> Rezultate pentru {name} (lungime {len(seq)})")
        stats = analyze_sequence(seq)
        for letter, percentage in stats.items():
            print(f"   {letter}: {percentage:.2f}%")
