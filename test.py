data = [['nameservers','panel'], ['nameservers','panel']]

with open("output.txt", "w") as txt_file:
    for i in data:
        txt_file.write(" ".join(i) + "\n") 