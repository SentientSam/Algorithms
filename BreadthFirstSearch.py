# Author : Samuel Lamb
# Date last worked on : 11/24/2020
# Purpose : Reference example of breadth-first search
# Finds a person named tim in your "contacts"



from collections import deque

graph = {}
graph["you"] = ["elizabeth","bob","wallace"]
graph["bob"] = ["jimmy","jane"]
graph["elizabeth"] = ["peggy"]
graph["jimmy"] = ["susan","jim"]
graph["susan"] = []
graph["wallace"] = ["stephen","annie","trevor"]
graph["stephen"] = ["tim","stephanie"]
graph["peggy"] = []
# graph["bob"] = []
graph["jane"] = []
graph["jim"] = []
graph["stephen"] = []
graph["annie"] = []
graph["trevor"] = []
graph["tim"] = []
graph["stephanie"] = []
# graph["sam"] = []

def person_is_tim(name):
  # print (name[-1])
  return name == "tim"
  # return True


def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_tim(person):
        print (person + " is a seller!")
        # print ("Found!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
        # print(searched)
  return False

search("you")