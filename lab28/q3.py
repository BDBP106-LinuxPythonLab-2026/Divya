from Bio.Seq import Seq

mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")
rc = mystery.reverse_complement()

frames = []
for s in (mystery, rc):
    for i in range(3):
        sub = s[i:]
        sub = sub[:len(sub) - len(sub) % 3]
        protein = str(sub.translate())
        frames.append(protein)
        print(protein)

for protein in frames:
    