"""
Convert DNA sequence to RNA
"""


def rna(seq):
    """
    Convert DNA sequence to RNA
    """
    # Determine if sequence was upper case
    seq_upper = seq.isupper()

    # Convert to lower case
    seq = seq.lower()

    # Swap out "t" with "u"
    seq = seq.replace('t', 'u')

    # Return upper or lower case RNA seq
    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_complement(seq):
    """
    Convert DNA into its reverse complement as RNA
    """
    # Determine if original was uppercase
    seq_upper = seq.isupper()

    # Reverse sequence
    seq = seq[::-1]

    # Convert to upper
    seq = seq.upper()

    # Compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    # Return result
    if seq_upper:
        return seq.upper()
    else:
        return seq
