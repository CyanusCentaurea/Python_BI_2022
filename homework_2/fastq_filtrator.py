def gc_in_bounds(seq: str, gc_bounds=(0, 100)):
    """gc_in_bounds(seq, gc_bounds=(0, 100))

    Counts gc_content for the sequence (seq) and determines if the received value is in gc_bounds.
    """
    gc_content = (seq.count('G') + seq.count('C')) / len(seq) * 100
    if isinstance(gc_bounds, int) and gc_content <= gc_bounds:
        return True
    elif isinstance(gc_bounds, tuple) and gc_bounds[0] <= gc_content <= gc_bounds[1]:
        return True
    else:
        return False


def len_in_length_bounds(seq, length_bounds=(0, 2**32)):
    """len_in_length_bounds(seq, length_bounds=(0, 2**32))
    Counts length of the sequence (seq) and determines if the received value is in length_bounds.
    """
    if isinstance(length_bounds, int) and len(seq) <= length_bounds:
        return True
    elif isinstance(length_bounds, tuple) and length_bounds[0] <= len(seq) <= length_bounds[1]:
        return True
    else:
        return False


def mean_quality_in_threshold(quality_line, quality_threshold=0):
    """mean_quality_in_threshold(quality_line, quality_threshold=0)
        Counts mean value of the quality_line and determines if the received value is greater than or equal to
        quality_threshold.
        """
    mean_quality = sum([ord(i) - 33 for i in quality_line]) / len(quality_line)
    if mean_quality >= quality_threshold:
        return True
    else:
        return False


def main(input_fastq: str,
         output_file_prefix: str,
         gc_bounds=(0, 100),
         length_bounds=(0, 2**32),
         quality_threshold=0,
         save_filtered=False):
    """main(input_fastq: str,
         output_file_prefix: str,
         gc_bounds=(0, 100),
         length_bounds=(0, 2**32),
         quality_threshold=0,
         save_filtered=False)
         Writes read from the input_fastq file to the output_file_prefix+_passed.fastq if every of gc_bounds,
         length_bounds and quality_threshold functions returns True for this read. Else writes this read to the
         output_file_prefix+_failed.fastq if save_filtered=False.
         """
    with open(input_fastq) as file:
        file = [line.strip() for line in file.readlines()]
        input_dict = {}
        while file:
            input_dict[file[0]] = [file[i] for i in range(1, 4)]
            file = file[4:]
    for read in input_dict:
        seq = input_dict[read][0]
        quality_line = input_dict[read][2]
        if gc_in_bounds(seq, gc_bounds) and \
                len_in_length_bounds(seq, length_bounds) and  \
                mean_quality_in_threshold(quality_line, quality_threshold):
            with open(output_file_prefix + "_passed.fastq", 'a') as passed:
                print(read, file=passed)
                for i in input_dict[read]:
                    print(i, file=passed)
        elif save_filtered:
            with open(output_file_prefix + "_failed.fastq", 'a') as failed:
                print(read, file=failed)
                for i in input_dict[read]:
                    print(i, file=failed)

