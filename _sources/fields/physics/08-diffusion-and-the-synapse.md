# 8. Diffusion and the Synapse

*Fick's Law and Neurotransmitter Release Timing*

**Field:** Neuroscience × Physics &nbsp;·&nbsp; **Project ID:** `physics/08-diffusion-and-the-synapse`

```{admonition} Big Question
:class: tip
Can basic diffusion physics (Fick's Law, concentration gradients) explain the timing of how quickly neurotransmitter molecules cross the synaptic gap?
```

```{admonition} Why This Matters
:class: note
Synaptic transmission is often taught as an instantaneous "signal crossing," but it is physically a diffusion process governed by the same concentration-gradient principles taught in intro chemistry/physics — modeling this explicitly gives a rigorous, calculable answer to "how fast is a synapse, really?"
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Fick, A. (1855). Uber Diffusion. Annalen der Physik, 170(1), 59-86.

Adolf Fick's original paper established the mathematical laws of diffusion — describing how the rate of molecular movement across a concentration gradient depends on the diffusion coefficient and the distance involved. This is the foundational physics source for the entire project: everything about estimating synaptic transmission time using Fick's Law traces back to this original 19th-century paper, written decades before synapses themselves were even discovered.

### 2. Eccles, J. C. (1964). The Physiology of Synapses. Springer-Verlag.

Eccles, a Nobel laureate for his work on synaptic transmission, provides detailed physiological measurements of synaptic delay — the brief time between a presynaptic signal arriving and a postsynaptic response occurring — establishing the roughly 0.5-1 millisecond delay figure that this project's Fick's Law estimate is checked against. This is the empirical, measured reference value the project's theoretical diffusion-time calculation is meant to approximate.

### 3. Stiles, J. R., & Bartol, T. M. (2001). Monte Carlo methods for simulating realistic synaptic microphysiology using MCell. In Computational Neuroscience: Realistic Modeling for Experimentalists. CRC Press.

Stiles and Bartol describe detailed computational simulations of neurotransmitter diffusion across a real synaptic cleft, accounting for molecular crowding and realistic cleft geometry rather than treating diffusion as occurring through simple, open space. This is a useful, more advanced companion source acknowledging an honest limitation of the project's simplified Fick's Law estimate: real synaptic diffusion is more geometrically complex than the straight-line approximation the project's calculation uses.

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design a "Synaptic Diffusion Timer" — a simplified model applying Fick's Law of diffusion to estimate the time for neurotransmitter molecules to cross the ~20-nanometer synaptic cleft, compared against published measured synaptic delay times. Innovation Proposal I documents the model setup and initial calculation.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review:** Fick's laws of diffusion, published synaptic transmission delay measurements (typically ~0.5-1 millisecond).
- [ ] **Hypothesis:** a diffusion-time estimate calculated from Fick's Law, using the known synaptic cleft width and typical neurotransmitter diffusion coefficients, falls within the same order of magnitude as published measured synaptic delay times.
- [ ] **Variables:** diffusion coefficient and cleft width as inputs; calculated diffusion time as DV compared against published measured delay.
- [ ] **Methodology:** direct application of the diffusion-time approximation (distance²/diffusion coefficient) using published values, compared to measured synaptic delay literature.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] A short explainer, "Your Synapses Are Doing Chemistry Class Diffusion Problems," using the same calculation; dissemination through school chemistry/physics clubs and STEM outreach.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] Simulates how estimated diffusion time changes with cleft width and diffusion coefficient, letting users test sensitivity — a direct algebraic sensitivity analysis; documented on GitHub.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] Policy proposal recommending this synaptic-diffusion module be adopted as a cross-listed lesson in chemistry (diffusion) and biology (synaptic transmission) curricula, aimed at curriculum coordinators.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Capstone integrates the timer, the validation comparison, the explainer, the sensitivity model, and the curriculum proposal into one "diffusion physics of the synapse" portfolio.

## Skills This Project Builds


## Why This Project Impresses

Applies a genuinely foundational physical-chemistry principle rigorously to a real neuroscience quantity with a checkable, published comparison value — appropriately hard, fully computable.

---

## How the Six Outputs Link Into One Portfolio

Every artifact in this project answers the same precise question at growing depth: how fast, in actual milliseconds, does a signal really cross a synapse? Unit I builds the first Fick's-Law-based timer. Unit II turns it into a genuine validation check against real measured synaptic delay values from the neuroscience literature. Unit III explains that exact calculation to an audience who's never realized "diffusion," a chemistry-class word, is happening inside their own brain right now. Unit IV shows precisely how sensitive the estimate is to cleft width and diffusion coefficient — real scientific sensitivity analysis, not guesswork. Unit V asks for this exact calculation to become the standard example bridging chemistry's diffusion unit and biology's synapse unit. A chemistry or biology mentor sees a 19th-century physics law applied rigorously and checkably to one of neuroscience's most fundamental numbers.

## Maximize Your Impact — What To Do With This After the Season

- Propose the Synaptic Diffusion Timer as a cross-listed chemistry/biology lesson to your school's science department.
- Submit the diffusion-time validation calculation to a science fair under biophysics or neuroscience.
- Share the sensitivity-analysis tool publicly as a resource for students learning Fick's Law.

