# 1. The Brain as a Circuit

*Modeling Neurons with RC Circuit Theory*

**Field:** Neuroscience × Physics &nbsp;·&nbsp; **Project ID:** `physics/01-the-brain-as-a-circuit`

```{admonition} Big Question
:class: tip
Can a basic RC (resistor-capacitor) circuit model, the same one used in introductory physics, capture the essential timing behavior of a real neuron's membrane potential?
```

```{admonition} Why This Matters
:class: note
Neurons are, at a basic biophysical level, leaky capacitors charged by ion currents — the same math taught in an intro circuits unit. Showing this connection concretely demystifies neuroscience for physics students and gives neuroscience students a rigorous, computable foundation instead of treating "the neuron fires" as a black box.
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Lapicque, L. (1907). Recherches quantitatives sur l'excitation electrique des nerfs traitee comme une polarisation. Journal de Physiologie et de Pathologie Generale, 9, 620-635.

Lapicque's century-old paper is the origin of the "integrate-and-fire" idea used in this project: he proposed that a nerve's electrical excitation could be modeled as a simple charging process building toward a threshold, similar to a capacitor charging in a circuit — long before the actual biophysical ion-channel mechanism was understood. It's included specifically because it shows this project's core analogy isn't a modern simplification invented for teaching purposes; it's the historical starting point of theoretical neuroscience itself, predating even the discovery of how ion channels work.

### 2. Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. Journal of Physiology, 117(4), 500-544.

Hodgkin and Huxley's Nobel Prize-winning work provided the full biophysical explanation for what Lapicque could only approximate: they measured how voltage-gated sodium and potassium channels open and close during a nerve impulse, and built a precise mathematical model of the action potential from real electrical measurements on squid neurons. This paper is what the "leaky" part of leaky integrate-and-fire refers to — it's the detailed ground truth the simplified circuit model is deliberately approximating, and it's worth knowing precisely what the simulator is (and isn't) capturing.

### 3. Koch, C. (1999). Biophysics of Computation: Information Processing in Single Neurons. Oxford University Press.

Koch's textbook works through exactly how a neuron's membrane can be modeled using standard circuit elements — resistors for ion channel conductance, capacitors for the membrane's charge-storing property — and derives the same RC time-constant equation (τ = RC) this project applies directly. It's the standard reference bridging real circuit theory and real neuroscience, useful specifically for checking the project's derivation against the accepted, complete version.

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design a "Neuron-as-Circuit Teaching Kit" — a physical or simulated RC circuit paired with a real (public-dataset) neural recording, letting students see side-by-side how a capacitor's charge/discharge curve resembles a neuron's subthreshold membrane potential. Innovation Proposal I documents the circuit design (using standard R and C values) and the specific dataset chosen for comparison.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review focus:** the leaky integrate-and-fire neuron model (a deliberately simplified alternative to full Hodgkin-Huxley), basic RC circuit charging equations.
- [ ] **Hypothesis:** an RC circuit's voltage-time curve, with parameters tuned to published membrane time-constant values, will match a real neuron's subthreshold voltage trace within a specified error tolerance.
- [ ] **Variables:** R and C values as IV; goodness-of-fit (R²) between circuit curve and neural trace as DV.
- [ ] **Methodology:** fit the RC time constant (τ = RC) to published membrane time constants, then compare predicted vs. actual voltage traces using a public dataset.
- [ ] **Investigation blueprint:** full equation derivation, parameter-fitting method, and error-metric definition — feasible with algebra and a spreadsheet, no calculus required beyond basic exponential functions.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] **Communication product:** a short explainer video, "Your Brain Cells Are Basically Tiny Batteries," using the same circuit-vs-neuron comparison.
- [ ] **Strategy document:** target audience = physics students intimidated by biology and biology students intimidated by physics; objective = show one equation bridges both; misconceptions addressed = "neuroscience math is too hard for physics people and vice versa."
- [ ] **Dissemination:** school science fair, STEM outreach programs for younger students.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] **What gets simulated:** the leaky integrate-and-fire model — membrane voltage charging toward a threshold, firing, and resetting, exactly analogous to a capacitor charging, hitting a set voltage, and discharging.
- [ ] **Mechanisms modeled:** RC time constant, threshold-triggered reset.
- [ ] **Why simulation matters:** turns the Unit I circuit demo into a fully interactive, adjustable model showing how changing resistance/capacitance changes firing rate — directly answering "why do some neurons fire faster than others?" using only algebra-level physics.
- [ ] **Implementation:** a spreadsheet or simple JavaScript tool with sliders for R, C, and threshold; documented on GitHub with the derivation shown step by step.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] **Policy proposal:** a curriculum-integration proposal recommending physics classes include a "circuits meet neuroscience" module using this exact model, aimed at physics curriculum committees.
- [ ] **Stakeholders:** physics teachers, biology teachers, STEM curriculum coordinators.
- [ ] **Institutions that benefit:** schools seeking to break down artificial subject silos.
- [ ] **Evidence:** cites the Unit II fit-quality results and Unit IV's interactive model.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Exhibition shows the physical/simulated circuit next to the live integrate-and-fire model; presentation walks from "a neuron is a leaky capacitor" through the curriculum proposal; reflection defense addresses the model's known limitations (it doesn't capture action-potential shape, only timing).

## Skills This Project Builds

*Technical skills:*circuit analysis, spreadsheet/JS modeling. *Research skills:* parameter fitting, error analysis. *Leadership:* running the STEM outreach session. *Communication:* video production, analogy-building. *Computational:* exponential-function modeling. *Policy:* curriculum-integration proposal writing.

## Why This Project Impresses

Demonstrates that the student can take an intro-physics concept and rigorously extend it into biology with real quantitative validation — exactly the kind of concrete, checkable interdisciplinary work admissions readers and research mentors trust over vaguer "brain waves are like physics" claims.

## How the Six Outputs Link Into One Portfolio

Every artifact in this project is the same equation, seen from a different angle. Unit I builds a physical or simulated circuit and simply notices it looks like a real neuron's voltage trace — an observation, not yet proof. Unit II turns that observation into an actual fit: real published time-constant values plugged into the circuit equation, checked against a real neural recording, with a real error metric. Unit III explains that exact fitted relationship to an audience that assumed physics and biology were unrelated subjects. Unit IV takes the same τ = RC equation and makes it touchable — sliders that let anyone feel why some neurons fire faster than others. Unit V asks a real curriculum committee to teach this exact bridge to the next generation of students. A physics teacher or research mentor doesn't see "a neuroscience project with some physics in it" — they see a single equation, derived, tested, explained, visualized, and proposed for adoption, which is precisely the throughline that makes interdisciplinary work convincing instead of decorative.

## Maximize Your Impact — What To Do With This After the Season

- Propose the Neuron-as-Circuit Teaching Kit to your school's physics or biology department as a permanent lab activity.
- Submit the model and fit-quality results to a regional science fair under computational biology or biophysics.
- Publish the interactive integrate-and-fire simulator publicly (GitHub Pages or similar) so any student worldwide can use it.

