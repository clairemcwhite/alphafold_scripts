import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def get_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fasta", dest = "fasta_path", type = str, required = True,
                         help="path to a fasta of protein sequences")
    parser.add_argument("-s", "--seglength", dest = "seglength", type = int, required = True,
            help="How long each segment should be ex. 400")
    parser.add_argument("-o", "--offset", dest = "offset", type = int, required = True,
            help="How much each segment should be off set (ex. 200)")
  
    
def get_segments(fasta, seglength, offset):
         

    for record in SeqIO.parse(fasta, "fasta"):
        for i in range(0, len(record.seq), offset)
            if i >= len(record.seq):
                 break
            identifier = "_{}_{}".format(i, i + seglength)
            segment = record.seq[i:i + seglength]
            segment_id = record.id + identifier  
            newrecord = SeqRecord(
                        Seq(segment),
                            id=segment_id)
            outfile = fasta.replace(".fasta", "")  + segment_id + ".fasta"
            with open(outfile, "w") as o:
               SeqIO.write(newrecord, o, "fasta")


if __name__ == "__main__":
  args = get_embed_args()
  fasta = args.fasta

  seglength = args.seglength
  offset = args.offset
  segments = get_segment(fasta, seglength, offset)


