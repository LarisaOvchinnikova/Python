#doesn't work(((
for x1 in range(1, 10):
    print('x1=', x1)
    for x2 in range(2, 8, 2):
        if x1 != x2:
            print('x2=', x2)
            for x3 in range(1, 10):
                if (x1 + x2 + x3) % 3 == 0 and x3 != x1 and x3!= x2:
                    print('x3=', x3)
                    for x4 in range(2, 9, 2):

                        z = set()
                        z.add(x1)
                        z.add(x2)
                        z.add(x3)
                        z.add(x4)
                        if (x1*1000 + x2*100 + x3*10 + x4) % 4 == 0 and len(z) == 4:
                            print('x4=', x4)
                            for x6 in range(2, 9, 2):
                                z = {5}
                                z.add(x1)
                                z.add(x2)
                                z.add(x3)
                                z.add(x4)
                                z.add(x6)
                                if (x1 + x2 + x3 + x4 + 5 + x6) % 3 == 0 and len(z) == 6:
                                    print('x6=', x6)
                                    for x7 in range(1, 10):
                                        z = {5}
                                        z.add(x1)
                                        z.add(x2)
                                        z.add(x3)
                                        z.add(x4)
                                        z.add(x6)
                                        z.add(x7)
                                        if(x1*1000000 + x2*100000 + x3*10000 + x4*1000 + 500 + x6*10 + x7) % 7 == 0 and len(z) == 7:
                                            print('x7=', x7)
                                            for x8 in range(1, 10):
                                                z = {5}
                                                z.add(x1)
                                                z.add(x2)
                                                z.add(x3)
                                                z.add(x4)
                                                z.add(x6)
                                                z.add(x7)
                                                z.add(x8)
                                                if (x6*100 + x7 *10 + x8) % 8 == 0 and len(z) == 8:
                                                    print('x8=', x9)
                                                    for x9 in range(1, 10):
                                                        z = {5}
                                                        z.add(x1)
                                                        z.add(x2)
                                                        z.add(x3)
                                                        z.add(x4)
                                                        z.add(x6)
                                                        z.add(x7)
                                                        z.add(x8)
                                                        z.add(x9)
                                                        if (x1+ x2+ x3+ x4+ 5+ x6+ x7+ x8+ x9) % 9 == 0 and len(z) == 9:
                                                            print(f"{x1}{x2}{x3}{x4}{5}{x6}{x7}{x8}{x9}0")
                                                            break


