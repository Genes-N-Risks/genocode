def type2diabetes(filepath):
    """
    1. Takes a text file as the only parameter and returns means and std of the phenotype typeII diabetes
    2. Search for data labels on the text file and read text file to csv file starting from the
    rows of labels present
    3. Replace missing data '--' with NaN and drop missing data
    4. Looking for all 17 snps (we have in our data bank) in the uploaded file
    5. Recreate a list of 8 pairs of snp information: rsid and corresponding genotype
    6. Obtain effect values for each snp and sum up to get a polygenic risk score
    7. Based on the polygenic risk score, return a mean and std of the bmi phenotype
    
    """
    fopen = open(filepath,mode='r+')
    fread = fopen.readlines()
    x = '# rsid	chromosome	position	genotype'
    n = 0
    for line in fread:
        n += 1
        if x in line:
            break
    df = pd.read_csv (filepath,'\s+', skiprows=n, names=['rsid','chromosome','position','genotype'])
    #df = df.replace('--', pd.NaT)  # need to correct this on the data extract file
    #df = df.dropna
    testfile = df[(df['rsid'] == 'rs560887') | 
            (df['rsid'] =='rs10830963') |
            (df['rsid'] == 'rs14607517')|
            (df['rsid'] == 'rs2191349') | 
            (df['rsid'] == 'rs780094') | 
            (df['rsid'] == 'rs11708067') | 
            (df['rsid'] == 'rs7944584') | 
            (df['rsid'] == 'rs10885122') | 
            (df['rsid'] == 'rs174550') |
            (df['rsid'] == 'rs11605924') |
            (df['rsid'] == 'rs11920090') |
            (df['rsid'] == 'rs7034200') |
            (df['rsid'] == 'rs340874') |
            (df['rsid'] == 'rs11071657') |
            (df['rsid'] == 'rs13266634') |
            (df['rsid'] == 'rs7903146') |
            (df['rsid'] == 'rs35767')]
    testlist = []
    for i in range(0, len(testfile.index)-1):
        rsid = testfile.iloc[i,0]
        genotype = testfile.iloc[i,3]
        i = (rsid, genotype)    # tuples of one rsid with genotype
        testlist.append(i)      # a list of tuples
    gendata = pd.read_csv('Genetic Data.csv')
    gendata['effect'] = pd.to_numeric(gendata['effect'])
    total = 0
    for i in testlist:
        snp = gendata[(gendata['rsid'] == i[0]) & (gendata['genotype'] == i[1])]
        effect = snp.iloc[i,4]
        total += effect
    if total < 13:
        return (92.5, 8.7)
    elif total == 13:
        return (93.6, 8.8)
    elif total == 14:
        return (94.2, 8.6)
    elif total == 15:
        return (94.3, 8.8)
    elif total == 16:
        return (95.2, 8.9)
    elif total == 17:
        return (95.4, 8.7)
    elif total == 18:
        return (95.9, 8.9)
    elif total == 19:
        return (96.5, 8.7)
    elif total == 20:
        return (97.3, 8.8)
    elif total == 21:
        return (98.1, 8.6)
    elif total == 22:
        return (98.6, 8.7)
    else:
        return (98.6, 8.6)
