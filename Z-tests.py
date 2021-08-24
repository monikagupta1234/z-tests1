import statistics as s
import pandas as p
import plotly.graph_objects as pgo
import plotly.Fiqure_factory as pff
import random as r 

df = p.read_csv("data.csv")
data = df["Math_score"].toList()

mean = s.mean(data)
print("Population Mean " + str(mean))

def randomSetOfSample():
    sampleSet=[]
    for i in range(0,30):
        ran = r.randint(0,len(data)-1)
        sampleSet.append(data[ran])

    SampleMean = s.mean(sampleSet)
    return(SampleMean)

meanOfSample = []
for i in range(0,100):
    mean1 =  randomSetOfSample()
    meanOfSample.append(mean1)



standradDeviation = s.stdev(meanOfSample)
firstStdevStart = mean - standradDeviation
firstStdevEnd = mean + standradDeviation 
print("Standrad Deviation" + str(standradDeviation))

secondStdevStart = mean - (2 * standradDeviation )
secondStdevEnd = mean + (2 * standradDeviation)

thirdStdevStart = mean - (3 * standradDeviation)
thirdStdevEnd = mean + (3 * standradDeviation)

sampleMean = p.read_csv("intervention.csv")

data1 = sampleMean ["Math_score"].tolist()

mean1 = s.mean(data1)
print("intervention Mean" + str(mean1))

zscore = (mean-mean) / standradDeviation

print("Z Test results" + str(zscore))


fig = pff.create_distplot([meanOfSample],["data"],show_hist=False)
fig.add_trace(pgo.scatter(x = [mean,mean], y = [0,0.15],mode = "lines",name="Mean"))
fig.add_trace(pgo.scatter(x = [firstStdevStart , firstStdevStart] , y = [0,0.15],mode = "lines",name="first Standard Deviation Start"))
fig.add_trace(pgo.scatter(x = [firstStdevEnd , firstStdevEnd] , y = [0,0.15],mode = "lines",name="first Standard Deviation End"))
fig.add_trace(pgo.scatter(x = [secondStdevStart , secondStdevStart] , y = [0,0.15],mode = "lines",name="second Standard Deviation Start"))
fig.add_trace(pgo.scatter(x = [secondStdevEnd , secondStdevEnd] , y = [0,0.15],mode = "lines",name="second Standard Deviation End"))
fig.add_trace(pgo.scatter(x = [thirdStdevStart , thirdStdevStart] , y = [0,0.15],mode = "lines",name="thrid Standard Deviation Start"))
fig.add_trace(pgo.scatter(x = [thirdStdevEnd , thirdStdevEnd] , y = [0,0.15],mode = "lines",name="thrid Standard Deviation End"))
fig.show()
