# 9. Pupillometry as a Pendulum Problem

*Modeling Pupil Response with Simple Feedback Dynamics*

**Field:** Neuroscience × Physics &nbsp;·&nbsp; **Project ID:** `physics/09-pupillometry-as-a-pendulum-problem`

```{admonition} Big Question
:class: tip
Can a basic feedback-control model (similar to the physics of a self-correcting system, like a thermostat or a damped pendulum returning to equilibrium) describe how the pupil adjusts to changing light levels?
```

```{admonition} Why This Matters
:class: note
Pupillary light reflex is a textbook example of a biological feedback-control system, and its response curve (rapid constriction, gradual settling to a new equilibrium size) can be modeled with the same first-order feedback-system math used in intro physics/engineering for control systems — connecting a visible, easily-measured reflex to genuine systems-physics concepts.
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Loewenfeld, I. E. (1993). The Pupil: Anatomy, Physiology, and Clinical Applications. Iowa State University Press.

Loewenfeld's comprehensive reference work documents the detailed physiology and time-course of the pupillary light reflex, including how pupil diameter changes in response to a step change in light and settles toward a new equilibrium size — the exact real-world behavior the project models using first-order feedback-system math. This is the standard clinical and physiological reference for everything related to pupil behavior.

### 2. Ellis, C. J. (1981). The pupillary light reflex in normal subjects. British Journal of Ophthalmology, 65(11), 754-759.

Ellis measured the detailed time-course of the human pupillary light reflex in a large sample of normal subjects, quantifying typical response latency, constriction speed, and settling behavior following a light-level change. This provides real, quantified human physiological data the project's own recorded pupil-diameter-over-time measurements can be compared against for validity.

### 3. Fotiou, F., Fountoulakis, K. N., Goulas, A., Alexopoulos, L., & Palikaras, A. (2000). Automated standardized pupillometry with optical method for purposes of clinical practice and research. Clinical Physiology, 20(5), 336-347.

This paper describes methodology for reliably and safely measuring pupillary responses using accessible optical/video methods, relevant to the project's phone-camera-based measurement approach, and discusses standard safe light-level ranges used in pupillometry research. It's a useful practical methods reference for ensuring the project's experimental setup follows safe, established measurement practices.

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design a "Pupillary Feedback Tracker" — a simple, safe experiment using a phone camera and controlled lighting change to record how pupil diameter changes over time in response to a light-level step change. Innovation Proposal I documents the experimental setup and a pilot recording.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review:** pupillary light reflex physiology, first-order system response curves (time constant, settling time) from intro control-systems/physics.
- [ ] **Hypothesis:** the pupil's diameter-vs-time response to a step change in light will be well-fit by a first-order exponential settling curve, similar to standard feedback-system responses.
- [ ] **Variables:** time since light-level change as IV; pupil diameter as DV.
- [ ] **Methodology:** video-based measurement of pupil diameter over time following a controlled, safe light-level change, curve-fit to a first-order exponential model.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] A short video, "Your Eyes Have a Thermostat," using the same tracker data; dissemination through school physics/biology clubs and STEM outreach.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] Simulates a first-order feedback system's response to a step input, showing how the "time constant" parameter shapes the settling curve, directly paralleling the collected pupil data; documented on GitHub.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] Policy proposal recommending this tracker be adopted as a standard applied lab connecting physics (feedback/control systems) and biology (reflexes) curricula, aimed at curriculum coordinators.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Capstone integrates the tracker, the curve-fit study, the video, the feedback-system model, and the curriculum proposal into one "pupil as feedback system" portfolio.

## Skills This Project Builds


## Why This Project Impresses

A safe, fully replicable experiment connecting a visible biological reflex to genuine control-systems physics — rigorous, novel-feeling, and well within reach.

---

## How the Six Outputs Link Into One Portfolio

This project's throughline is a single visible, measurable reflex, made more precise at every stage. Unit I sets up a safe, simple phone-camera experiment. Unit II turns the resulting footage into a genuine curve-fit, checking the pupil's real response shape against the standard first-order feedback-system model. Unit III explains that exact fitted result to an audience who's never thought of their own eyes as running a feedback-control system, the same kind used in a thermostat. Unit IV lets a visitor adjust a time-constant parameter and watch the predicted response curve change to match. Unit V asks for this exact lab to become standard practice bridging physics control-systems concepts and biology reflex concepts. A mentor in physics, engineering, or physiology sees a safe, original, fully-replicable experiment connecting a visible human reflex to genuine feedback-systems mathematics.

## Maximize Your Impact — What To Do With This After the Season

- Propose the Pupillary Feedback Tracker as a joint physics/biology lab connecting control systems and reflexes.
- Submit the curve-fit study to a science fair under biophysics or physiological engineering.
- Share the phone-camera measurement protocol publicly so other students can replicate the experiment safely.

