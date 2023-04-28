from Node import Node
from linked_list import LinkedList

class timeline:

    def __init__(self) -> None:
        self.linkedList = None
        self.currentNode = None
        self.linkedList = LinkedList()
        self.currentNode = Node(None,None,None,None)
        self.index = 0
        return

    #json file load implementation required
    def loadTimeLine(self) -> None:
        self.linkedList = LinkedList()
        return

    #json file save implementation required
    def saveTimeLine(self) -> None:
        return

    def startTimeline(self) -> None:
        self.currentNode = self.linkedList.head
        self.index = 0
        return

    def nextEvent(self) -> None:
        self.currentNode = self.currentNode.next
        self.index += 1
        return

    def previousEvent(self) -> None:
        self.index -= 1
        return

    def goTo(self,index: int) -> None:
        if(self.index==index):
            return
        if(self.index<index):
            while(self.index<index):
                self.currentNode = self.currentNode.next
                self.index += 1
            return

        ''' need to implement previous functionality in linkedlist 
        if(self.index>index):
            while(self.index<index):
                return
        '''
        return


    def getTitle(self) -> str:
        print(self.currentNode.title)
        return self.currentNode.title

    def getSummary(self) -> str:
        print(self.currentNode.summary)
        return self.currentNode.summary

    def getDate(self) -> str:
        print(self.currentNode.date)
        return self.currentNode.date

    def getFacts(self) -> str:
        print(self.currentNode.facts)
        return

    def setTitle(self,title: str) -> None:
        self.currentNode.title = title
        return

    def setSummary(self, summary: str) -> None:
        self.currentNode.summary=summary
        return

    def setDate(self, date: str) -> None:
        self.currentNode.date=date
        return

    def setFacts(self,facts: str) -> None:
        self.currentNode.facts=facts
        return

    def addEvent(self, title: str, summary: str, date: str, facts: str) -> None:
        self.linkedList.addNewNode(title,date,summary,facts)
        return

    def deleteEvent(self) -> None:
        self.linkedList.delete(self.index)
        return


#Testing

TL = timeline()
TL.loadTimeLine()
TL.startTimeline()
TL.addEvent("t4","s4","d4","f4")
TL.linkedList.display()
TL.getTitle()
TL.goTo(2)
TL.getTitle()
