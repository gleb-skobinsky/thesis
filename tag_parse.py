from nltk.tokenize import word_tokenize
from nltk import pos_tag

noun_tags = {"NN", "NNS", "NNP", "NNPS"}

with open("finkler.txt", "r") as f:
    text = f.read()
    f.close()

sent_tokens = word_tokenize(text)
sent_pos = pos_tag(sent_tokens)

count = 1
with open("potential_compounds.txt", "a") as output:
    for i in range(len(sent_pos)):
        current = sent_pos[i]
        try:
            next_pos = sent_pos[i+1]
            if current[1] in noun_tags and next_pos[1] in noun_tags:
                output.write(f"{count}. {current[0]} {next_pos[0]}\n")
                count += 1
        except IndexError:
            print("End of document")
    output.close()
