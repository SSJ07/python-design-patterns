## Clean Architecture Design

- SOLID principles -> It tell us how to arrange bricks(code) into walls(classes, interfaces) and rooms(modules) of the buildings(applications)
- Component principles -> It tell us how to arrange rooms(classes, interfaces, modules) in the buildings(applications)


- **SOLID** principle
  - Tell us how to arrange functions and data structures into classes
  - It simply applies for grouping functions and data
  - It tells us how to arrange bricks in wall and room of the building
- S --> **The Single responsibility principle**
  - This principle states that a class should do one thing, and therefore it should 
    have only a single reason to change
  - For example:  Let's take most common example of Employee class
  ```
    |==============|
    |Employee      | <--- Employee class violates the SRP princeple. It has three reasons to modify this class
    |==============|
    |+ cal_pay     | <--- Reason 1. It's accountant reponsiblity. Can create class PayCalculator which calcuates payment
    |+ report_hours| <--- Reason 2. It's HR department responsibility. Can create class like TimeReporter which report hours detail 
    |+ save        | <--- Reason 3. It's DBA responsibilty. Can create class like EmployeeDB which store emp details
    |==============|
  
    --> Solution: Create separate classes for each responsibilty and that's SRP
  ```
  - Another example could be: `Book class, Invoice class, PrintInvoice class` <-- each class has single reason(responsibility) to change it
- O --> **The Open-closed principle**
  - This principle states that classes should be open for extensions and closed to modification
  - Open for extension means can add new functionality
  - Closed to modifications means can't modify existing structure
  - We achieve this principle by using interfaces and abstract classes 
- L --> **The Liskov substitution principle**
  - this principle states that subclasses should be substitutable for their base classes
  - e.g: Base class A has child class B and object of B class can be passed to any methods that expects object of A
- I --> **The interface segregation principle**
  - Segregation means keeping things separated
  - This principle is about keeping interfaces separated
  - It states that many client specific interfaces are better than one general purpose interface
- D --> **The Dependency inversion principle**
  - This principle states that our classes should depend on interfaces and abstract classes instead of concrete classes
  - It tells to refer abstraction/interfaces instead of concreate classes.
  - Interfaces are less volatile(rarely change) but concrete classes(implementation) are volatile and can be frequently changed
  - If it's about using abstract classes then what about concrete classes like str, list??
  - Well, these concreate classes are very stable and rarely modifies, we don't need to worry about it
  - We would use an `Abstract Factory` to manage this undesirable dependency
  - Abstract component --> high level business rules of application
  - Concreate component--> Implementation details that those business rules manipulate

- **Component Principles**
  - Component is the smallest part or entity of system
  - **Component cohesion**:
    - REP: The Reuse/Release Equivalence Principle
    - CCP: The Common Closure Principle(Same as SRP principle)
      - Gather together those things that change at same times and for the same reasons
      - Separate those things that change at different times or for the different reasons
    - CRP: The Common Reuse Principle
      - Don't force users of a component to depend on things which they don't need.
      - It tells us that which classes _shouldn't be together_ than about which classes should be together
      - It describes dependency rules. Classes should not be tightly coupled in different component
      - _Don't depend on things you don't need_
  - **Component coupling**:
    - It describes the relationship between components
    - The Acyclic Dependencies Principle(ADP):
      - Allows no cycles in component dependency graph