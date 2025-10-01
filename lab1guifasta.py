import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- FASTA Functions ----------------
def read_fasta(filename):
    sequences = {}
    name = None
    seq_parts = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name and seq_parts:
                    sequences[name] = "".join(seq_parts).upper()
                    seq_parts = []
                name = line[1:]
            else:
                seq_parts.append(line)
        if name and seq_parts:
            sequences[name] = "".join(seq_parts).upper()
    return sequences

def analyze_sequence(seq):
    alphabet = set(seq)
    results = {}
    for letter in alphabet:
        count = seq.count(letter)
        results[letter] = (count / len(seq)) * 100
    return results

# ---------------- GUI Functions ----------------
def select_file():
    global fasta_file
    fasta_file = filedialog.askopenfilename(
        title="Select FASTA File",
        filetypes=[("FASTA files", "*.fasta *.fa"), ("All files", "*.*")]
    )
    if fasta_file:
        file_label.config(text=f"Selected: " + fasta_file)

def show_results():
    if not fasta_file:
        messagebox.showerror("Error", "Please select a FASTA file first.")
        return
    sequences = read_fasta(fasta_file)
    result_text.delete("1.0", tk.END)
    for name, seq in sequences.items():
        result_text.insert(tk.END, f">>> {name} (length {len(seq)})\n")
        stats = analyze_sequence(seq)
        for letter, percentage in stats.items():
            result_text.insert(tk.END, f"   {letter}: {percentage:.2f}%\n")
        result_text.insert(tk.END, "\n")

# ---------------- GUI Layout ----------------
fasta_file = None
root = tk.Tk()
root.title("FASTA Analyzer")

file_btn = tk.Button(root, text="Select FASTA File", command=select_file)
file_btn.pack(pady=5)

file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=5)

result_btn = tk.Button(root, text="Show Results", command=show_results)
result_btn.pack(pady=5)

result_text = tk.Text(root, height=20, width=60)
result_text.pack(pady=10)

root.mainloop()
