subory = ['', '1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt']
with open('words_alpha.txt', 'r') as f:
    with open('1.txt', 'w') as jeden:
        with open('2.txt', 'w') as dva:
            with open('3.txt', 'w') as tri:
                with open('4.txt', 'w') as styri:
                    with open('5.txt', 'w') as pat:
                        with open('6.txt', 'w') as sest:
                            with open('7.txt', 'w') as sedem:
                                with open('8.txt', 'w') as osem:
                                    with open('9.txt', 'w') as devat:
                                        with open('10.txt', 'w') as desat:
                                            subory = ['', jeden, dva, tri, styri, pat, sest, sedem, osem, devat, desat]
                                            for line in f:
                                                if(line[-1]=='\n'):
                                                    line = line[:-1]
                                                try: 
                                                    subory[len(line)].write(line + '\n')
                                                except IndexError:
                                                    pass
print("hotovo")

        
