import random

class Node:

    def __init__(self,NodeID,minProcessingDelay=0.5,maxProcessingDelay=2,minNodeReliability=0.95,maxNodeReliability=0.999):
        self.NodeId=NodeID
        self.ProcessingDelay = random.uniform(minProcessingDelay,maxProcessingDelay)#ms
        self.NodeReliability = random.uniform(minNodeReliability,maxNodeReliability)#%
        self.links=[]

    def addLink(self,DestinationNodeID):
        flag=False
        if self.NodeId==DestinationNodeID:
            return
        for i in range(len(self.links)):
            if DestinationNodeID==self.links[i].DestinationNode:
                flag=True
                break

        if flag==False:
            new_link = Link(DestinationNodeID)
            self.links.append(new_link)



        """for i in range(len(self.links)):
            print(self.links[i].DestinationNode)"""





class Link:
    #her bir node sahip olduğu bağlantı kadar link tutar. her bir link o node'dan hangi node'a bağlanıldığını destination node ile gösterir.
    def __init__(self,DestinationNode,minBandwidth=100,maxBandwidth=1000,minLinkDelay=3,maxLinkDelay=15,minLinkReliability=0.95,maxLinkReliability=0.999):
        self.DestinationNode=DestinationNode
        self.Bandwidth=random.uniform(minBandwidth,maxBandwidth)#mbps
        self.LinkDelay=random.uniform(minLinkDelay,maxLinkDelay)#ms
        self.LinkReliability=random.uniform(minLinkReliability,maxLinkReliability)#%
