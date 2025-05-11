def apply_processors(input_path, output_path, processors):
    with open(input_path, 'r') as infile:
        lines = infile.readlines()
    for processor in processors:
        lines = [processor(line) for line in lines]
    with open(output_path, 'w') as outfile:
        for line in lines:
            outfile.write(line + '\n')
