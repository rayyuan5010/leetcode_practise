def deleteReoccurringCharacters(input):
    show_up = []
    output = []
    for i in input:
        if not i in show_up:
            show_up.append(i)
            output.append(i)
    return "".join(output)


print(deleteReoccurringCharacters("aaacggggbbbsssewaf"))