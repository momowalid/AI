# ai-companies-
### 1.Arab Cloud Computing
### 2.BeitBatt
### 3.EgyptLabs
### 4.Betakod *
### 5.El-Masry for Artificial Intelligence *
### 6.Robusta *
### 7.Innoventures
### 8.Vortechs
### 9.Nahdit misr for AI
### 10.WideBot
### 11.Botme
### 12.Vortechs *
### 13.Nasser EL Din Intelligent *
##### Companies that marked with '*' they are companies that develop smart solutions using AI for health care field
### ***************************************************************************************************************
# Clean Code Principles 
## 1.SOLID: This acronym stands for Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle. These principles help to ensure that code is modular, reusable, and easy to maintain.

## 2.Keep it simple, stupid (KISS): This principle emphasizes the importance of simplicity in code. Complex code can be difficult to understand and maintain, so it's important to keep things as simple as possible.

## 3.Don't repeat yourself (DRY): This principle encourages developers to avoid duplicating code. Repeating code can lead to errors and make the code more difficult to maintain.

## 4.Separation of concerns (SoC): This principle encourages developers to separate different parts of the code into separate modules or classes, each responsible for a single concern.

## 5.Single responsibility principle (SRP): This principle states that each module or class should have a single responsibility or reason to change. This helps to ensure that code is modular and easy to maintain.

## 6.Open/closed principle (OCP): This principle states that modules or classes should be open for extension but closed for modification. This means that new functionality can be added without changing existing code.

## 7.Liskov substitution principle (LSP): This principle states that subclasses should be substitutable for their superclass. This helps to ensure that code is flexible and can be easily extended.

## 8.Interface segregation principle (ISP): This principle states that clients should not be forced to depend on interfaces they do not use. This helps to ensure that code is modular and easy to maintain.

## 9.Dependency inversion principle (DIP): This principle states that high-level modules should not depend on low-level modules, but instead both should depend on abstractions. This helps to ensure that code is flexible and easy to maintain.

## 10.Law of Demeter (LoD): This principle states that modules or classes should only communicate with their immediate neighbors. This helps to ensure that code is modular and easy to maintain.

## 11.Composition over inheritance: This principle states that code should favor composition over inheritance, as composition is more flexible and easier to maintain.

## 12.Minimize coupling: This principle encourages developers to minimize the dependencies between modules or classes. This helps to ensure that code is modular and easy to maintain.

## 13.Maximize cohesion: This principle encourages developers to maximize the coherence within modules or classes. This helps to ensure that code is modular and easy to maintain.
## *************************************************************************************************************************
# the implementation of the graph in python 
## In Python, there are several ways to implement a graph data structure. One common approach is to use a dictionary to represent the graph, where the keys of the dictionary are the nodes and the values are lists of the nodes that they are connected to. Here is an example implementation of an undirected graph using a dictionary:
### class Graph:
###    def __init__(self):
###        self.graph = {}

###    def add_edge(self, u, v):
###        if u not in self.graph:
###            self.graph[u] = []
###        if v not in self.graph:
###            self.graph[v] = []
###        self.graph[u].append(v)
###        self.graph[v].append(u)
## In this implementation, add_edge takes two nodes u and v and adds an undirected edge between them. If either u or v is not already in the graph dictionary, it is added as a key with an empty list as its value. Then, the method appends v to the list of u's connections, and vice versa.

## To use this implementation, you can create a Graph object and add edges to it like this:

### g = Graph()
### g.add_edge(1, 2)
### g.add_edge(2, 3)
### g.add_edge(3, 4)

## This creates a graph with nodes 1, 2, 3, and 4, and edges between 1 and 2, 2 and 3, and 3 and 4. You can then access the connections of a node by looking it up in the graph dictionary:
### print(g.graph[2])  // prints [1, 3]

