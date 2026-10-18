# Python Academy

A self-hosted Python tutor for an AI assistant: four mentors with different teaching methods, a set of rules they all follow, and three small files that act as the tutor's memory between sessions.

It's built for people learning Python on their own or alongside a course, who want to actually get better at reasoning, debugging and building, not just collect working code.

## What makes it different

- **It won't write your work for you.** The mentors explain, question, review and demonstrate on different examples, but your projects, exercises and graded coursework stay yours.
- **You run the code.** You run everything in your own editor or terminal and paste the output. The mentors never pretend to have run something, and a real run always beats their reading of the code.
- **Evidence, not vibes.** Every claim about what you can do is labelled: *observed* (you ran it and pasted the output), *tested* (you did it unaided in a test), *reported* (you said so), or *read* (a mentor's guess from reading code). Strengths need real evidence.
- **It remembers.** Your toolkit, your struggles and a session log are kept in files that every mentor reads at the start of each session.
- **Gaps, not restrictions.** Mentors can show you anything in Python, but anything you haven't learned yet is flagged and logged, with where to study it.

## The mentors

| Mentor | Call it for |
|---|---|
| **Socratic** | Learning a new concept, or getting unstuck on an exercise without being handed the answer |
| **Exploratory** | "Why does this work?", direct explanations, experiments, tangents |
| **Senior** | Honest, ranked review of code you wrote |
| **Tester** | A short test with a scorecard and model solutions |

## Files

| File | What it is | Where it goes |
|---|---|---|
| `project-instructions.md` | The rules every session follows | The project's **instructions** field |
| `tutor-socratic-python.md` | Socratic mentor | Project files |
| `tutor-exploratory-python.md` | Exploratory mentor | Project files |
| `tutor-senior-code-reviewer.md` | Senior reviewer | Project files |
| `tutor-tester.md` | Tester | Project files |
| `current-toolkit.md` | Your setup, sources and what you know (template) | Project files |
| `current-struggles.md` | Your struggles, strengths and pending items (template) | Project files |
| `session-log.md` | History of your sessions (template) | Project files |

`README.md` and `LICENSE` don't need uploading.

## Setup

You need an AI assistant that supports **projects**: a persistent instructions field plus uploaded files that every chat in the project can read. Claude Projects works; similar features in other assistants should too.

1. Create a new project.
2. Paste the contents of `project-instructions.md` into the project's instructions field.
3. Upload the other seven `.md` files as project files.
4. Open a new chat in the project and say hello.

## Your first session: intake

Because the templates are blank, the first session is a short **intake** interview: your background, what you've learned so far and from where, your setup, your goals, and whether you're on a graded course. You'll be offered a short placement test (about six items) to turn what you told it into real evidence. Taking it is optional.

At the end you get filled-in versions of the files to upload in place of the templates.

## Everyday use

- **Pick a mentor** by name: `Socratic: I'm stuck on this loop exercise`, `@Senior review this`, `Tester, test me on dictionaries`. Or just say what you want and it will suggest one.
- **Switch** at any time: `handoff to Exploratory`.
- **Paste code in a fenced block** so the indentation survives:
  ````
  ```python
  your code here
  ```
  ````
- **Predict before you run.** The mentors will ask what you expect a program to do before you run it. A wrong prediction is useful: it shows exactly where your mental model differs from Python's.
- **Say "close"** when you're done.

## After every session

When you close, the mentor gives you:

1. a **session-close block** summarising what you covered, what you showed, new struggles, strengths and gaps, and what's next;
2. short feedback from the other three mentors;
3. updated **`current-toolkit.md`** and/or **`current-struggles.md`** as complete files;
4. a **new entry** for `session-log.md`.

Then:

1. Replace the changed files in your project with the new versions.
2. Paste the new log entry at the top of `session-log.md` (below the Condensed history section) and re-upload it.
3. Start your next session in a new chat.

If your assistant can edit project files directly, it will do this for you and tell you what changed.

## The rules in short

Your work comes in three tiers:

- **Assessed work** (graded coursework, exams): explanation and hints only.
- **Own work** (your projects, book and course exercises): no mentor writes it, not even a skeleton or a fix. They point at lines, explain problems, and demonstrate on different examples.
- **Practice code** (written by a mentor to teach): fair game, including model solutions to the Tester's own exercises.

Struggles are retired only with evidence from a Tester session plus one other session, and only when you confirm it.

## Customising

Everything is plain Markdown. You can change a mentor's voice, add a mentor (add a row to the table in `project-instructions.md` and a file), or change the marking scheme in `tutor-tester.md`. Keep the floor and the evidence labels if you want the system to stay honest.

The kit is Python-specific for now; the mechanics would work for other languages with the Python details swapped out.

## License

MIT. See `LICENSE`.
