# 4. The Attention Filter

*Coding a Simple Program That Mimics Selective Attention*

**Field:** Neuroscience × Computer Science &nbsp;·&nbsp; **Project ID:** `computer-science/04-the-attention-filter`

```{admonition} Big Question
:class: tip
Can a simple program — one that filters a list of inputs based on a rule — model how the brain's attention works, letting some information through while ignoring the rest?
```

```{admonition} Why This Matters
:class: note
Selective attention (like the classic "cocktail party effect," noticing your name in a noisy room) is a foundational neuroscience concept, and it maps directly onto one of the most basic programming skills — filtering a list based on a condition — making it an excellent, concrete first project connecting code to cognition.
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Cherry, E. C. (1953). Some experiments on the recognition of speech, with one and with two ears. Journal of the Acoustical Society of America, 25(5), 975-979.

Cherry's classic "cocktail party" experiments played different messages into each ear and found that listeners could follow one conversation while filtering out the other — but importantly, certain especially salient information (like hearing their own name) in the unattended ear would sometimes break through the filter and get noticed anyway. This is the foundational study behind the entire "cocktail party effect" and the direct basis for the project's central hypothesis about noticing one's own name in a filtered stream.

### 2. Moray, N. (1959). Attention in dichotic listening: Affective cues and the influence of instructions. Quarterly Journal of Experimental Psychology, 11(1), 56-60.

Moray specifically confirmed that a person's own name is unusually likely to break through selective attention filtering compared to other equally unfamiliar words, even when someone is deliberately focused on a different message. This is the direct, specific evidence for the exact experimental design the project uses — comparing detection rates for one's own name versus a control word.

### 3. Wood, N., & Cowan, N. (1995). The cocktail party phenomenon revisited: How frequent are attention shifts to one's name in an irrelevant auditory channel? Journal of Experimental Psychology: Learning, Memory, and Cognition, 21(1), 255-260.

This later, more carefully controlled study found the name-detection effect is real but smaller and less universal than early demonstrations suggested — roughly a third of participants noticed their name in the unattended channel, not the near-universal effect sometimes implied by popular accounts. This is a useful, honest correction: the project's own results should be interpreted with realistic expectations about how often this effect actually occurs, not assumed to happen for every participant.

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design an "Attention Filter Simulator" — a simple program that takes a list of many words (representing "background noise") with one or two special target words mixed in, and filters the list to show only words matching a chosen rule (like the peer's own name). Innovation Proposal I documents the program's filtering rule and a sample run.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review:** plain-language summaries of selective attention research (the "cocktail party effect" and related findings), plus basic list-filtering programming concepts.
- [ ] **Hypothesis:** peers will notice and correctly identify a target word (like their own name) hidden in a fast-scrolling word list significantly more often than a random, non-personally-relevant control word, mirroring what the coded filter demonstrates logically.
- [ ] **Variables:** word type (personally relevant vs. control) as the thing being compared; correct-detection rate as the outcome.
- [ ] **Methodology:** show peers a fast-moving list of words with either their name or a control word hidden inside, and record whether they notice it, comparing rates across conditions.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] A short video, "I Coded the 'Hearing Your Name in a Noisy Room' Effect," using the same filter program and peer results; dissemination through school coding club and psychology/biology classes.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] Simulates the attention-filter program interactively, letting users set their own "target rule" and see it applied to a generated list, directly illustrating the filtering logic behind the Unit II experiment; documented on GitHub.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] Policy proposal recommending this project be used as a standard beginner list-filtering assignment in intro computer science classes, connecting directly to a genuinely interesting psychology finding, aimed at computer science curriculum coordinators.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Capstone integrates the filter simulator, the detection-rate study, the video, the interactive filter tool, and the curriculum proposal into one "attention filter" portfolio.

## Skills This Project Builds

- Writing list-filtering logic based on a defined rule.
- Designing and running a real psychology-style peer experiment.
- Explaining a famous psychological phenomenon through working code.
- Building an interactive filter demo with adjustable rules.
- Proposing a cross-disciplinary CS-psychology lesson to a curriculum committee.


## Why This Project Impresses

Uses one of the most basic programming operations (filtering a list) to model a famous, relatable psychological phenomenon, with a real peer experiment backing it up.

---

## How the Six Outputs Link Into One Portfolio

This project's six artifacts all point at the same moment: hearing your name in a noisy room. Unit I writes the first filtering program. Unit II turns it into a genuine peer experiment testing the real cocktail-party effect. Unit III explains that exact real result to an audience who's experienced it constantly without knowing its name. Unit IV turns the filtering logic into an interactive demo. Unit V asks CS classes to adopt this exact project as their list-filtering assignment. A CS mentor sees one of the most basic programming operations — filtering — used to recreate and test a genuinely famous psychology finding.

## Maximize Your Impact — What To Do With This After the Season

- Propose the project as a standard list-filtering assignment connecting CS and psychology in your curriculum.
- Submit the detection-rate study to a science fair under cognitive science or computer science.
- Share the interactive filter demo publicly as a teaching tool.

