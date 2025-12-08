import time
from NodeClass import *
def CreateNetwork(NumOfNodes,ProbabilityOfLinks):
    Nodes=[]
    for i in range(NumOfNodes):
        Nodes.append(Node(i))

    for i in range(NumOfNodes):
        for j in range(i+1,NumOfNodes):

            if i!=j and random.uniform(0.0,1.0)<ProbabilityOfLinks:
                Nodes[i].addLink(j) #i indeskli  node'a link eklenir. destination nodeID=j
                Nodes[j].addLink(i)#tam tersi



    return Nodes

def test(NumOfNodes,ProbabilityOfLinks):
    print("test başlatırlıyor")
    start=time.time()
    network=CreateNetwork(NumOfNodes,ProbabilityOfLinks)
    totalNodes=len(network)
    totalLinks=0

    for node in network:
        totalLinks+=len(node.links)

    AvgLinksPerNode=totalLinks/totalNodes
    print(f"Toplam Node sayısı:{totalNodes}")
    print(f"Toplam Link sayısı:{totalLinks}")
    print(f"Ortalama link sayısı:{AvgLinksPerNode}")
    end=time.time()
    print(f"Geçen süre:{end-start}")