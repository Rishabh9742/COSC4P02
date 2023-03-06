class Node:
    def __init__(self, title: str, date: str, summary: str, facts: str) -> None:
        self.title = title
        self.date = date
        self.summary = summary
        self.facts = facts
        self.next = None

    def deleteSummary(self):
        self.summary = ""
        
    def addSummary(self, new_summary: str):
        self.summary += " " + new_summary
        
    def addFacts(self, new_facts: str):
        self.facts += " " + new_facts
        
    def deletefacts(self):
        self.facts = ""

    def deleteTitle(self):
        self.title = ""

    def displayInfo(self):
        print("-"*50)
        print("Title: ", self.title)
        print("Date: ", self.date)
        print("Summary: ", self.summary)
        print("Facts: ", self.facts)