def find_prob(event,samplespace):
    probability=(event/samplespace)*100
    return round(probability,1)

cards=52
king=4

kingprobability=find_prob(king,cards)

cards=51
ace=4

aceprobability=find_prob(ace,cards)

print(str(aceprobability) + '%')
print(str(kingprobability) + '%')
print(str(aceprobability*kingprobability) + '%')

