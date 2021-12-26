from rosalind_utils import mass_to_aa

def build_peptide(n, frag_dict, peptide='', aa=0):

    if aa == 0:
        aa = min(frag_dict)
    
    if len(peptide) == n:
        return peptide
    else:
        for i in frag_dict[aa]:
            return build_peptide(n, frag_dict, peptide+i[0], i[1])


def peptide_from_fragments(p, l):
    n = (len(l)-2)/2
    

    pairs = {}
    for i in range(len(l)):
        for j in range(i, len(l)):
            aa = mass_to_aa(l[j]-l[i])
            if aa:
                if l[i] in pairs:
                    pairs[l[i]].append((aa, l[j]))
                else:
                    pairs[l[i]] = [(aa, l[j])]
        
    peptide = build_peptide(n, pairs)
    
    return peptide


def main():
    with open('./rosalind_full.txt', 'r') as infile:
        p = float(infile.readline().strip())
        frags = list(map(float, infile.readlines()))
     
    print(peptide_from_fragments(p, frags))


if __name__ == '__main__':
    main()