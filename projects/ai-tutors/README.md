# Python Tutor Prompts

Chat prompts that teach and review Python. No platform, plugins, or accounts required — they're plain markdown, and they work pasted into any capable chat. Python itself runs on your machine; a terminal is preferred where a tutor asks for one, and each tutor says exactly what it needs from you.

## The Tutors

- **`socratic-python-tutor.md`** — teaches by questioning. Won't hand over answers you can reach yourself; hints and exercises arrive one rung at a time. Best when you want to be pushed.
- **`peer-code-reviewer.md`** — a senior student reviewing your code: blunt, severity-ranked findings, honest verdicts, study directives. Best when you want to know what's wrong.
- **`exploratory-programming-tutor.md`** — investigates alongside you. Direct explanations, tangents, experiments, labelled speculation. Best when you want to understand why.

## Checkpoints

The tutors don't remember you between sessions — every chat starts from zero. The **checkpoint is your save file**, and it's portable across all of them.

**Getting one:**
- Ask any time, mid-session: *"give me a checkpoint."*
- They're also emitted automatically at session end, on topic changes, and when a piece of work completes.

It's a plain-text block that looks like this (fields vary by tutor):

```
CHECKPOINT — 2024-06-01
TOOLKIT:      variables, conditionals, loops, functions
COVERED:      dictionaries, file reading
DEMONSTRATED: wrote a file parser unaided
SHAKY:        nested loops
...
```

**Using it:**
1. Copy the whole block before you close the chat — it's the only thing that carries over.
2. Paste it as your first message next session. If you're running the tutor as a saved assistant/GPT, that's all it takes; if you're pasting the tutor prompt into a fresh chat, paste the tutor first, then the checkpoint.
3. The tutor loads it instead of asking intake questions and confirms the toolkit is still accurate.

The `TOOLKIT` line is the shared currency — what you can use unaided — and every tutor reads it, so a checkpoint from any of them works in any other. The remaining fields differ by tutor (the reviewer's carries a study queue; the tutors' carry misconceptions and project state), and whatever the receiving tutor is missing, it simply asks for — usually just what you want to do today.

**Example workflow:** build a piece with the exploratory tutor, take a checkpoint, then paste it to the peer reviewer along with your code — it already knows what you're supposed to know, and the review starts at the right level.
