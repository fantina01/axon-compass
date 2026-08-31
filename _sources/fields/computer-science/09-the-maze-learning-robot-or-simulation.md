# 9. The Maze-Learning Robot (or Simulation)

*Trial-and-Error Learning in Code vs. in the Brain*

**Field:** Neuroscience × Computer Science &nbsp;·&nbsp; **Project ID:** `computer-science/09-the-maze-learning-robot-or-simulation`

```{admonition} Big Question
:class: tip
Can a simple program that "learns" a maze through repeated trial and error (getting slightly better each time, without any advanced AI) illustrate the same basic trial-and-error learning process seen in real animal and human learning?
```

```{admonition} Why This Matters
:class: note
Classic learning experiments (like a rat learning a maze, getting faster over repeated trials) can be mirrored almost exactly by a very simple program that remembers which paths worked before and tries them again — connecting a foundational neuroscience/psychology experiment to basic programming concepts like memory (storing past results) and simple decision rules.
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Thorndike, E. L. (1898). Animal Intelligence: An Experimental Study of the Associative Processes in Animals. Macmillan.

Thorndike's classic experiments, placing cats in puzzle boxes they had to learn to escape, established the "Law of Effect" — behaviors followed by a satisfying outcome become more likely to be repeated, while behaviors followed by an unsatisfying outcome become less likely. This is the foundational, historical trial-and-error learning research the project's maze-learner program directly reimplements as a simple avoidance rule.

### 2. Tolman, E. C. (1948). Cognitive maps in rats and men. Psychological Review, 55(4), 189-208.

Tolman's research specifically used maze-learning in rats to argue that animals build something like an internal mental map of a maze's layout, rather than simply memorizing a fixed sequence of turns — a more sophisticated form of the trial-and-error learning process than Thorndike's original simple stimulus-response account. This is a useful, more nuanced companion source for a project wanting to discuss what kind of "memory" a maze-learning program might be simulating, beyond simple move avoidance.

### 3. Olton, D. S., & Samuelson, R. J. (1976). Remembrance of places passed: Spatial memory in rats. Journal of Experimental Psychology: Animal Behavior Processes, 2(2), 97-116.

Olton and Samuelson's radial-arm maze studies provided detailed, quantitative evidence of how efficiently rats learn to avoid previously-visited (and therefore already-emptied) paths in a maze — very similar in structure to the project's own avoidance-based learning rule. This gives the project's simplified program a genuine, well-matched real-animal-learning study to compare its own trial-by-trial improvement curve against.

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design a "Maze Learner" — either a simple simulated maze in code (a grid where a virtual character tries different paths, remembers dead ends, and improves over repeated attempts using only basic memory/decision rules, no advanced AI) or a simple physical maze-solving exercise with peers, paired for comparison. Innovation Proposal I documents the maze design and the simple learning rule used (like "avoid paths that were dead ends last time").

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review:** classic trial-and-error learning research (maze-learning studies), plus basic programming concepts for storing and using past results (simple memory/lists, conditional avoidance rules).
- [ ] **Hypothesis:** both the coded maze-learner and real peers solving a similar maze will show a decreasing number of wrong turns over repeated attempts, following a similar improvement pattern.
- [ ] **Variables:** attempt number as the thing being tracked; number of wrong turns (or time to solve) as the outcome, for both the program and real peer trials.
- [ ] **Methodology:** run the coded maze-learner for several attempts and record wrong-turn counts; separately, have peers attempt a similar real or on-paper maze repeatedly and record the same measure; compare the improvement patterns side by side.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] A short video, "I Coded a Program That Learns Like a Rat in a Maze," using the same maze learner and peer comparison; dissemination through school coding club and biology/psychology classes.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] Simulates the maze-learner interactively, letting users watch it attempt the maze repeatedly and see the wrong-turn count decrease, with the simple avoidance rule clearly displayed at each step; documented on GitHub with the logic explained in plain comments.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] Policy proposal recommending this project be used as a standard beginner assignment introducing the idea of a program that "remembers" past results to improve, connecting directly to real learning-science research, aimed at computer science curriculum coordinators.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Capstone integrates the maze learner, the improvement-pattern comparison study, the video, the interactive demo, and the curriculum proposal into one "maze-learning" portfolio.

## Skills This Project Builds

- Building a program that stores and uses past results to improve over time.
- Designing a direct comparison between a program's and real peers' learning curves.
- Explaining a classic psychology experiment through an original coded recreation.
- Building a step-by-step, fully visible interactive simulation.
- Proposing a foundational 'learning program' lesson to a CS curriculum.


## Why This Project Impresses

Connects a genuinely classic neuroscience/psychology experiment to basic programming concepts (memory, simple decision rules) without requiring any real machine learning — an elegant, appropriately-scoped analogy.

---

## How the Six Outputs Link Into One Portfolio

Every unit of this elegant project draws the same parallel more precisely: a simple program learning a maze, and a real animal doing the same thing. Unit I builds the first working maze-learner. Unit II compares its improvement pattern directly against real peer maze-solving data. Unit III explains that exact parallel to an audience who's heard "trial and error" without ever seeing it modeled in code. Unit IV makes the learning process fully visible, step by step. Unit V proposes this exact project as the standard introduction to programs that remember and improve. A CS mentor sees a classic psychology experiment recreated in code, with real, comparable human data alongside it.

## Maximize Your Impact — What To Do With This After the Season

- Propose the project as the standard introduction to programs that learn from past results in your CS curriculum.
- Submit the improvement-pattern comparison to a science fair under computer science or comparative psychology.
- Share the interactive maze-learner demo publicly as a teaching resource.

