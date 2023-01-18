import csv
GENETIC_CODE = "genetic_code.csv"
NUCLEOTIDES = ("A", "C", "U", "G")


# This function is able to create the dictionary aminoacid-codons, using a relation between the aminoacid and a tuple of codons
def create_dictio():
    with open(GENETIC_CODE, encoding='utf8') as file:
        elements = dict()
        for aminoacid, codons in csv.reader(file):
            elements[aminoacid.rstrip()] = tuple(codons.rstrip().split(", "))
        return elements


# The function creates a list for each mRNA sequence found (sequence of codons, starting with the aminoacid "start").
# The function is able to split the input insert in multiple lists (if there are multiple mRNA sequences).
# Firstly, the function "check" is recalled to verify if every single gene is in the dictionary, otherwise "error"! (look at the function for more details ;-))
# Until the "start" aminoacid is found, the function continues to search for the "start" instruction, moving in 1 index.
# When the "start" aminoacid is found, the transcription inside the list starts until the "stop" aminoacid is found, moving in 3 indexes.
# Counter_genetic_code is useful to create a new sublist in case of a new different mRNA sequence is found.
# If the "start" aminoacid is found but not the "stop" one, error!
def single_genes_list(sequence, dictio):
    protein = list()
    first_found = False
    last_found = False
    finish = False
    counter_genetic_code = 0
    index = 0
    while not finish:
        check(sequence[index:index + 3], dictio)
        if index + 3 >= len(sequence):
            finish = True
        if not first_found and not last_found:
            if sequence[index:index + 3] in dictio["start"]:
                protein.append(list())
                protein[counter_genetic_code].append(sequence[index:index + 3])
                first_found = True
                index += 3
            else:
                index += 1
        elif first_found and not last_found:
            protein[counter_genetic_code].append(sequence[index:index + 3])
            if sequence[index:index + 3] in dictio["stop"]:
                last_found = True
            index += 3
        elif first_found and last_found:
            counter_genetic_code += 1
            first_found = False
            last_found = False
    if first_found and not last_found:
        exit("Error! Insert a valid sequence! The first codon is found, but it doesn't terminate!")
    return protein


# This function is able to check that all elements in the input are in the dictionary. Otherwise, error!
# The second part is dedicated to those elements which have a length smaller than 3. The function is able to check if those elements contains nucleotides.
# This section is fundamental: example from GitHub - GUAUGCACGUGACUUUCCUCAUGAGCUGAU (the sequence terminates with the codon UGA and the last element to check is U, that is smaller than 3).
def check(gene, dictio):
    checked = False
    for key in dictio:
        for elements in dictio[key]:
            if elements == gene:
                checked = True
                break
    if len(gene) < 3:
        for index_nucleotide, nucleotide in enumerate(gene):
            for index_tuple, element_tuple in enumerate(NUCLEOTIDES):
                if nucleotide == element_tuple:
                    checked = True
                    break
                else:
                    checked = False
    if not checked:
        exit("Error! Something went wrong, please check your mRNA sequence!")


# This function is able to unpack the dictionary and to convert every single codon of the mRNA sequence in aminoacid.
# The codon must be equal to the element in the dictionary and what is requested to do is to avoid to translate the word "start", but the correct aminoacid.
def convert_protein(proteins_list, dictio):
    protein_string = ""
    if len(proteins_list) == 0:
        exit("Error! The sequence is not supported! No values to translate!")
    for index_protein, protein in enumerate(proteins_list):
        for index_gene, gene in enumerate(protein):
            for aminoacid in dictio:
                for element in dictio[aminoacid]:
                    if element == gene and aminoacid != "start":
                        protein_string += aminoacid
    return protein_string


def main():
    try:
        mrna_code = create_dictio()
        print("***** mRNA translator *****")
        sequence = input("Insert a sequence of mRNA to translate (lower or upper case): ")
        print(convert_protein(single_genes_list(sequence.upper(), mrna_code), mrna_code))
    except OSError as error:
        print(f"Error! {error}")


if __name__ == "__main__":
    main()
