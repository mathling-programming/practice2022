import numpy as np
lines = 0
final = []

with open('C:\\Users\\LENOVO\\Desktop\\sample.csv', encoding = 'utf-8') as f:
    r = np.genfromtxt(f, delimiter = ',', skip_header=1)
    #print(r)
    for line in r:
        lines += 1
        a = np.array(line)
        mean = np.mean(a)
        otkl = np.std(a)
        #print(lines, otkl)
        if otkl < 250:
            out = lines, mean, otkl
            final.append(out)
            b = np.array(final)
            #print(out)
            #tofile = np.array(out)
            np.savetxt('C:\\Users\\LENOVO\\Desktop\\output.txt', b, fmt = '%.2f', delimiter = '\t')
        
