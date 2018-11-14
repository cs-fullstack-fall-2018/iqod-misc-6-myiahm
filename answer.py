def stars(input):
    for i in range(input):
        s = "*"


        for x in range(i):
            s+= s

        print(s+str(i))


stars(4)
