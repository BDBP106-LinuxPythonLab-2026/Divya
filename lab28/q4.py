import sys

from Bio.Seq import Seq
from Bio.Restriction import EcoRI, BamHI
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, SimpleLocation
from Bio import SeqIO

plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")
record = SeqRecord(plasmid_seq, id = "PLAB001", name = "PLAB001")
record.annotations["molecule_type"] = "DNA"
bamhi = SeqFeature(SimpleLocation(0,6), type = "misc_feature", qualifiers = {"note": "bamhi site"})
cds = SeqFeature(SimpleLocation(8,41, strand = 1), type = "CDS", qualifiers = {"gene": "lab A", "translation": "MASKGEELFT"})
ecor1 = SeqFeature(SimpleLocation(41,47), type = "misc_feature", qualifiers = {"note": "ecor1 site"})

record.features.append(bamhi)
record.features.append(cds)
record.features.append(ecor1)

SeqIO.write(record, "lab_construct.gb", "genbank")

new_record = SeqIO.read("lab_construct.gb", "genbank")

for f in new_record.features:
    start = int(f.location.start)
    end = int(f.location.end)

    if "gene" in f.qualifiers:
        label = f.qualifiers["gene"][0]
    else:
        label = f.qualifiers["note"][0]

    print(f.type, start, end, label)

for f in new_record.features:
    if f.type == "CDS":
        dna = f.extract(new_record.seq)
        protein = str(dna.translate(to_stop=True))
        stored = f.qualifiers["translation"][0]
        print(protein)
        print(stored)
        print(protein == stored)

    