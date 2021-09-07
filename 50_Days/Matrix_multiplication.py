if __name__=='__main__':
    with open('./../Files/in2.txt') as f1:
        with open('./../Files/in1.txt') as f:
            a = f.readlines()
            b = f1.readlines()
            matrixa = []
            matrixb = []
            for line in a:
                var = line.split(",")
                #print(var)
                matA = []
                for line1 in var:
                    #print(line1)
                    matA.append(int(line1.replace(" ","").replace(";","").replace("\n","")))
                matrixa.append(matA)
            print(matrixa)
            for line in b:
                var = line.split(",")
                matB = []
                #print(var)
                for line1 in var:
                    #print(line1)
                    matB.append(int(line1.replace(" ","").replace(";","").replace("\n","")))
                matrixb.append(matB)
            print(matrixb)
            matrixc = []
            if len(matrixa[0]) == len(matrixb):
                print("Matrix multiplication possible")
                for i in range(0,len(matrixa)):
                    matc = []
                    for j in range(0,len(matrixb[0])):
                        c = 0
                        for k in range(0,len(matrixb)):
                            c += matrixa[i][k] * matrixb[k][j]
                        matc.append(c)
                    matrixc.append(matc)
                print(matrixc)
                with open('./../Files/out.txt', 'w') as f3:
                    for i in range(0,len(matrixc)):
                        for j in range(0, len(matrixc[0])):
                            if j == len(matrixc[0]) - 1:
                                f3.write('%s;' % matrixc[i][j])
                                break
                            f3.write('%s, ' % matrixc[i][j])
                        f3.write("\n")
            else:
                print("Cannot do matrix multiplication")





