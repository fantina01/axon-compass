# 2. If-Then Brains

*Modeling Simple Decision-Making with Conditional Logic*

**Field:** Neuroscience × Computer Science &nbsp;·&nbsp; **Project ID:** `computer-science/02-if-then-brains`

```{admonition} Big Question
:class: tip
Can basic if-then (conditional) programming logic — the very first thing most students learn in coding — model how the brain makes simple, fast decisions under different conditions?
```

```{admonition} Why This Matters
:class: note
A huge amount of everyday decision-making follows simple if-then patterns (if tired, then more likely to snack; if stressed, then more likely to procrastinate), and building this as literal code makes an abstract psychological idea into something concrete, testable, and buildable by a true beginner programmer.
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Baumeister, R. F., Bratslavsky, E., Muraven, M., & Tice, D. M. (1998). Ego depletion: Is the active self a limited resource? Journal of Personality and Social Psychology, 74(5), 1252-1265.

This influential (though later contested) study proposed that self-control draws on a limited resource that becomes depleted with use, meaning fatigue or stress could make impulsive decisions more likely later in the day — a plausible mechanism behind the project's if-then rules linking conditions like fatigue to decisions like snacking. Note: subsequent large replication attempts have found much weaker or inconsistent ego-depletion effects than the original studies suggested, so the project should present this as a debated, not fully settled, mechanism.

### 2. Hagger, M. S., Wood, C., Stiff, C., & Chatzisarantis, N. L. D. (2010). Ego depletion and the strength model of self-control: A meta-analysis. Psychological Bulletin, 136(4), 495-525.

This meta-analysis found a real, if modest, average ego-depletion effect across many studies existing at the time — but the field's confidence in the effect size has weakened considerably since, following larger, more rigorous replication attempts (like a major 2016 multi-lab registered replication that found little to no effect). This paper is useful precisely for teaching the project's core lesson responsibly: cite the original theory, but be honest that later, larger studies complicate the simple story.

### 3. Danziger, S., Levav, J., & Avnaim-Pesso, L. (2011). Extraneous factors in judicial decisions. Proceedings of the National Academy of Sciences, 108(17), 6889-6892.

This widely-cited study found that judges' parole decisions became notably less favorable as time passed since their last food break, then improved again right after a break — offered as real-world evidence that simple physiological conditions (like hunger or fatigue) can measurably shift consequential decisions. (This finding has also faced methodological critique since publication, so it should be presented as a striking, real, but debated example rather than an uncontested fact.)

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design a "Decision Pattern Tracker and Simulator" — peers log simple daily conditions (sleep, stress level, hunger) and a related decision (snack choice, screen time), and students build a simple if-then program predicting the decision based on the conditions. Innovation Proposal I documents the tracking method and an initial, simple set of if-then rules.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review:** plain-language summaries of how simple contextual conditions (fatigue, stress) shift everyday decisions, plus basic conditional-logic programming concepts.
- [ ] **Hypothesis:** an if-then program built from real peer data will correctly predict peers' logged decisions more often than random guessing.
- [ ] **Variables:** logged conditions (sleep, stress, hunger) as the input; the actual decision made as the outcome to predict.
- [ ] **Methodology:** collect a real dataset from peer logs, build simple if-then rules based on patterns in the data, then test the rules against new data points not used to build them.
- [ ] **Investigation blueprint:** the full data-collection method, the rule-building process, and the accuracy-testing method, all clearly documented.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] A short video, "I Coded a Program That Predicts My Bad Decisions," using the same tracker and program; dissemination through school coding club and health/wellness classes.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] Simulates the if-then decision program interactively, letting users enter their own conditions (sleep, stress, hunger) and see a predicted decision, along with the confidence based on how often that rule held true in the real data; documented on GitHub with the logic explained in plain comments.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] Policy proposal recommending this project be used as a standard beginner conditional-logic assignment in intro computer science classes, since it connects code directly to a personally relevant behavioral question, aimed at computer science curriculum coordinators.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Capstone integrates the tracker, the prediction-accuracy study, the video, the interactive predictor, and the curriculum proposal into one "if-then brains" portfolio.

## Skills This Project Builds

- Writing conditional (if-then) logic rules from real collected data.
- Validating a model against new data it wasn't built from (out-of-sample testing).
- Explaining basic predictive-modeling concepts to a general audience.
- Building an interactive predictor tool with clear, documented logic.
- Proposing a real-data programming assignment to a CS curriculum.


## Why This Project Impresses

Uses the most basic programming concept (if-then logic) to build something genuinely predictive from real, personally-collected data — simple tool, real result.

---

## How the Six Outputs Link Into One Portfolio

This project's throughline is a single idea — everyday decisions follow patterns a computer can learn — proven more rigorously at each stage. Unit I builds the first simple prediction rules from real peer data. Unit II tests those rules against new data the rules weren't built from, real out-of-sample validation. Unit III explains that finding to an audience who's never thought of their own snacking as a predictable if-then pattern. Unit IV turns the rules into an interactive predictor anyone can try. Unit V asks CS classes to adopt this exact real-data project as their conditional-logic assignment. A CS or data-science mentor sees genuine predictive-modeling thinking — training on some data, testing on new data — executed at a beginner level but with real rigor.

## Maximize Your Impact — What To Do With This After the Season

- Share the prediction-accuracy findings and tool with your school's health or wellness program as a self-reflection resource.
- Submit the project to a science fair under data science or behavioral science.
- Propose the project as a real-data conditional-logic assignment to your CS teacher.

