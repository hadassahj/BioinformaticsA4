#Find the percentage for all the dinucleotide and trinucleotide combinations for the sequence: 
# S="TACGTGCGCGCGAGCTATCTACTGACTTACGACTAGTGTAGCTGCATCATCGATCGA".

# 1. Build a brute force engine to generate all dinucleotide and trinucleotide combinations.
# 2. For each combination, find out the percentage inside the S sequence.
# 3. Show the percentage for each combination in the output of your implementation.

#Jercau Hadasa - Stefana, group 1241EB

#problem 1
list1=['A','T','C','G']
dinucleotide=[]
trinucleotide=[]

def brute_engine(): 
    # combinatii de 4 luate cate 2
    for i in list1:
        for j in list1:
            dinucleotide.append(i+j)
    # combinatii de 4 luate cate 3
    for i in list1:
        for j in list1:
            for k in list1:
                trinucleotide.append(i+j+k)
    return dinucleotide, trinucleotide

dinucleotide, trinucleotide = brute_engine()
print("Dinucleotide combinations: ", dinucleotide)
print("Trinucleotide combinations: ", trinucleotide)
print('\n')
print('\n')

#problem 2
S="TACGTGCGCGCGAGCTATCTACTGACTTACGACTAGTGTAGCTGCATCATCGATCGA"

def find_percentage(sequence, combinations):
    percentages = {}
    for comb in combinations:
        count = sequence.count(comb)
        percentages[comb] = (count / len(sequence)) * 100
    return percentages

#problem 3
dinucleotide_percentages = find_percentage(S, dinucleotide)
trinucleotide_percentages = find_percentage(S, trinucleotide)
print("Dinucleotide percentages: ", dinucleotide_percentages)
print("Trinucleotide percentages: ", trinucleotide_percentages)

print('\n')
print('\n')

#problem 1 in class
#find in sequence s only the dinucleotydes and trinucleotydes that exists without the use of brute force engine. 
#In order to achieve the results one must veriffy this combinations starting from the beginning. eg: s='abaa' dinucleotydes ab: 1, ba: 1, aa: 1; 
#trinucleotydes aba: 1, baa: 1
def find_existing_combinations(sequence, length):
    existing_combinations = {}
    for i in range(len(sequence) - length + 1):
        comb = sequence[i:i+length]
        if comb in existing_combinations:
            existing_combinations[comb] += 1
        else:
            existing_combinations[comb] = 1
    return existing_combinations

s1='aabaa'

existing_dinucleotides = find_existing_combinations(s1, 2)
existing_trinucleotides = find_existing_combinations(s1, 3)
print("Sequence s1: ", s1)
print("Existing dinucleotides in s1: ", existing_dinucleotides)
print("Existing trinucleotides in s1: ", existing_trinucleotides)

print('\n')
print('\n')

#problem 2 in class 
# Design an application using ai, which contains a gui that allows the user to choose a fasta file. The content of the file should be analysed by
# using a sliding window of 30 positions. The content for each sliding window should be used in order to extract the relative frequencies of the 
# symbols found in the alphabet of the sequeence. Thus your input will be the dna seq from the fasta file and the output will be the values from 
# the relative frequencies of each symbol for the alphabet of the sequence. 
# translate in lines on a chart thus your chart in the case of dna will have 4 lines, which reflect the values found over the sequnce. 

import tkinter as tk
from tkinter import filedialog, messagebox
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np


def read_fasta(file_path):
    """Read DNA sequence from a FASTA file"""
    record = next(SeqIO.parse(file_path, "fasta"))
    return str(record.seq).upper()


def sliding_window_analysis(sequence, window_size=30):
    """Compute relative frequencies of A, C, G, T for each sliding window"""
    alphabet = ['A', 'C', 'G', 'T']
    freq_dict = {base: [] for base in alphabet}

    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        total = len(window)
        for base in alphabet:
            freq_dict[base].append(window.count(base) / total)

    return freq_dict


def plot_frequencies(freq_dict):
    """Plot relative frequencies as 4 lines"""
    plt.figure(figsize=(10, 5))
    x = range(len(next(iter(freq_dict.values()))))
    for base, freqs in freq_dict.items():
        plt.plot(x, freqs, label=base)

    plt.title("Relative Nucleotide Frequencies (Sliding Window = 30)")
    plt.xlabel("Window Position")
    plt.ylabel("Relative Frequency")
    plt.legend()
    plt.grid(True)
    plt.show()


def open_file():
    """Open file dialog and analyze FASTA"""
    filepath = filedialog.askopenfilename(
        title="Select FASTA file",
        filetypes=[("FASTA files", "*.fasta *.fa *.fna"), ("All files", "*.*")]
    )
    if not filepath:
        return

    try:
        sequence = read_fasta(filepath)
        freq_dict = sliding_window_analysis(sequence)
        plot_frequencies(freq_dict)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# ---------- GUI ----------
root = tk.Tk()
root.title("DNA Frequency Analyzer (AI-based)")
root.geometry("400x200")

label = tk.Label(root, text="Select a FASTA file to analyze DNA frequencies", wraplength=300)
label.pack(pady=20)

button = tk.Button(root, text="Choose File", command=open_file, width=20, height=2, bg="#4CAF50", fg="white")
button.pack()

root.mainloop()



