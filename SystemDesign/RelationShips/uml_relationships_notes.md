# UML Relationships — Complete Notes

Six relationship types in UML, from weakest to strongest coupling:

```
Dependency → Association → Aggregation → Composition → Realization → Inheritance
```

- **Dependency, Association, Aggregation, Composition** → relationships between **objects** (who holds/uses whom)
- **Inheritance, Realization** → relationships between **classes/types** (what something *is* or *promises to be*)

---

## 1. Dependency

**Definition:** The weakest relationship. One class *uses* another temporarily — usually just within a single method — without storing any reference to it.

- **UML notation:** Dashed arrow (`- - ->`), pointing from dependent class to the class it depends on
- **Relationship:** "uses"
- **Lifecycle:** Object created/obtained locally, used once, discarded

```python
class Printer:
    def print_document(self, text):
        print(f"Printing: {text}")


class Report:
    def generate(self):
        content = "Annual Report 2026"
        printer = Printer()               # created LOCALLY, only exists here
        printer.print_document(content)   # used once, then discarded
        # after generate() finishes, Report has no memory Printer existed


r = Report()
r.generate()
```

**Key signal:** Object is created *inside* a method (or passed in and used once) — never stored as `self.something`.

---

## 2. Association

**Definition:** A general relationship where two classes interact — one uses another, typically passed in from outside — but neither owns the other, and no persistent reference is kept.

- **UML notation:** Plain solid line
- **Relationship:** "uses / interacts with"
- **Lifecycle:** Fully independent; relationship exists only during interaction

```python
class Student:
    def __init__(self, name):
        self.name = name


class Teacher:
    def __init__(self, name):
        self.name = name
        # NOTE: no self.students list — Teacher doesn't "have" students

    def teach(self, student):             # student is external, used once
        print(f"{self.name} is teaching {student.name}")


t = Teacher("Mr. Sharma")
s = Student("Sameer")
t.teach(s)
# after this line, 't' has ZERO trace of 's' anywhere in its state
```

**Key signal:** Object passed as a parameter, used meaningfully, but not stored as an attribute.

---

## 3. Aggregation

**Definition:** A special "has-a" (whole-part) relationship. One class holds a reference to another as an attribute, but the "part" existed before and survives independently after the "whole" is destroyed.

- **UML notation:** Solid line with a **hollow diamond** on the "whole" side
- **Relationship:** "has-a" (weak ownership)
- **Lifecycle:** Part is independent of whole

```python
class Professor:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, dept_name, professors):
        self.dept_name = dept_name
        self.professors = professors      # stored, but NOT created here


# Professors exist independently first
p1 = Professor("Dr. Rao")
p2 = Professor("Dr. Iyer")

cse = Department("CSE", [p1, p2])

# Delete the department — professors are untouched
del cse
print(p1.name, p2.name)   # still accessible, still valid objects
```

**Key signal:** Object is stored as `self.x`, but it was created *outside* and passed in — its life doesn't depend on the container.

---

## 4. Composition

**Definition:** The strong form of aggregation. One class creates and owns another internally — the "part" cannot exist without the "whole" and is destroyed along with it.

- **UML notation:** Solid line with a **filled (solid) diamond** on the "whole" side
- **Relationship:** "has-a" (strong ownership)
- **Lifecycle:** Part dies with the whole

```python
class Engine:
    def __init__(self):
        print("Engine built")


class Car:
    def __init__(self):
        self.engine = Engine()    # created INTERNALLY, tied to Car's lifecycle


car = Car()
del car
# The Engine object created here has no external reference and is
# garbage collected along with Car — it was never independently usable
```

**Key signal:** Object is both created *and* stored inside the container's own constructor — no external reference ever exists.

---

## 5. Realization

**Definition:** The relationship between an interface (or abstract class) and a class that implements it. It represents fulfilling a contract, not inheriting actual behavior or state.

- **UML notation:** **Dashed line** with a **hollow triangle** arrowhead
- **Relationship:** "implements"
- **Mechanism in Python:** Abstract Base Classes (`ABC`)

```python
from abc import ABC, abstractmethod

class Flyable(ABC):              # this is the "interface"
    @abstractmethod
    def fly(self):
        pass                      # no implementation — just a contract


class Bird(Flyable):              # Bird REALIZES Flyable
    def fly(self):
        print("Bird flaps wings and flies")


class Airplane(Flyable):          # Airplane REALIZES Flyable too
    def fly(self):
        print("Airplane uses jet engines to fly")


b = Bird()
a = Airplane()
b.fly()
a.fly()
# Bird and Airplane share no inheritance relationship with each other,
# but both PROMISE to provide a fly() method
```

**Key signal:** Class subclasses an `ABC` and implements its `@abstractmethod`(s); unrelated classes can realize the same interface.

---

## 6. Inheritance (Generalization)

**Definition:** An "is-a" relationship — a subclass is a specialized version of a superclass. It inherits attributes and behavior, and can override or extend them.

- **UML notation:** Solid line with a **hollow triangle** arrowhead, pointing from child → parent
- **Relationship:** "is-a"
- **Mechanism in Python:** Regular subclassing

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):                # Dog IS-A Animal
    def make_sound(self):         # overrides parent behavior
        print(f"{self.name} barks")


class Cat(Animal):                # Cat IS-A Animal
    def make_sound(self):
        print(f"{self.name} meows")


d = Dog("Tommy")
c = Cat("Whiskers")
d.make_sound()   # Tommy barks
c.make_sound()   # Whiskers meows

print(isinstance(d, Animal))   # True — a Dog literally IS an Animal
```

**Key signal:** `class Child(Parent)` — child automatically gets everything the parent has, plus its own additions/overrides.

---

## Summary Table

| Relationship | UML Notation | Relationship Type | Object Stored? | Who Creates It | Lifecycle Dependency |
|---|---|---|---|---|---|
| Dependency | Dashed arrow | "uses" | No | Created locally inside method | None — momentary |
| Association | Solid line | "uses / interacts" | No | Passed in from outside | Independent |
| Aggregation | Solid line + hollow diamond | "has-a" (weak) | Yes (`self.x`) | Created outside, passed in | Part survives whole |
| Composition | Solid line + filled diamond | "has-a" (strong) | Yes (`self.x`) | Created inside constructor | Part dies with whole |
| Realization | Dashed line + hollow triangle | "implements" | N/A (class-level) | N/A | Contract only, no shared code |
| Inheritance | Solid line + hollow triangle | "is-a" | N/A (class-level) | N/A | Full structural inheritance |

## Quick Mental Model

- **Dependency** → "I borrow you for a moment, inside one method, then forget you."
- **Association** → "I interact with you, you're passed to me from outside, but I don't keep you."
- **Aggregation** → "I hold onto you (`self.x`), but you existed before me and survive after me."
- **Composition** → "I create you, I hold you, and you die when I die."
- **Realization** → "I promise to provide this behavior, as defined by a contract."
- **Inheritance** → "I am a specialized type of you."

**The three questions that decide object-level relationships (dependency/association/aggregation/composition):**
1. Who creates the object?
2. Is it stored as `self.something`?
3. Whose lifecycle controls whose?
