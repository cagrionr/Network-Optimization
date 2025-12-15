import random
import numpy as np

import Metrics
from Metrics import TotalDelay,ReliabilityCost,ResourceCost


def fitnessFunction(Nodes, weightDelay, weightReliability, weightResource, pathIDs, sourceID, destinationID):
    #3 METRİK için ağırlıklar verilir
    #pathIDs yoldaki node'ların id'lerini tutar örneğin [1 numaralı node, 8 numaralı node, 95 numaralı node, 3 numaralı node]

    if pathIDs[0]!=sourceID or pathIDs[-1]!=destinationID:
        return float("inf")
        #başlangıç ve//veya bitiş id'ler farklı ise yol kesinlikle yanlıştır fitness değeri 0 ver.
    else:
        fitnessScore = 0
        pathNodes=[Nodes[i] for i in pathIDs]
        totalDelay=weightDelay*Metrics.TotalDelay(pathNodes)
        reliabilityCost=weightReliability*Metrics.ReliabilityCost(pathNodes)
        resourceCost=weightResource*Metrics.ResourceCost(pathNodes)

        fitnessScore=totalDelay+reliabilityCost+resourceCost


        return fitnessScore


def createİnitialPopulation(length,lowerBound, upperBound):
    #returns a list of node ids
    if length<=1:
        raise ValueError("Popülasyon büyüklüğü 1'den büyük olmalı.")

    population = []
    for i in range(length):
        population.append(random.randint(lowerBound, upperBound))
    return population


def crossover(crossOverChance, parent1, parent2):
    #parent1 and parent2 as a list of node ids in the path(possible solution)

    #BU KOD ÇALIŞMAZMIŞ ÇOCUKLARDA PATH SÜREKLİ KOPUK OLURMUŞ(İLLA Kİ BAĞLI OLAN YOL ÇIKAR AMA HERALDE ÇOK HESAPLAMA YÜKÜ OLUR)

    """parent'ların 1er tane genom'unu rastgele al. birbirleriyle değiştir."""
    lengthofParent1 = len(parent1)
    lengthofParent2 = len(parent2)

    count=int(crossOverChance*min(lengthofParent1, lengthofParent2))

    for i in range(count):
        changed=set()
        idxgenom1=random.randint(0,lengthofParent1-1)
        idxgenom2=random.randint(0,lengthofParent2-1)
        changed.add(idxgenom1)
        changed.add(idxgenom2)
        child1=parent1
        child2=parent2

        if (idxgenom1 in changed) or (idxgenom2 in changed):
            temp=parent1[idxgenom1]
            child1[idxgenom1]=parent2[idxgenom2]
            child2[idxgenom2]=temp
    return child1, child2

def crossoverOneJoint(crossoverChance, parent1, parent2):
    if (random.random>crossoverChance):
        return
        #x ihtimalle cross over yap/yapma

    point=random.randint(0,min(len(parent1),len(parent2))-1)
    child1=parent1.copy()
    child2=parent2.copy()


    i=point
    while i<min(len(parent1),len(parent2)):
        child1[i]=parent2[i]
        i+=1

    i = point
    while i < min(len(parent1), len(parent2)):
        child2[i] = parent1[i]
        i += 1


    return child1, child2


def mutation(individual, changeMutation, lowerBound, upperBound):
    child=individual.copy()
    if random.random()<changeMutation:

    return child









