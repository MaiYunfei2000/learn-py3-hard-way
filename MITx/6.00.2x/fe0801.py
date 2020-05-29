import pylab, random
random.seed(0)

####################
## Helper functions#
####################
def flipCoin(numFlips):
    '''
    Returns the result of numFlips coin flips of a biased coin.

    numFlips (int): the number of times to flip the coin.

    returns: a list of length numFlips, where values are either 1 or 0,
    with 1 indicating Heads and 0 indicating Tails.
    '''
    with open('coin_flips.txt','r') as f:
        all_flips = f.read()
    # https://docs.python.org/zh-cn/3/library/random.html#random.sample
        # 无重复的随机抽样。返回从总体序列 all_filps 中选择的唯一元素
        #（这里不是 H 就是 T ）的长度为 numFlips 的列表。
        # 也就是抛 numFlips 次硬币，把结果记录到列表里。
    flips = random.sample(all_flips, numFlips)
    # print("flips:", flips)
    # 返回一个列表，把 flips 中的每个 H 转换为 1 ，每个 T 转换为 2 。
    return [int(flip == 'H') for flip in flips]

# a = flipCoin(100)
# print("a:", a)

def getMeanAndStd(X):
    """
    输入：序列 X 
    输出：二元组 (X 的均值, X 的标准差)
    """
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        # 就是方差公式的分母
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std


#############################
## CLT Hands-on             #
##                     #
## Fill in the missing code #
## Do not use numpy/pylab   #
#############################
meanOfMeans, stdOfMeans = [], []
sampleSizes = range(10, 500, 50)

def clt():
    for sampleSize in sampleSizes:
        sampleMeans = []
        # 在每系列抛硬币中，得到一个样本并求其均值，append 进 sampleMeans
        for t in range(20):
            # 以 sampleSize 作为抛硬币次数，获得一系列抛硬币结果作为此次 toss 的样本
            sample = flipCoin(sampleSize)
            sampleMeans.append(getMeanAndStd(sample)[0])
        ## FILL IN TWO LINES
        ## WHAT TO DO WITH THE SAMPLE MEANS?
        # print(len(sampleMeans), sampleSize)
        meanOfMeans.append(sum(sampleMeans) / len(sampleMeans))
        stdOfMeans.append(getMeanAndStd(sampleMeans)[1])

clt()
pylab.figure(1)
pylab.errorbar(sampleSizes, meanOfMeans,
               yerr = 1.96*pylab.array(stdOfMeans),
               label = 'Est. mean and 95% confidence interval')
pylab.xlim(0, max(sampleSizes) + 50)
pylab.axhline(0.65, linestyle = '--',
              label = 'True probability of Heads')
pylab.title('Estimates of Probability of Heads')
pylab.xlabel('Sample Size')
pylab.ylabel('Fraction of Heads (minutes)')
pylab.legend(loc = 'best')
pylab.show()