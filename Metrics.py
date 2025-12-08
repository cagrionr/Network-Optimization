import math


def TotalDelay(nodes):
    #nodes listesi alır [node1,node2,node3,node4] gibi
    totalDelay = 0
    for i in range(len(nodes)-1):
        totalDelay += nodes[i].ProcessingDelay
        for j in range(len(nodes[i].links)):
            if nodes[i].links[j].DestinationNode == nodes[i+1].NodeID:
                totalDelay += nodes[i].links[nodes[i+1].NodeID].LinkDelay
    totalDelay += nodes[-1].ProcessingDelay

def TotalReliability(nodes):
    # nodes listesi alır [node1,node2,node3,node4] gibi
    totalReliability = 0
    linkReliability = 1
    nodeReliability = 1

    #link reliability hesapla
    for i in range(len(nodes)-1):
        for j in range(len(nodes[i].links)):
            if nodes[i].links[j].DestinationNode == nodes[i+1].NodeID:
                linkReliability *= nodes[i].links[nodes[i+1].NodeID].LinkReliability


    for i in range(len(nodes)):
        nodeReliability*= nodes[i].NodeReliability

    totalReliability =linkReliability * nodeReliability



def ReliabilityCost(nodes):
    reliabilityCost = 0
    for i in range(len(nodes) - 1):
        reliabilityCost += math.log(nodes[i].ProcessingDelay)
        for j in range(len(nodes[i].links)):
            if nodes[i].links[j].DestinationNode == nodes[i + 1].NodeID:
                reliabilityCost += math.log(nodes[i].links[nodes[i+1].NodeID].LinkDelay)
    reliabilityCost += nodes[-1].ProcessingDelay


def ResourcesCost(nodes):
    resourceCost = 0
    for i in range(len(nodes) - 1):
        for j in range(len(nodes[i].links)):
            if nodes[i].links[j].DestinationNode == nodes[i+1].NodeID:
                 resourceCost+= (1000/(nodes[i].links[nodes[i+1].NodeID].Bandwidth))