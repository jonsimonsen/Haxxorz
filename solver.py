#Initializing variables

code =      [ 0, 5, 0, 5, 10, 8, 11, 0, 12, 6, 5, 2, 7, 13, 3, 14, 3, 1, 9, 7, 0, 1, 3, 8, 3,
            1, 0, 15, 0, 9, 4, 16, 3, 1, 5, 7, 8, 4, 11, 12, 6, 16, 2, 15, 14, 2, 4, 0, 6,
            1, 13, 2, 17, 2, 4, 17, 6, 1, 2, 7, 10, 9, 4, 1]

subcode = [2, 1, 5, 3, 0, 1, 2, 4, 2, 1]

chars =     ['e', 't', 'a', 'o', 'i', 'n', 's', 'h']
extras =    ['r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

#It appears that the following could be refactored into a recursive function. Should consider doing that if the code is reused later.
for a in range(len(chars)):
    ares = list()
    achars = list(chars)
    ares.append(achars.pop(a))

    for b in range(len(achars)):
        bres = list(ares)
        bchars = list(achars)
        bres.append(bchars.pop(b))

        for c in range(len(bchars)):
            cres = list(bres)
            cchars = list(bchars)
            cres.append(cchars.pop(c))

            for d in range(len(cchars)):
                dres = list(cres)
                dchars = list(cchars)
                dres.append(dchars.pop(d))

                for e in range(len(dchars)):
                    eres = list(dres)
                    echars = list(dchars)
                    eres.append(echars.pop(e))

                    for f in range(len(echars)):
                        fres = list(eres)
                        fchars = list(echars)
                        fres.append(fchars.pop(f))

                        output = ''

                        for z in range(len(subcode)):
                            if subcode[z] in range(0, len(fres)):
                                output = output + fres[subcode[z]]
                            else:
                                output = output + '-'

                        print(output)
