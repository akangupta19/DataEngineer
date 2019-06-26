def find_prob(event, samplespace):
    probability=(event/samplespace)*100
    return round(probability,1)


sample = {'HHH','HHT','HTH','HTT','THH','THT','TTH','TTT'}
sample=8
oneh=1

probability1=find_prob(oneh,sample)

sample=8
threeh=3

probability2=find_prob(threeh,sample)


sample=8
A=4
B=7

probabilityA=find_prob(A,sample)
probabilityB=find_prob(B,sample)

probabilityAbyB=(probabilityA/probabilityB)*100


print(str(probability1) + '%')
print(str(probability2) + '%')
print(str(probabilityAbyB) + '%')


