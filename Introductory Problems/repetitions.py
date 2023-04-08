from collections import defaultdict


def repetitions(sequence):
    dict_occurrences = defaultdict(int)
    previous_char = sequence[0]
    occurences = 1
    dict_occurrences[previous_char] = occurences

    # Calculate occurences
    for i in range(1, len(sequence)):
        if previous_char == sequence[i]:
            occurences += 1
        else:
            if occurences > dict_occurrences[previous_char]:
                dict_occurrences[previous_char] = occurences
            previous_char = sequence[i]
            occurences = 1

    if occurences > dict_occurrences[previous_char]:
        dict_occurrences[previous_char] = occurences

    return max(dict_occurrences.values())


def repetitions2(sequence):
    prev_char = sequence[0]
    occurence_char = 1
    max_occurence = 1

    for i in range(1, len(sequence)):
        if sequence[i] == prev_char:
            occurence_char += 1
        else:
            max_occurence = max(occurence_char, max_occurence)
            prev_char = sequence[i]
            occurence_char = 1

    max_occurence = max(occurence_char, max_occurence)

    return max_occurence


def repetitions3(sequence):
    prev_char = sequence[0]
    occurence_char = 0
    max_occurence = 0

    for char in sequence:
        if char == prev_char:
            occurence_char += 1
        else:
            max_occurence = max(occurence_char, max_occurence)
            prev_char = char
            occurence_char = 1

    max_occurence = max(occurence_char, max_occurence)

    return max_occurence


if __name__ == "__main__":
    dna_sequence = input()
    print(repetitions3(dna_sequence))
