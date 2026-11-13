import sys

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, SimpleLocation

records = list(SeqIO.parse("lab_genes.fasta", "fasta"))
print("length of records", len(records))

for record in records:
    gc = gc_fraction(record.seq)*100
    protein = record.seq.translate(to_stop=True)
print(f"{record.id},{len(record.seq)},{gc:.1f},{protein}")    
    

high_gc = [r for r in records if gc >=50]
count = SeqIO.write(high_gc, "lab_high_gc.fasta", "fasta")
print("records written to lab_high_gc.fasta", count)

