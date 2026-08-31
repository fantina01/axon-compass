# 2. Brainwaves, Literally

*Fourier Analysis of EEG Signals as Superposed Waves*

**Field:** Neuroscience × Physics &nbsp;·&nbsp; **Project ID:** `physics/02-brainwaves-literally`

```{admonition} Big Question
:class: tip
Can basic wave physics (frequency, amplitude, superposition) explain what EEG "brainwave bands" (alpha, beta, theta, delta) actually are, without needing advanced signal-processing math?
```

```{admonition} Why This Matters
:class: note
People casually say "brainwaves" without realizing it's a literal physics statement — EEG signals genuinely are superpositions of oscillations at different frequencies, and the same wave-addition principles taught in intro physics (constructive/destructive interference, frequency, amplitude) explain what's being measured.
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Berger, H. (1929). Uber das Elektrenkephalogramm des Menschen. Archiv fur Psychiatrie und Nervenkrankheiten, 87, 527-570.

Hans Berger's original paper is the first published human EEG recording, and it's where he first described the "alpha rhythm" — a roughly 10 Hz oscillation that appeared strongly when a resting subject's eyes were closed and diminished when eyes opened. This is the foundational discovery behind the whole project: everything about "brainwave bands" traces back to Berger's original observation of this one specific, reproducible oscillation.

### 2. Adrian, E. D., & Matthews, B. H. C. (1934). The Berger rhythm: Potential changes from the occipital lobes in man. Brain, 57(4), 355-385.

Adrian and Matthews independently confirmed Berger's controversial claim (many scientists initially doubted a signal so small could really be measured from outside the skull) and specifically demonstrated the eyes-closed/eyes-open alpha-blocking effect in careful, controlled recordings. This paper is what turned Berger's discovery from a disputed claim into an accepted, replicated finding — it's the direct scientific basis for the specific eyes-open/eyes-closed comparison this project's Unit II hypothesis tests.

### 3. Pfurtscheller, G., & Lopes da Silva, F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: Basic principles. Clinical Neurophysiology, 110(11), 1842-1857.

This review formalizes "event-related desynchronization" — the general principle that specific frequency bands (like alpha) predictably decrease in power when the brain region associated with that rhythm becomes actively engaged, and increase again at rest. It generalizes Berger's original eyes-open/eyes-closed alpha finding into the broader framework used throughout modern EEG research, useful for understanding that the phenomenon in this project is one specific case of a much more general and well-established principle.

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design a "Brainwave Decoder Kit" — using a public EEG dataset and a basic Fourier-transform tool (available in most spreadsheet/plotting software without requiring the student to derive the transform from scratch) to break a raw EEG signal into its component frequency bands. Innovation Proposal I documents the chosen dataset and the visual decomposition of one sample signal.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review:** classical wave superposition principles, basic EEG frequency-band literature (alpha ~8-12 Hz, beta ~13-30 Hz, etc.).
- [ ] **Hypothesis:** a resting-eyes-closed EEG recording will show a dominant peak in the alpha band (8-12 Hz) compared to an eyes-open recording from the same public dataset, consistent with the well-known "alpha blocking" phenomenon.
- [ ] **Variables:** eyes-open/closed condition as IV; alpha-band power as DV.
- [ ] **Methodology:** apply frequency decomposition to paired open/closed segments from a public dataset and compare alpha-band power.
- [ ] **Investigation blueprint:** fully specified using existing data, no data collection risk, and computable with standard tools.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] A short explainer, "Brainwaves Are Real Waves — Here's the Physics," using the same decomposition; dissemination through school physics and biology clubs, STEM outreach for younger students.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] Simulates a synthetic signal built by adding sine waves of different frequencies/amplitudes (a direct, hands-on superposition demo), then shows how a Fourier decomposition recovers the original component frequencies — directly illustrating the same principle used on the real EEG data; documented on GitHub.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] Policy proposal recommending physics curricula use EEG frequency decomposition as a real-world application example when teaching wave superposition and Fourier concepts, aimed at physics curriculum coordinators.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Capstone integrates the decoder kit, the alpha-blocking comparison, the explainer, the synthetic-wave demo, and the curriculum proposal into one "brainwaves are literal waves" portfolio.

## Skills This Project Builds


## Why This Project Impresses

Makes an abstract physics concept (superposition/Fourier decomposition) concrete and biologically meaningful using only tools already available in standard software — approachable rigor rather than intimidating math for its own sake.

---

## How the Six Outputs Link Into One Portfolio

This project's six artifacts all point at one moment: the instant someone closes their eyes and their alpha rhythm appears. Unit I's decomposition kit first shows that moment exists in real EEG data. Unit II turns it into a real, hypothesis-driven comparison — eyes-open versus eyes-closed alpha power, measured, not assumed. Unit III explains that exact finding as a literal application of a wave-physics concept most students think is "just math." Unit IV rebuilds the same phenomenon from scratch, adding sine waves together and recovering them with a Fourier decomposition, so a visitor can see with their own eyes that superposition isn't abstract. Unit V asks physics teachers to use this exact demonstration as the standard real-world example for wave superposition. A physics or STEM curriculum reader sees a project that didn't just borrow neuroscience vocabulary — it took a real physics theorem and used it to make a real, verifiable claim about the brain, then closed the loop by proposing the whole demonstration become how the theorem gets taught.

## Maximize Your Impact — What To Do With This After the Season

- Offer the Brainwave Decoder Kit as a guest demonstration to a physics class currently studying waves and superposition.
- Submit the alpha-blocking analysis to a science fair under neuroscience or signal processing.
- Share the synthetic-wave/Fourier demo publicly as an open teaching resource for other students learning Fourier analysis.

