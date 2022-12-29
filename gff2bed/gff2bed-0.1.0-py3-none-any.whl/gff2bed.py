#===============================================================================
# gff2bed.py
#===============================================================================

"""Convert GFF3 data to BED format"""

# Imports ======================================================================

import gzip




# Functions ====================================================================

def parse_gff_attributes(attr: str):
    """Parse an entry from the "attr" column of a GFF3 file and return it as
    a dict

    Parameters
    ----------
    attr : str
        feature attribute string

    Returns
    ------
    dict
        attr entries as a dict
    """

    return dict(pair.split('=') for pair in attr.split(';'))


def parse_gff(gff, type: str = 'gene', parse_attr: bool = True):
    """Parse a GFF3 file and yield its lines as tuples

    Parameters
    ----------
    gff
        path to GFF3 file
    type
        string indicating feature type to include, or None to include all
        features
    parse_attr : bool
        if False, do not parse attributes
    
    Yields
    ------
    seqid, start, end, strand, attr
        coordinates of a feature
    """

    with (gzip.open(gff, 'rt') if str(gff).endswith('.gz') else open(gff, 'r')) as f:
        for line in f:
             if not line.startswith('#'):
                seqid, _, t, start, end, _, strand, _, attr = line.rstrip().split('\t')
                if ((t == type) or (type is None)):
                    if parse_attr:
                        yield (seqid, int(start), int(end), strand,
                            parse_gff_attributes(attr))
                    else:
                        yield seqid, int(start), int(end), strand, '.'


def generate_bed(gff, type: str = 'gene', tag: str = 'ID'):
    """Convert rows of GFF3 data to BED data. This involves reordering the
    columns to conform with BED format and shifting the coordinates to 0-based
    half-open values.

    Parameters
    ----------
    gff
        path to GFF3 file
    type
        type of GFF3 record to parse
    tag : str
        GFF3 attribute tag to parse [ID]

    Yields
    ------
    tuple
        a row of BED data
    """

    for seqid, start, end, strand, attr in parse_gff(gff, type=type):
        yield seqid, start - 1, end, attr[tag], 0, strand
