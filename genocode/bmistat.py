def bmistat(filepath):
    """
    1. Takes a text file as the only parameter and returns means and std of the phenotype BMI
    2. Search for data labels on the text file and read text file to csv file starting from the
    rows of labels present
    3. Replace missing data '--' with NaN and drop missing data
    4. Looking for all 8 snps (we have in our data bank) in the uploaded file
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
    txt = pd.read_csv (filepath,'\s+', skiprows=n, names=['rsid','chromosome','position','genotype'])
    txt.to_csv('../genome_Thomas_Wood.csv',index=False)
    df = pd.read_csv('../genome_Thomas_Wood.csv')
    #df = df.replace('--', pd.NaT)  # need to correct this on the data extract file
    #df = df.dropna
    testfile = df[(df['rsid'] == 'rs9939609') | 
            (df['rsid'] =='rs6548238') |
            (df['rsid'] == 'rs17782313') |
            (df['rsid'] == 'rs10938397') | 
            (df['rsid'] == 'rs7498665') | 
            (df['rsid'] == 'rs10838738') | 
            (df['rsid'] == 'rs11084753') |
            (df['rsid'] == 'rs2815752')]
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
        effect = snp.iloc[0,4]
        total += effect
    if total < 4:
        return (25.4, 3.1)
    elif total == 4:
        return (25.7, 3.4)
    elif total == 5:
        return (25.9, 3.8)
    elif total == 6:
        return (26.2, 3.7)
    elif total == 7:
        return (26.2, 3.6)
    elif total == 8:
        return (26.3, 3.7)
    elif total == 9:
        return (26.5, 3.7)
    elif total == 10:
        return (26.6, 3.9)
    elif total == 11:
        return (26.8, 4.2)
    elif total == 12:
        return (27, 4)
    else:
        return (26.8, 3.8)
