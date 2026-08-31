# AXON REVIEW — FULL CURRICULUM ALIGNMENT
### Neuroscience × Physics — All Ten Projects, All Twenty-Four Weeks

---

### HOW THIS DOCUMENT WORKS

The Operational Handbook already defines *how* every week runs — the reading-analysis pattern, the five tournament formats (Confidence Gap, Prediction Ladder, Signal and the Noise, Distortion Chain, Self-Forecast Duel), the five laboratory formats (Build-a-System Simulation, Message Transmission Simulation, Distortion & Reconstruction Experiment, Identity & System Construction Workshop, Capstone Prototype Development), and the fixed 75-minute session shapes. None of that is repeated here.

What this document provides is the piece that was missing: **exactly what content each of Physics's ten projects plugs into that fixed structure, week by week, for all 24 weeks.** A chapter leader running "The Brain as a Circuit" should never have to guess what their Week 10 tournament station is about, or what their Week 15 lab's manipulated stimulus should be — it's specified here, tied directly to the equations, datasets, and literature named in each project file, and specified so that Week 4's Innovation Proposal, Week 8's Research Investigation, Week 12's communication product, Week 16's simulation, and Week 20's policy draft all visibly build on each other, exactly the way the Handbook's own unit-to-unit logic requires.

Every entry below names the correct universal format from the Handbook and then gives the project-specific content for that slot — nothing here contradicts or replaces the Handbook's mechanics. Because physics projects live and die on whether the numbers actually check out, every Week 8 and Week 16 entry below states the specific equation, the specific published reference value, and the specific comparison being made — the same standard of concreteness the Economics alignment held throughout.

---
---

## PROJECT 1 — The Brain as a Circuit
*Modeling neurons with RC circuit theory*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is Lapicque's 1907 integrate-and-fire idea — that a nerve's excitation builds toward a threshold the same way a capacitor charges in a circuit. Pre-reading: participants sketch, from memory, what they think a capacitor's charging curve looks like on a graph, before seeing any real curve. Research Summary I must state the RC analogy in plain language and name one everyday device (a camera flash, a phone charger) that uses the same charging curve.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station is a short quiz asking participants to predict, before calculating, how long a simple RC circuit (given R and C values) takes to reach 63% of full charge — the definition of one time constant, τ = RC. Log every prediction against the real calculated value; the gap becomes Week 4 evidence.

**Week 3 (Field-in-Action Experiment):** three trials building or simulating a simple RC circuit with a different resistor each time, timing how long the capacitor voltage takes to visibly rise, and recording predicted vs. observed charging time at every trial.

**Week 4 (Main Output — Innovation Proposal I):** design the Neuron-as-Circuit Teaching Kit — a physical or simulated RC circuit paired with a real public-dataset neural recording, chosen specifically because its subthreshold voltage trace resembles a capacitor charging curve. The proposal documents the exact R and C values used and cites the Week 2 confidence-gap size and the Week 3 trial data as evidence that the charging-curve intuition is worth teaching explicitly.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is the leaky integrate-and-fire model as a deliberate simplification of Hodgkin and Huxley's full 1952 biophysical model. Research Summary II must state the season's testable hypothesis precisely: an RC circuit's voltage-time curve, with R and C tuned to published membrane time-constant values, will match a real neuron's subthreshold voltage trace within a specified error tolerance.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real neuron types with different published membrane time constants; participants predict which neuron's subthreshold voltage will rise fastest, rehearsing that a smaller τ = RC means a faster response.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw neural voltage trace. Reception receives it only partially; Filtering decides which segment matters; Integration adds a "known R and C" assumption; Reconstruction rebuilds the expected curve from memory; Decision judges whether the rebuilt curve still looks like a legitimate RC charging curve. Log exactly where the curve's shape gets distorted.

**Week 8 (Main Output — Research Investigation):** fit τ = RC to published membrane time-constant values (Koch, 1999), then compare the resulting predicted voltage trace against a real public-dataset subthreshold recording using goodness-of-fit (R²) as the outcome measure. The poster's central chart overlays the fitted RC curve on the real neural trace, stating the R² value directly and citing the Week 6 tournament's time-constant intuition as the framing.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to explain a circuit equation to an audience that assumes physics and biology are unrelated subjects.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 R² fit is presented two ways — as "a circuit equation" versus "your neurons are basically tiny batteries" — rated for how relatable and credible each framing feels to a mixed physics/biology audience.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground-truth message is the real Week 8 fit result. Team 2 delivers it in the winning framing; Team 3 tracks which numbers survive; Team 4 reconstructs the claim from memory; Team 5 decides whether the reconstructed version still states the equation correctly.

**Week 12 (Main Output — Public Communication Project):** produce "Your Brain Cells Are Basically Tiny Batteries," presenting the real τ = RC fit from Week 8 in the winning framing, distributed at the school science fair and to STEM outreach programs for younger students.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a student might remember an equation as "close enough" without recalling the real error tolerance it was actually fit within.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state the real Week 8 R² value once, distract, then ask participants to restate it — quantifying how a specific number degrades into a vague impression like "pretty good."

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real fitted RC curve; initial recall of the R² value is collected; the manipulation subtly changes the stated fit quality; final recall is collected; comparison shows how easily the false number replaces the real one, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive leaky integrate-and-fire simulator — sliders for R, C, and firing threshold — calibrated so its default settings reproduce the real Week 8 fit, letting a user watch firing rate change as resistance or capacitance changes. Documented on GitHub with the τ = RC derivation shown step by step.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how "physics" and "biology" became separate subject identities in most school curricula despite sharing this exact equation.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** the team seals three predictions about how a real physics teacher will react to the circuit-meets-neuroscience module, opened and scored in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the school's physics curriculum — origin, influence, stakeholder, environmental, system — to find the realistic point where a circuits-meets-neuroscience unit could actually be inserted.

**Week 20 (Main Output — Policy Formation Simulation):** draft the curriculum-integration proposal recommending physics classes adopt a circuits-meets-neuroscience module using this exact model, citing the real Week 8 fit-quality result and the Week 16 interactive model, aimed at physics curriculum committees.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline traces one equation, τ = RC, from a Week 1 sketch through a real validated fit, a video, a working simulator, to a curriculum proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the integrate-and-fire simulator as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer who has not seen an RC circuit before.

**Week 23 (Capstone Draft):** integrate the teaching kit, the real fit-quality investigation, the video, the simulator, and the curriculum proposal into one draft, honestly naming the model's known limitation — it captures timing, not action-potential shape.

**Week 24 (Summit):** exhibition places the physical or simulated circuit next to the live integrate-and-fire model; reflection defense states the real R² value and what it does and doesn't prove.

---
---

## PROJECT 2 — Brainwaves, Literally
*Fourier analysis of EEG signals as superposed waves*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is Berger's 1929 discovery of the alpha rhythm — a roughly 10 Hz oscillation that strengthens when a resting subject's eyes close. Pre-reading: participants guess whether "brainwaves" is a literal physics term or just a figure of speech, and write down their guess before reading.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station shows two overlapping sine waves and asks participants to sketch, before checking, what the summed (superposed) wave looks like. Log the gap between the predicted and the real superposed waveform.

**Week 3 (Field-in-Action Experiment):** three trials adding two sine waves of different frequency and amplitude combinations by hand or with simple plotting software, comparing the predicted sum to the real one each time.

**Week 4 (Main Output — Innovation Proposal I):** design the Brainwave Decoder Kit — using a public EEG dataset and a standard spreadsheet/plotting Fourier tool to break one raw EEG signal into its component frequency bands (alpha ~8–12 Hz, beta ~13–30 Hz, theta, delta). The proposal documents the chosen dataset and the visual decomposition of one sample signal, citing the Week 2 superposition-prediction gap and the Week 3 hand-addition trials as the conceptual groundwork.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is Adrian and Matthews's 1934 confirmation of Berger's alpha rhythm, specifically the eyes-closed/eyes-open comparison. Research Summary II must state the season's testable hypothesis precisely: a resting eyes-closed EEG recording will show a dominant peak in the alpha band (8–12 Hz) compared to an eyes-open recording from the same public dataset.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real EEG frequency-band definitions with escalating frequency ranges; participants predict which band a described mental state (relaxed, drowsy, alert) belongs to.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw EEG signal. Reception receives only a short segment; Filtering decides which frequency range looks dominant by eye; Integration adds a "known alpha-blocking" assumption; Reconstruction rebuilds an expected frequency spectrum from memory; Decision judges whether the reconstructed spectrum still matches the real one.

**Week 8 (Main Output — Research Investigation):** apply frequency decomposition to paired eyes-open/eyes-closed segments from a public dataset and compare alpha-band power directly. The poster's central chart is a side-by-side power spectrum for both conditions, stating the real alpha-band power difference and citing the Week 6 tournament's band-identification practice.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is Pfurtscheller and Lopes da Silva's 1999 framework generalizing alpha-blocking into "event-related desynchronization" — the general principle this project's one specific finding is a case of.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 alpha-power finding delivered two ways — as a raw spectral-power statistic versus "your brain has a literal 10 Hz idle hum, and it goes quiet when you focus" — rated for relatability.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 alpha-power comparison, passed through the five roles to test whether the specific eyes-open/eyes-closed numbers survive retelling or collapse into a vague "brain waves change."

**Week 12 (Main Output — Public Communication Project):** produce "Brainwaves Are Real Waves — Here's the Physics," presenting the real Week 8 finding using the winning framing, disseminated through school physics and biology clubs and STEM outreach for younger students.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a listener might remember "the alpha wave disappeared" when the real data shows it only decreased in power.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state the real Week 8 alpha-power percentage once, distract, then ask for a restatement — quantifying how the specific number drifts.

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real spectral comparison; initial recall is collected; the manipulation alters the reported alpha-power change; final recall is collected; comparison shows the false number's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive synthetic-wave tool — sliders that add sine waves of different frequencies and amplitudes together, then run a Fourier decomposition that recovers the original component frequencies, directly illustrating the same principle applied to the real EEG data in Week 8. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how wave superposition is taught abstractly in most physics classes, disconnected from any real-world signal.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether a physics teacher will find the alpha-blocking demo a compelling real-world example of superposition, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the physics curriculum's wave/superposition unit to find where the EEG demonstration could realistically replace a more abstract example.

**Week 20 (Main Output — Policy Formation Simulation):** draft the curriculum recommendation that physics classes use EEG frequency decomposition as the standard real-world application example when teaching wave superposition, citing the real Week 8 alpha-power data and the Week 16 synthetic-wave demo.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 sketch of two summed waves through a real eyes-open/eyes-closed dataset finding to a curriculum proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the synthetic-wave/decomposition tool as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with a peer unfamiliar with Fourier analysis.

**Week 23 (Capstone Draft):** integrate the decoder kit, the real alpha-blocking investigation, the explainer, the synthetic-wave demo, and the curriculum proposal into one "brainwaves are literal waves" draft.

**Week 24 (Summit):** exhibition shows the decoder kit's real spectral output beside the live synthetic-wave demo; reflection defense states the real alpha-power numbers found in Week 8.

---
---

## PROJECT 3 — How Fast Is a Thought?
*Measuring and modeling neural conduction velocity*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is Helmholtz's 1850 first-ever measurement of nerve conduction velocity, made by stimulating a frog's nerve at two points and timing the muscle-response difference. Pre-reading: participants estimate, in their own words, whether nerve signals travel closer to the speed of sound or the speed of a thrown baseball, before any reference values are given.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station is a falling-ruler reaction-time test; participants predict their own reaction time in milliseconds before taking the test. Log the predicted-vs-actual gap for every participant.

**Week 3 (Field-in-Action Experiment):** three trials of the falling-ruler test per participant, recording reaction time at every trial and tracking whether repeated trials produce faster or more consistent times.

**Week 4 (Main Output — Innovation Proposal I):** design the Reaction Time and Nerve Speed Toolkit — the falling-ruler test paired with an estimated physical nerve-pathway distance from hand to spinal cord to brain and back. The proposal documents a pilot reaction-time dataset collected from peers, citing the Week 2 confidence gap and the Week 3 trial-to-trial pattern.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is the published nerve conduction velocity ranges compiled in *Principles of Neural Science* (Kandel et al.), from under 2 m/s for slow unmyelinated fibers up to 120 m/s for fast myelinated ones. Research Summary II must state the season's testable hypothesis precisely: measured reaction times, converted to an implied average conduction velocity using estimated pathway distance, will fall within the published range for the relevant nerve fiber types.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real reaction-time values from published studies; participants predict which implies the fastest conduction velocity once distance is factored in.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw reaction-time measurement. Reception receives only the number; Filtering decides whether it looks "fast" or "slow"; Integration adds an assumed pathway-distance figure; Reconstruction rebuilds an implied velocity from memory; Decision judges whether the reconstructed velocity still looks physiologically plausible.

**Week 8 (Main Output — Research Investigation):** apply distance = speed × time algebra to real reaction-time measurements collected from a peer sample, computing implied conduction velocity, mean, and standard deviation. The poster's central chart shows each participant's implied velocity against the published reference range from Kandel et al., citing the Week 6 tournament's calibration.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to communicate a real, personally-collected measurement to an audience that assumes "speed of thought" is only a figure of speech.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 implied-velocity finding delivered two ways — as a raw m/s statistic versus "I can measure the speed of your reflexes with a ruler" — rated for engagement.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 implied velocity, passed through the five roles to test whether the specific number survives retelling.

**Week 12 (Main Output — Public Communication Project):** produce "I Can Measure the Speed of Your Reflexes With a Ruler," using the real Week 8 data, disseminated through school science fairs and STEM outreach for younger students.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a participant might remember their own reaction time as faster than the real recorded number.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state a real recorded reaction time once, distract, then ask for a restatement — quantifying how the specific millisecond value drifts.

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is a real reaction-time trial; initial recall is collected; the manipulation alters the stated time; final recall is collected; comparison shows the false number's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive sensitivity-analysis tool, letting a user change the assumed pathway distance or reaction-time measurement error and watch the implied conduction velocity shift — a direct propagation-of-error exercise calibrated using the real Week 8 dataset. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how hands-on, equipment-free labs rarely make it into a school's standard science curriculum despite requiring nothing but a ruler and a stopwatch.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether the science department will adopt the toolkit as a standard lab, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the school's science curriculum-adoption process to find the realistic path for a new joint physics/biology lab.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that the school adopt this toolkit as a standard hands-on physics-meets-biology lab exercise, citing the real Week 8 velocity data and the Week 16 sensitivity model, aimed at science department curriculum leads.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 estimate through a real personally-measured conduction velocity to a curriculum-adoption proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the sensitivity-analysis tool as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the toolkit, the real reaction-time dataset, the video, the sensitivity model, and the curriculum-adoption proposal into one "measuring the speed of thought" draft.

**Week 24 (Summit):** the falling-ruler test runs live at the exhibition table; reflection defense states the real implied velocity found and how sensitive it is to the distance assumption.

---
---

## PROJECT 4 — Thermodynamics of Thinking
*Modeling the brain's energy budget*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is the well-documented fact that the brain, at roughly 2% of body weight, consumes roughly 20% of resting energy. Pre-reading: participants estimate, as a percentage, how much of the body's resting energy the brain uses, before seeing the real figure.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station asks participants to estimate the number of neurons in the human brain and the energy cost of one ion-pump cycle, before checking published order-of-magnitude values. Log the predicted-vs-real gap on both estimates.

**Week 3 (Field-in-Action Experiment):** three trials each scaling a single-neuron ion-pump energy estimate up to a whole-brain estimate using a different assumed neuron count each time, tracking how much the final answer changes.

**Week 4 (Main Output — Innovation Proposal I):** design the Brain Energy Budget Calculator — a bottom-up model estimating the energy required to maintain the sodium-potassium gradient across a typical neuron's membrane, scaled to a whole-brain estimate, compared against published whole-body metabolic data. The proposal documents the calculation approach and initial estimate, citing the Week 2 estimation gap and the Week 3 scaling-sensitivity pattern.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is Attwell and Laughlin's 2001 detailed, bottom-up energy budget for grey-matter signaling. Research Summary II must state the season's testable hypothesis precisely: a bottom-up estimate built from single-neuron ion-pump energy cost, scaled by estimated neuron count, will land within a reasonable order of magnitude of the published whole-brain energy-consumption figure (~20% of resting metabolic rate, per Raichle & Gusnard, 2002).

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real order-of-magnitude estimation problems from everyday life (grains of sand on a beach, cells in the body); participants predict which estimate lands closest to the accepted real value, building the estimation instinct Unit II's calculation requires.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a single per-neuron energy-cost figure. Reception receives it without context; Filtering decides which assumptions to keep; Integration adds an assumed total neuron count; Reconstruction rebuilds the whole-brain estimate from memory; Decision judges whether the reconstructed estimate still looks like a reasonable order-of-magnitude figure.

**Week 8 (Main Output — Research Investigation):** perform the dimensional-analysis-style calculation using published per-neuron ion-pump energy estimates (Attwell & Laughlin) and neuron-count estimates, then check the result against the published ~20% whole-body resting-energy figure. The poster's central chart compares the calculated estimate to the real published figure on the same axis, citing the Week 6 estimation-calibration exercise.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is the common myth that intense mental effort burns significantly more calories than rest — and why the real physics says otherwise.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 finding delivered two ways — "the brain's energy use barely changes with mental effort" versus "thinking hard doesn't burn many extra calories (but existing does)" — rated for which framing corrects the myth more effectively.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 estimate, passed through the five roles to test whether the myth-correcting nuance survives retelling or collapses back into "thinking burns tons of calories."

**Week 12 (Main Output — Public Communication Project):** produce "Why Thinking Hard Doesn't Burn Many Extra Calories (But Existing Does)," using the real Week 8 calculation, disseminated through school health/nutrition classes and STEM outreach.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a listener might remember "the brain barely uses energy" — the opposite distortion of the myth this project corrects.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state the real Week 8 percentage once, distract, then ask for a restatement — quantifying how the specific 20% figure drifts.

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real energy-budget figure; initial recall is collected; the manipulation alters the stated percentage; final recall is collected; comparison shows the false number's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive sensitivity-analysis tool, letting a user change the assumed neuron count or ion-pump efficiency and watch the whole-brain energy estimate shift, calibrated using the real Week 8 numbers. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how physics energy concepts and biology metabolism units are taught as separate, unconnected topics.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether a curriculum committee will adopt the calculator as a joint lesson, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the science department's curriculum structure to find where a physics-energy/biology-metabolism joint lesson could realistically fit.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that the energy-budget model become a standard lesson bridging physics energy/thermodynamics and biology metabolism curricula, citing the real Week 8 calculation and Week 16 sensitivity model.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 percentage guess through a real order-of-magnitude calculation to a joint-curriculum proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the sensitivity-analysis tool as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the calculator, the real order-of-magnitude investigation, the myth-busting explainer, the sensitivity model, and the curriculum proposal into one "thermodynamics of the brain" draft.

**Week 24 (Summit):** exhibition displays the real calculated figure beside the published reference figure; reflection defense states honestly how much the estimate depends on its underlying assumptions.

---
---

## PROJECT 5 — Resonance and the Startle Reflex
*Damped oscillator models of sensory habituation*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is Thompson and Spencer's 1966 defining paper on habituation — that repeated-stimulus response decline is typically negatively accelerated, large drops early, smaller drops later. Pre-reading: participants sketch, from memory, what they expect a habituation curve to look like across ten repeated trials.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station is a damped-pendulum or damped-spring demo; participants predict how many swings it will take to visibly settle, before timing the real decay.

**Week 3 (Field-in-Action Experiment):** three trials of the damped-oscillator demo with a different damping condition each time (more friction, less friction, added weight), recording predicted vs. observed settling behavior at every trial.

**Week 4 (Main Output — Innovation Proposal I):** design the Startle Habituation Tracker — a simple, ethically-designed experiment measuring peers' self-reported or observable startle response (blink/flinch) to a repeated harmless sound across trials, following the Blumenthal et al. (2005) safety guidelines. The proposal documents the experimental protocol and a pilot trial, citing the Week 2 confidence gap and the Week 3 damping pattern.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is Groves and Thompson's 1970 dual-process theory — that the observed response curve is the net result of a genuine habituation process and a competing sensitization process. Research Summary II must state the season's testable hypothesis precisely: startle-response magnitude across repeated trials will follow a decay pattern statistically well-fit by an exponentially-damped curve, analogous to a damped oscillator's amplitude decay.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real damped-oscillator decay curves with different damping coefficients; participants predict which curve settles fastest.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw startle-response trial-by-trial dataset. Reception receives only the first three trials; Filtering decides which trials look like real decline versus noise; Integration adds an assumed damping coefficient; Reconstruction rebuilds the expected full curve from memory; Decision judges whether the reconstructed curve still fits a damped exponential.

**Week 8 (Main Output — Research Investigation):** run the repeated-trials within-subject startle protocol and curve-fit the response-decay data to a damped exponential using basic curve-fitting tools. The poster's central chart overlays the real data points on the fitted damped-oscillator curve, stating the fitted damping coefficient and citing the Week 6 tournament's decay intuition.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to explain a physics equation applied to a feeling every participant has already had — the fading intensity of a repeated jump scare.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 finding delivered two ways — as a damping-coefficient statistic versus "why the second jump scare never hits as hard" — rated for relatability.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 fitted curve, passed through the five roles to test whether the specific damping-coefficient number survives retelling.

**Week 12 (Main Output — Public Communication Project):** produce "Why the Second Jump Scare Never Hits as Hard," using the real Week 8 tracker data, disseminated through school psychology/physics clubs and general STEM outreach.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a participant might remember startling "just as much" on the last trial as the first, despite the real decay data.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** show the real trial-1 and trial-10 response magnitudes once, distract, then ask for a restatement — quantifying how the real decline drifts toward "about the same."

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real decay dataset; initial recall is collected; the manipulation flattens the reported decline; final recall is collected; comparison shows the flattening's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive damped-oscillator model, showing the real collected habituation data side-by-side with an adjustable damping-coefficient curve, letting a user fit different individuals' decay rates. Documented on GitHub with the oscillator equation shown explicitly.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how physics (damped oscillators) and psychology/biology (habituation) are taught as unrelated subjects despite sharing this exact math.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether the science department will adopt the comparison as a cross-listed lab, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the school's physics and psychology/biology course sequences to find the realistic point for a cross-listed lab.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that this comparison become a standard cross-listed lab in physics (damped oscillators) and psychology/biology (habituation) courses, citing the real Week 8 fitted curve and Week 16 interactive model.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 sketched guess through a real fitted damping coefficient to a cross-listed-lab proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the damped-oscillator model as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the tracker, the real curve-fit investigation, the video, the oscillator model, and the curriculum proposal into one "physics of habituation" draft.

**Week 24 (Summit):** exhibition lets visitors adjust the damping-coefficient slider live and compare it to the chapter's real collected startle data; reflection defense states the real fitted coefficient honestly.

---
---

## PROJECT 6 — The Physics of a Concussion
*Impact forces, momentum, and traumatic brain injury risk*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is Holbourn's 1943 argument that rotational acceleration, not just linear impact force, is a major cause of traumatic brain injury. Pre-reading: participants predict whether a "harder" hit or a "more rotational" hit is more dangerous, before the reading resolves it.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station asks participants to predict, before calculating, how much peak force drops when the same impulse (change in momentum) is spread over a longer time — the impulse-momentum theorem in action.

**Week 3 (Field-in-Action Experiment):** three trials dropping the same object onto surfaces with different amounts of padding, timing the impact duration and comparing predicted vs. observed differences in peak force.

**Week 4 (Main Output — Innovation Proposal I):** design the Concussion Risk Physics Explainer and Helmet Comparison — analyzing publicly available helmet safety-rating data through the lens of impulse and energy-absorption physics. The proposal documents the chosen dataset and initial physics-based interpretation of what separates higher- and lower-rated helmets, citing the Week 2 confidence gap and the Week 3 padding trials.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is Rowson and Duma's 2013 combined linear/rotational acceleration injury-risk model, built from real instrumented-helmet football data. Research Summary II must state the season's testable hypothesis precisely: helmets with higher published safety ratings show measurably longer impact-force time-profiles, consistent with better energy absorption via impulse-momentum principles, than lower-rated helmets.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real published helmet safety ratings; participants predict which helmet's impact-force profile lasts longest (spreads the impulse over more time).

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw helmet impact-test dataset. Reception receives only the peak-force number; Filtering decides whether that number alone indicates safety; Integration adds the impact-duration data; Reconstruction rebuilds an expected safety ranking from memory; Decision judges whether the reconstructed ranking still matches the real published rating.

**Week 8 (Main Output — Research Investigation):** perform a comparative analysis of publicly published helmet impact-test data (Broglio et al., 2010, style measurements), applying impulse-momentum calculations by hand. The poster's central chart compares impact-force duration across helmet ratings, citing the Week 6 tournament's ranking predictions.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to explain equipment-safety physics to athletes and coaches who make real purchasing and rule decisions.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 finding delivered two ways — as a raw impulse-momentum statistic versus "the physics of why some helmets actually work better" — rated for which framing coaches say they'd actually act on.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 helmet comparison, passed through the five roles to test whether the specific ranking survives retelling to athletic staff.

**Week 12 (Main Output — Public Communication Project):** produce "The Physics of Why Some Helmets Actually Work Better," using the real Week 8 comparison, disseminated through school sports programs, athletic training staff, and STEM outreach.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a coach might remember "the expensive helmet is obviously safer" without recalling the real impact-duration data behind that ranking.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state the real Week 8 safety ranking once, distract, then ask for a restatement — quantifying how the specific ranking degrades or reorders.

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real helmet comparison dataset; initial recall is collected; the manipulation swaps two helmets' rankings; final recall is collected; comparison shows the swap's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive impulse-momentum model, showing how impact force changes as a function of impact duration for a fixed change in momentum — illustrating why spreading out an impact reduces peak force, calibrated with the real Week 8 helmet data. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how school athletic programs make equipment-purchasing decisions with or without physics-based evidence.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether the athletic director will review the equipment recommendation, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the school's athletic-equipment purchasing process to find the realistic decision point.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that the athletic program adopt equipment-purchasing guidelines informed by the impulse-based physics comparison, citing the real Week 8 data and Week 16 model, aimed at athletic directors and school safety committees.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 dropped-object demo through a real published helmet-data comparison to an equipment-purchasing recommendation.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the impulse-momentum model as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the helmet comparison, the real impulse-momentum investigation, the explainer, the impact-force model, and the equipment policy into one "physics of concussion prevention" draft.

**Week 24 (Summit):** exhibition displays the real helmet-comparison chart beside the live impulse-momentum model; reflection defense states honestly what public helmet-rating data can and can't prove.

---
---

## PROJECT 7 — Optics of Perception
*Modeling the eye as a physical lens system*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is the thin-lens equation (1/f = 1/d_o + 1/d_i) as it applies to the human eye. Pre-reading: participants predict whether a nearsighted or farsighted eye focuses light in front of or behind the retina, before the reading resolves it.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station presents a simple lens setup (object distance and focal length given); participants predict the image distance using the thin-lens equation before calculating it.

**Week 3 (Field-in-Action Experiment):** three trials with a real or simulated lens, changing the object distance each time, comparing predicted vs. calculated image distance at every trial.

**Week 4 (Main Output — Innovation Proposal I):** design the Eye-as-Lens Calculator — a tool applying the thin-lens equation to model how corrective lenses shift the focal point of a simplified eye model back onto the retina. The proposal documents the model's assumptions and a sample calculation for a specific refractive error, using publicly available typical eye-dimension data, citing the Week 2 confidence gap and Week 3 trial pattern.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is Atchison and Smith's *Optics of the Human Eye* application of formal optical theory to real ocular anatomy and refractive errors (myopia, hyperopia). Research Summary II must state the season's testable hypothesis precisely: the calculated corrective lens power needed to refocus a simplified myopic/hyperopic eye model onto the retina, using the thin-lens equation, matches published typical prescription ranges for corresponding degrees of refractive error.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real degrees of refractive error (in diopters); participants predict which requires the strongest corrective lens power.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a simplified eye's refractive-error value. Reception receives only the raw diopter number; Filtering decides whether it's myopic or hyperopic; Integration adds an assumed eye-dimension figure; Reconstruction rebuilds the required lens power from memory; Decision judges whether the reconstructed lens power still matches a real prescription range.

**Week 8 (Main Output — Research Investigation):** apply 1/f = 1/d_o + 1/d_i directly across a range of simulated refractive errors, comparing the calculated lens power to published prescription reference ranges (Emsley, 1952, style calculations). The poster's central chart plots calculated lens power against published prescription ranges, citing the Week 6 tournament's calibration.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to explain that a glasses prescription is literally a solved optics homework problem, to an audience who has never made that connection.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 finding delivered two ways — as a diopter-calculation statistic versus "your glasses prescription is just physics homework" — rated for relatability.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 calculation, passed through the five roles to test whether the specific lens-power number survives retelling.

**Week 12 (Main Output — Public Communication Project):** produce "Your Glasses Prescription Is Just Physics Homework," using the real Week 8 calculation, disseminated through school optics/physics clubs and STEM outreach for younger students.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a listener might remember "glasses just magically fix vision" without recalling the specific calculation behind it.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state a real calculated lens power once, distract, then ask for a restatement — quantifying how the specific diopter value drifts.

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is a real calculation; initial recall is collected; the manipulation alters the stated lens power; final recall is collected; comparison shows the false number's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive ray-tracing simulation through the simplified eye-lens model, visually showing how light rays converge before, on, or behind the retina under different refractive-error and corrective-lens conditions, calibrated with the real Week 8 values. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how thin-lens optics is usually taught with abstract, disconnected examples rather than the eye itself.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether physics curriculum coordinators will adopt the eye-as-lens module, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the physics curriculum's optics unit to find where the eye-as-lens module could realistically replace or supplement the standard example.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that this eye-as-lens module be adopted as the standard applied example when teaching thin-lens optics, citing the real Week 8 validation and Week 16 ray-tracing simulation, aimed at physics curriculum coordinators.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 prediction through a real validated calculation to a curriculum-adoption proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the ray-tracing simulation as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the calculator, the real validation investigation, the explainer, the ray-tracing simulation, and the curriculum proposal into one "optics of the eye" draft.

**Week 24 (Summit):** exhibition lets visitors adjust refractive-error and lens-power sliders and watch the ray-tracing converge live; reflection defense states honestly where the simplified fixed-lens model diverges from the real, dynamically-accommodating eye (Charman, 2008).

---
---

## PROJECT 8 — Diffusion and the Synapse
*Fick's Law and neurotransmitter release timing*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is Fick's 1855 original diffusion law — decades before synapses themselves were discovered. Pre-reading: participants estimate, in milliseconds, how long they think it takes a signal to cross a synapse, before any reference value is given.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station presents a diffusion-time estimation problem (given distance and diffusion coefficient); participants predict the diffusion time before calculating it using distance²/diffusion coefficient.

**Week 3 (Field-in-Action Experiment):** three trials of a simple diffusion demonstration (a drop of food coloring in water, or an equivalent), timing how long it takes to visibly spread a fixed distance, comparing predicted vs. observed each time.

**Week 4 (Main Output — Innovation Proposal I):** design the Synaptic Diffusion Timer — a simplified model applying Fick's Law to estimate the time for neurotransmitter molecules to cross the ~20-nanometer synaptic cleft, compared against published measured synaptic delay times. The proposal documents the model setup and initial calculation, citing the Week 2 confidence gap and Week 3 diffusion-demo trials.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is Eccles's 1964 measured synaptic-delay figure of roughly 0.5–1 millisecond, the empirical reference value this project's calculation is checked against. Research Summary II must state the season's testable hypothesis precisely: a diffusion-time estimate calculated from Fick's Law, using the known synaptic cleft width and typical neurotransmitter diffusion coefficients, falls within the same order of magnitude as published measured synaptic delay times.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real diffusion scenarios with different distances; participants predict which diffuses fastest, since diffusion time scales with distance squared.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw cleft-width and diffusion-coefficient pair. Reception receives only the cleft width; Filtering decides which diffusion coefficient value to use; Integration adds the distance²/diffusion-coefficient formula; Reconstruction rebuilds the estimated time from memory; Decision judges whether the reconstructed estimate still lands near the published 0.5–1 ms range.

**Week 8 (Main Output — Research Investigation):** apply the diffusion-time approximation (distance²/diffusion coefficient) using published values for the synaptic cleft width and neurotransmitter diffusion coefficient, then compare the result to the measured synaptic-delay literature (Eccles, 1964). The poster's central chart places the calculated estimate directly beside the published measured range, citing the Week 6 tournament's distance-squared intuition.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to explain that "diffusion," a chemistry-class word, is literally happening inside a synapse right now.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 finding delivered two ways — as a distance²/diffusion-coefficient calculation versus "your synapses are doing chemistry class diffusion problems" — rated for relatability.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 estimate, passed through the five roles to test whether the specific millisecond figure survives retelling.

**Week 12 (Main Output — Public Communication Project):** produce "Your Synapses Are Doing Chemistry Class Diffusion Problems," using the real Week 8 calculation, disseminated through school chemistry/physics clubs and STEM outreach.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a listener might remember synaptic transmission as "instant" despite the real, calculable delay.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state the real Week 8 estimate once, distract, then ask for a restatement — quantifying how the specific millisecond figure drifts toward "basically instant."

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real diffusion-time calculation; initial recall is collected; the manipulation alters the stated time; final recall is collected; comparison shows the false figure's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive sensitivity-analysis tool, letting a user change cleft width and diffusion coefficient and watch the estimated diffusion time shift, calibrated with the real Week 8 values. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how chemistry's diffusion unit and biology's synapse unit are taught as unconnected topics.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether curriculum coordinators will adopt this synaptic-diffusion module, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the school's chemistry and biology course sequences to find the realistic point for a cross-listed lesson.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that this synaptic-diffusion module be adopted as a cross-listed lesson in chemistry (diffusion) and biology (synaptic transmission) curricula, citing the real Week 8 calculation and Week 16 sensitivity model.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 millisecond guess through a real Fick's-Law-based estimate to a cross-listed-lesson proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the sensitivity-analysis tool as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the timer, the real validation investigation, the explainer, the sensitivity model, and the curriculum proposal into one "diffusion physics of the synapse" draft.

**Week 24 (Summit):** exhibition displays the real calculated diffusion time beside the published measured range; reflection defense honestly names the simplification (Stiles & Bartol, 2001) that real synaptic diffusion is more geometrically complex than the straight-line approximation used.

---
---

## PROJECT 9 — Pupillometry as a Pendulum Problem
*Modeling pupil response with simple feedback dynamics*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is the pupillary light reflex as a textbook feedback-control system — rapid constriction, gradual settling to a new equilibrium size. Pre-reading: participants predict, in seconds, how long they think their own pupil takes to settle after a light change, before any measurement.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station is a simple first-order system demo (a cup of hot water cooling, or an equivalent settling system); participants predict how long it takes to visibly approach its new equilibrium, before timing the real settling curve.

**Week 3 (Field-in-Action Experiment):** three trials of a safe, controlled light-level change with a phone camera, each with a different lighting condition, recording predicted vs. observed pupil-settling time.

**Week 4 (Main Output — Innovation Proposal I):** design the Pupillary Feedback Tracker — a simple, safe experiment using a phone camera and controlled lighting change to record how pupil diameter changes over time in response to a light-level step change, following Fotiou et al.'s (2000) safe light-level guidelines. The proposal documents the experimental setup and a pilot recording, citing the Week 2 confidence gap and Week 3 trial pattern.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is Ellis's 1981 quantified measurement of the human pupillary light reflex's time-course — latency, constriction speed, and settling behavior in normal subjects. Research Summary II must state the season's testable hypothesis precisely: the pupil's diameter-vs-time response to a step change in light will be well-fit by a first-order exponential settling curve, similar to standard feedback-system responses.

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real first-order system response curves with different time constants; participants predict which settles fastest.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw pupil-diameter-over-time recording. Reception receives only the first few frames; Filtering decides which portion looks like the real settling curve; Integration adds an assumed time constant; Reconstruction rebuilds the expected full curve from memory; Decision judges whether the reconstructed curve still fits a first-order exponential.

**Week 8 (Main Output — Research Investigation):** measure pupil diameter over time via video following a controlled, safe light-level change, and curve-fit the resulting data to a first-order exponential model. The poster's central chart overlays the real measured data on the fitted curve, stating the fitted time constant and citing the Week 6 tournament's settling-time intuition.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to explain that a visible human reflex runs on the same math as a thermostat, to an audience who has never made that connection.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 finding delivered two ways — as a fitted time-constant statistic versus "your eyes have a thermostat" — rated for relatability.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 fitted curve, passed through the five roles to test whether the specific time-constant number survives retelling.

**Week 12 (Main Output — Public Communication Project):** produce "Your Eyes Have a Thermostat," using the real Week 8 tracker data, disseminated through school physics/biology clubs and STEM outreach.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a viewer might remember the pupil response as instantaneous despite the real, measurable settling time.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state the real Week 8 fitted time constant once, distract, then ask for a restatement — quantifying how the specific number drifts.

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real pupil-response curve; initial recall is collected; the manipulation alters the stated settling time; final recall is collected; comparison shows the false figure's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive first-order feedback-system model, showing how a "time constant" parameter shapes the settling curve, directly paralleling the real collected pupil data from Week 8. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how physics control-systems concepts and biology reflex concepts are taught as unconnected topics.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether curriculum coordinators will adopt this tracker as a joint lab, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the school's physics and biology course sequences to find the realistic point for a joint control-systems/reflexes lab.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that this tracker be adopted as a standard applied lab connecting physics (feedback/control systems) and biology (reflexes) curricula, citing the real Week 8 fitted curve and Week 16 model.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 settling-time guess through a real fitted time constant to a joint-lab proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the feedback-system model as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the tracker, the real curve-fit investigation, the video, the feedback-system model, and the curriculum proposal into one "pupil as feedback system" draft.

**Week 24 (Summit):** exhibition lets visitors watch a live pupil-response recording beside the fitted model curve; reflection defense states the real fitted time constant found.

---
---

## PROJECT 10 — Sound, Cochlea, and Resonance
*Modeling frequency discrimination with resonant cavities*

#### UNIT I — Weeks 1–4

**Week 1 (Reading):** Article I focus is von Bekesy's Nobel Prize-winning direct observation of traveling waves along the basilar membrane — different frequencies peak at different physical locations. Pre-reading: participants predict whether a longer or shorter organ pipe produces a lower pitch, before the reading connects this to the cochlea.

**Week 2 (Game Tournament — THE CONFIDENCE GAP):** the station presents strings or tubes of different lengths; participants predict which produces the lowest pitch before plucking or blowing each one.

**Week 3 (Field-in-Action Experiment):** three trials changing the length or tension of a simple resonant tube/string, recording predicted vs. observed resonant frequency each time.

**Week 4 (Main Output — Innovation Proposal I):** design the Cochlea-as-Resonant-Cavity Demo Kit — a set of simple resonant tubes or strings of varying length/tension, paired with a diagram mapping this principle onto the cochlea's basilar membrane structure. The proposal documents the physical demo design and the anatomical mapping, citing the Week 2 confidence gap and Week 3 trial pattern.

#### UNIT II — Weeks 5–8

**Week 5 (Reading):** Article II focus is basic resonance and standing-wave physics (resonant frequency depends on length/tension/stiffness) and von Bekesy's traveling-wave theory of cochlear tonotopy. Research Summary II must state the season's testable hypothesis precisely: a simple resonant-tube/string model, with dimensions scaled to approximate the basilar membrane's stiffness gradient, produces a resonant-frequency-vs-position pattern qualitatively consistent with published cochlear tonotopic maps (high frequencies at the base, low frequencies at the apex).

**Week 6 (Game Tournament — THE PREDICTION LADDER):** stations present five real tube/string dimensions; participants predict which position along a modeled "cochlea" would resonate at the highest frequency.

**Week 7 (Cognitive Laboratory — BUILD-A-SYSTEM SIMULATION):** the stimulus is a raw resonant-frequency measurement at one position along the physical model. Reception receives only that one measurement; Filtering decides whether it's a base or apex position; Integration adds an assumed stiffness gradient; Reconstruction rebuilds the expected full frequency-position map from memory; Decision judges whether the reconstructed map still resembles a real tonotopic map.

**Week 8 (Main Output — Research Investigation):** measure the resonant frequencies of a physical model (tubes or strings of varying length) at different "positions," then compare the resulting frequency gradient pattern to published cochlear tonotopic maps. The poster's central chart plots the model's frequency-vs-position curve directly against the published cochlear map, citing the Week 6 tournament's position predictions.

#### UNIT III — Weeks 9–12

**Week 9 (Reading):** Article III focus is how to explain that the inner ear runs on the same physics as a musical instrument, to an audience who has never made that connection.

**Week 10 (Game Tournament — SIGNAL AND THE NOISE):** the real Week 8 finding delivered two ways — as a frequency-vs-position statistic versus "your inner ear is basically an organ pipe" — rated for relatability.

**Week 11 (Cognitive Laboratory — MESSAGE TRANSMISSION SIMULATION):** the ground truth is the real Week 8 comparison, passed through the five roles to test whether the specific frequency-mapping pattern survives retelling.

**Week 12 (Main Output — Public Communication Project):** produce "Your Inner Ear Is Basically an Organ Pipe," using the real Week 8 demo-kit comparison, disseminated through school music/physics clubs and STEM outreach.

#### UNIT IV — Weeks 13–16

**Week 13 (Reading):** Article IV focus is memory reconstruction, applied to why a listener might remember the cochlea as working like a single microphone rather than a spatially-organized frequency map.

**Week 14 (Game Tournament — THE DISTORTION CHAIN):** state the real Week 8 base-vs-apex frequency comparison once, distract, then ask for a restatement — quantifying how the specific frequency mapping drifts.

**Week 15 (Cognitive Laboratory — DISTORTION & RECONSTRUCTION EXPERIMENT):** observation is the real frequency-position dataset; initial recall is collected; the manipulation swaps which end is high-frequency; final recall is collected; comparison shows the swap's persistence, followed by full debrief.

**Week 16 (Main Output — Memory Systems Simulation):** build the interactive continuous simulation of resonant frequency varying with a changing stiffness/length parameter along a modeled "cochlear" length, producing a frequency-map curve directly comparable to both the physical demo and the published data from Week 8. Documented on GitHub.

#### UNIT V — Weeks 17–20

**Week 17 (Reading):** Integration article focus — applied to how acoustics/resonance and auditory biology are taught as unconnected topics.

**Week 18 (Game Tournament — THE SELF-FORECAST DUEL):** sealed predictions about whether curriculum coordinators will adopt the demo kit as a standard lesson, opened in Week 19.

**Week 19 (Cognitive Laboratory — IDENTITY & SYSTEM CONSTRUCTION WORKSHOP):** map the physics and biology course sequences to find the realistic point for an acoustics-meets-hearing lesson.

**Week 20 (Main Output — Policy Formation Simulation):** draft the recommendation that this demo kit be adopted as a standard applied-physics lesson connecting acoustics/resonance to auditory biology, citing the real Week 8 comparison and Week 16 simulation, aimed at physics and biology curriculum coordinators.

#### UNIT VI — Weeks 21–24

**Week 21 (Synthesis):** the throughline runs from a Week 1 pitch-length prediction through a real validated frequency-position comparison to a curriculum-adoption proposal.

**Week 22 (Cognitive Laboratory — CAPSTONE PROTOTYPE DEVELOPMENT):** finalize the continuous frequency-map simulation as capstone centerpiece; map at least three evidence links back to Units I, II, and IV; feedback-test with an unfamiliar peer.

**Week 23 (Capstone Draft):** integrate the demo kit, the real resonance-mapping investigation, the explainer, the frequency-map simulation, and the curriculum proposal into one "physics of hearing" draft.

**Week 24 (Summit):** exhibition lets visitors pluck or blow the physical resonant tubes/strings and immediately compare the result to the live frequency-map simulation and the real cochlear data; reflection defense honestly names the limitation (Robles & Ruggero, 2001; Hudspeth, 2014) that the living cochlea actively amplifies frequencies beyond what this passive resonance model captures.

---
---

### CROSS-PROJECT NOTE

Every project above runs the same 24-week skeleton from the Operational Handbook — five tournaments, five labs, five main outputs building toward one capstone. Every one of Physics's ten projects was built to the same depth throughout: a real equation stated explicitly (τ = RC, Fourier superposition, distance = speed × time, the energy-budget calculation, the damped-oscillator equation, the impulse-momentum theorem, the thin-lens equation, Fick's Law, the first-order feedback-system equation, resonant-frequency-vs-length), a real published reference value to check it against, and an explicit statement of which earlier week's evidence each later step depends on, from Week 1 through Week 24.
