# README — How this project fits together

This file exists to answer one question: **when I call something, which
file's code actually runs?** That's the thing that trips people up most
when a project grows past one file.

## 1. The file map (who imports whom)

```
main.py
  ├── imports Book        from book.py
  ├── imports Member      from member.py
  ├── imports Librarian   from librarian.py
  └── imports Library     from library.py

member.py
  ├── imports Person      from person.py   (Member INHERITS from Person)
  └── imports Book        from book.py     (Member USES Book objects)

librarian.py
  ├── imports Person      from person.py   (Librarian INHERITS from Person)
  └── imports Book        from book.py     (Librarian USES Book objects)

library.py
  ├── imports Book        from book.py     (Library HOLDS Book objects)
  └── imports Member      from member.py   (Library HOLDS Member objects)

person.py    -> imports nothing (it's the base, everything else builds on it)
book.py      -> imports nothing (it's standalone)
```

Two different relationships are hiding in that list, and mixing them up is
usually the actual source of confusion:

- **"IS-A" (inheritance)** — `Member(Person)` means a Member *is a kind of*
  Person. This is why `member.py` imports `person.py`.
- **"HAS-A" (composition)** — `Library` *has* a list of Books and Members.
  This is why `library.py` imports `book.py` and `member.py`, even though
  Library doesn't inherit from either.

Same keyword pattern (`import X from x.py`), two very different meanings.
Always ask yourself: *is this an "is-a" or a "has-a"?*

## 2. Worked example: tracing `member1.introduce_yourself()`

This answers the question from earlier: when `main.py` calls
`member1.introduce_yourself()`, which file's code runs — `member.py`'s or
`person.py`'s?

**Answer: `member.py`'s version runs.** Here's the rule and the trace.

**The rule (Python's method lookup):** when you call `object.method()`,
Python looks for `method` starting in the object's *own* class first. Only
if it's *not* found there does Python walk up to the parent class and look
again. This walk-up-if-missing behavior is what makes polymorphism work.

**The trace, step by step:**

1. `member1` was created as a `Member`, not a `Person`. Its class is
   `Member`.
2. Python sees `member1.introduce_yourself()` and asks: "Does the `Member`
   class define `introduce_yourself`?"
3. Yes — `member.py` has its own `introduce_yourself()` that overrides the
   one in `Person`. Python stops looking and runs *that* version.
4. Control never even visits `person.py` for this particular call, even
   though `Member` inherits from `Person`.

**Now compare** — if `Member` did *not* define its own
`introduce_yourself()`, step 2 would come back empty, and Python would walk
up to `Person` and run *that* version instead. Same line of calling code
(`member1.introduce_yourself()`), two different possible outcomes,
depending purely on whether the subclass overrode the method. **That's
what "polymorphism" means in practice** — not a magic trick, just "check
the child first, fall back to the parent if the child is silent."

## 3. A mental model for reading any call, not just this one

Whenever you see `something.method_name()` anywhere in this project, ask
two questions in order:

1. **What class is `something` actually an object of?** (Not what type you
   *expect* — what it *literally was created as*, e.g. `Member`,
   `Librarian`, `Book`.)
2. **Does that exact class define `method_name`?** If yes, that's the code
   that runs. If no, walk up to its parent class and ask again.

That's the entire trick behind every "which file runs" question in this
codebase.

## 4. Small syntax pieces, named

A few shapes that show up repeatedly — broken into plain-English pieces
so a new one doesn't feel like a wall of symbols:

| Syntax | What it means, piece by piece |
|---|---|
| `class Member(Person):` | `class` = I'm defining a blueprint · `Member` = its name · `(Person)` = built on top of this other blueprint |
| `def __init__(self, name, age):` | `def` = defining a function · `__init__` = the special "setup" function that runs when an object is created · `self` = "the object being built" · the rest = data it needs |
| `super().__init__(name, age)` | `super()` = "reach up to my parent class" · `.__init__(...)` = "and run its setup function, so I don't have to repeat that code" |
| `@property` | "the method right below this acts like a plain attribute — you can read it without typing `()`" |
| `self._name` | `self` = this specific object · `_name` = a piece of data it owns (the leading `_` is a convention meaning "please don't touch this from outside") |

When a new syntax shape overwhelms you, come back to this table's format:
split it into pieces, name what each piece is doing, ignore the rest until
you need it.