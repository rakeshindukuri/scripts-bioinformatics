"""
Requires:
pip install biopython
pip install clustalo
"""

from Bio import Entrez, SeqIO
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo
import ssl
import sys
from Bio.Align.Applications import ClustalOmegaCommandline

import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context

def download_sequences(query, retmax=10, format="fasta"):
    Entrez.email = "your.email@example.com"
    handle = Entrez.esearch(db="nucleotide", term=query, retmax=retmax)
    record = Entrez.read(handle)
    handle = Entrez.efetch(db="nucleotide", id=record["IdList"], rettype=format, retmode="text")
    records = list(SeqIO.parse(handle, format))
    handle.close()
    return records


def align_sequences(sequences):
    """
    Align gene sequences using Clustal Omega.
    Returns a Bio.Align.MultipleSeqAlignment object.
    """
    input_file = "sequences.fasta"
    with open(input_file, "w") as handle:
        SeqIO.write(sequences, handle, "fasta")
    cline = ClustalOmegaCommandline(infile="sequences.fasta", outfile="alignment.fasta", verbose=True, force=True)
    stdout, stderr = cline()
    output_file = "alignment.aln"
    alignment = AlignIO.read(output_file, "clustal")
    return alignment


def construct_phylogenetic_tree(alignment):
    """
    Construct a phylogenetic tree using the neighbor-joining method.
    Returns a Bio.Phylo.BaseTree.Tree object.
    """
    calculator = DistanceCalculator("identity")
    dm = calculator.get_distance(alignment)
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)
    return tree

if __name__ == "__main__":
    print("Usage: python seq2align2phylo.py <query sequence name>")
    if len(sys.argv) > 1:
        query_seq_name = sys.argv[1]
    else:
        print("User failed to enter: Querying for human insulin")
        query_seq_name = "human insulin"
    sequences = download_sequences(query_seq_name, retmax=5)
    alignment = align_sequences(sequences)
    tree = construct_phylogenetic_tree(alignment)
    Phylo.draw(tree)
