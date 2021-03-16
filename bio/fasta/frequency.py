import sys

from bio.fasta import radix
from bio.fasta import nodes


def convert_to_list(seq_dict):
    seq_list = []
    for v in seq_dict.values():
        seq_list.append(v)
    return seq_list


def build_sequence_dict(fasta_filepath):
    max_val = 0
    seq_dict = {}
    with open(fasta_filepath, 'r') as f:
        lines = f.readlines()
        i = 1
        while i < len(lines):
            seq = lines[i].strip('\n')
            if seq_dict.get(seq):
                seq_dict[seq].cnt += 1
                if seq_dict[seq].cnt > max_val:
                    max_val = seq_dict[seq].cnt
            else:
                seq_dict[seq] = nodes.SeqNode(seq)
            i += 2
    return seq_dict, max_val


def build_output_message(seq_list):
    output_msg = ""
    for i in range(1, min(10, len(seq_list))):
        seq_node = seq_list[-i]
        output_msg += f"Sequence: {seq_node.seq}\n"
        output_msg += f"Sequence Frequency Count: {seq_node.cnt}\n\n"
    return output_msg


def main():
    fasta_filepath = sys.argv[1]
    seq_dict, max_val = build_sequence_dict(fasta_filepath)
    seq_list = convert_to_list(seq_dict)
    radix.RadixSort().sort(seq_list, max_val)
    output_msg = build_output_message(seq_list)
    print(output_msg)


if __name__ == "__main__":
    main()