import Bio
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, SimpleLocation

thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
print(len(thrL))
print(f"GC content: {gc_fraction(thrL)}")
print(thrL.complement())      
print(thrL.reverse_complement())
print(thrL.transcribe())
print(thrL.translate())
print(thrL.translate(to_stop=True)) 
print(thrL.count('ACC'))
print(f"last codon: {thrL[-1]}")
print(f"first 12 bases of rc: {thrL.reverse_complement()[:12]}")