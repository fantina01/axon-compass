# 1. The Forgetting Curve Classroom

*Redesigning Homework Around Spaced Retrieval*

**Field:** Neuroscience × Education &nbsp;·&nbsp; **Project ID:** `education/01-the-forgetting-curve-classroom`

```{admonition} Big Question
:class: tip
Can restructuring homework timing around the neuroscience of memory consolidation reduce the amount of study time students need while improving retention?
```

```{admonition} Why This Matters
:class: note
Homework load is one of the most contested issues in secondary education, and most schools schedule review with no reference to how the hippocampus consolidates memory during sleep and spaced intervals. A homework system grounded in retrieval practice and spacing effects could measurably reduce student stress while increasing learning — a rare case where evidence-based redesign helps both wellbeing and achievement simultaneously.
```

## Core Literature — Read This Before Starting Unit II

Three real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Ebbinghaus, H. (1885/1913). Memory: A Contribution to Experimental Psychology.

Hermann Ebbinghaus ran the first rigorous experiments on forgetting, testing himself on lists of meaningless syllables and timing how quickly he lost the ability to recall them. He found forgetting is not a straight-line decline — it drops fast in the first hours after learning, then levels off, so most of what's going to be forgotten is lost surprisingly soon after the learning session ends. This is the origin of the "forgetting curve" behind the whole project: it establishes that forgetting has a predictable shape, which is exactly what makes it possible to schedule review around it instead of guessing.

### 2. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. Psychological Bulletin, 132(3), 354–380.

This is a meta-analysis — a study that statistically combines results from many other studies — covering 317 separate experiments on spacing out practice versus cramming it into one session. The consistent finding: spreading the same total amount of study time across multiple sessions produces much better long-term retention than massing it into one sitting, and the ideal gap between review sessions gets longer the further in the future you need to remember the material. This paper is the strongest large-scale evidence behind "spacing beats cramming," and it's why the project's homework schedule uses increasing intervals (1, 3, 7, 16 days) rather than evenly spaced ones.

### 3. Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. Psychological Science, 17(3), 249–255.

Roediger and Karpicke had students study a passage either by re-reading it multiple times or by reading it once and then testing themselves on it. Counterintuitively, the group that reread the material felt more confident and did better on an immediate test — but a week later, the group that had quizzed themselves remembered dramatically more. This is the foundational study behind "the testing effect": the act of retrieving information from memory strengthens that memory far more than passively reviewing it does, even though it feels harder and less effective in the moment. It's the direct evidence for building retrieval-practice quizzes into the homework redesign, not just spacing out re-reading.

## Full Project Toolkit

**Quick facts:** Team size 2–4 · ~3–4 hrs/week outside session · Cost: $0 · Needs: a quiet room, no special equipment.

**Ethics flag:** Low-risk. This project surveys peers about study habits and runs a homework-schedule comparison — no sensitive topics, but it still needs a completed Ethics Review Checklist Section 1–2 before Unit II data collection, since it involves real classmates' real data.

**Materials by unit:** Unit I — two blank homework-calendar templates (paper or spreadsheet), a whiteboard for the wireframe sketch. Unit II — two matched vocabulary/formula lists (10–15 items each), a simple recall quiz template, a stopwatch or phone timer. Unit III — a phone or basic recorder for the podcast, a simple audio-editing app (free options: Audacity, GarageBand, or even a voice-memo app). Unit IV — spreadsheet software (Google Sheets is fine) for the interval calculator.

**Ready-to-use data template (Unit II):** a simple table with columns: Participant ID · Condition (Spaced/Massed) · Day 1 Score · Day 3 Score · Day 7 Score · Day 16 Score · Notes. Give every participant an ID, never a name, on the data sheet itself.

**Worked example — the hardest step (building the interval calculator, Unit IV):** start with one input cell for "days since last review," and one formula: `Retention % = 100 * EXP(-days/S)` where S is a "strength" number that gets bigger every time the material is reviewed (start S at 1, add 2 each review). Graph Retention % against days for a few different S values side by side — that side-by-side comparison *is* the whole simulator.

**Common pitfalls:** teams often forget to keep the two homework lists' total study time equal — if the spaced group gets more total minutes, the comparison is meaningless. Teams also sometimes skip the Day 16 test because it falls outside the normal session — put it on a shared calendar in Week 5 so it isn't missed.

**Elevator pitch:** "We tested whether spacing out your homework review — instead of cramming it into one night — actually helps you remember more, using the same amount of total study time. It does, and we built a tool that shows exactly why."

**Low-resource adaptation:** the whole project runs on paper — printed word lists, a hand-drawn interval chart on grid paper instead of a spreadsheet, and the "podcast" becomes a live 3-minute presentation instead of a recorded file.

---

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students identify a real classroom problem: homework is assigned in massed blocks (all math tonight, all history tomorrow) that ignore the forgetting curve. They design a "Spaced Retrieval Homework System" — a redesigned homework calendar and companion app concept that assigns retrieval-practice questions at scientifically staggered intervals (1 day, 3 days, 7 days, 16 days) instead of one-time review. The Innovation Proposal I documents: the observed problem (interviews with 15–20 students/teachers on current homework fatigue), the neuroscience rationale (Ebbinghaus forgetting curve, spacing effect, testing effect literature), and a wireframe/mockup of the redesigned homework structure. This proposal is the conceptual seed for the entire season — everything after this validates, communicates, models, and scales this single idea.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review focus:** spacing effect (Cepeda et al. meta-analyses), testing effect (Roediger & Karpicke), desirable difficulties (Bjork), and existing edtech spaced-repetition tools (Anki, SuperMemo) as prior art.
- [ ] **Abstract:** summarizes the proposed intervention and predicted retention gains.
- [ ] **Introduction:** frames homework redesign as an applied neuroscience problem.
- [ ] **Hypothesis:** students using spaced-interval homework will show significantly higher retention on a 30-day delayed test than students using massed-review homework, with equal or lower total study time.
- [ ] **Research question:** Does spacing homework according to the forgetting curve improve long-term retention without increasing workload?
- [ ] **Variables:** IV = homework scheduling condition (massed vs. spaced); DV = delayed recall accuracy, self-reported study time, stress rating.
- [ ] **Methodology:** proposed matched-groups design across two classroom sections, pre/post vocabulary or formula recall tests, 4-week intervention window.
- [ ] **Investigation blueprint:** full protocol, consent considerations, and data collection instruments ready for future execution — not yet run, but execution-ready.
This unit converts the classroom hunch from Unit I into a testable, falsifiable claim, giving the innovation scientific legitimacy it didn't have as a mockup alone.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] **Communication product:** a short investigative podcast episode, "Why Cramming Fails," featuring the same forgetting-curve research and the same homework redesign from Units I–II — not a new topic.
- [ ] **Communication Strategy Document:** target audience = parents and teachers skeptical of "less homework, more learning" claims; objective = build trust in spacing-based scheduling; scientific message = spaced retrieval beats massed review at equal time cost; misconceptions addressed = "more repetition always equals more learning"; platform = school newsletter + Spotify/podcast platforms.
- [ ] **Public Dissemination Plan:** pitched to the school's PTA meeting, distributed through partner nonprofit newsletters focused on student wellbeing, and shared with teacher professional-development groups.
- [ ] **Public impact:** positions the same intervention as something schools could realistically adopt, not just a science-fair concept.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] **What gets simulated:** the forgetting curve itself and the effect of different spacing intervals on retention probability over time.
- [ ] **Mechanisms modeled:** exponential decay of memory strength, boosted retention after each retrieval event, interaction between interval length and consolidation.
- [ ] **Why simulation matters:** lets the student show, quantitatively, why their Unit I schedule (1/3/7/16 days) outperforms daily cramming — turning the proposal's core claim into a visual, interactive proof.
- [ ] **Implementation:** a spreadsheet or lightweight Python/JavaScript model where users adjust interval length and see a retention curve update live; documented and pushed to GitHub with a README explaining the equations and their source literature.
- [ ] **How this strengthens previous units:** gives Unit II's hypothesis a visual, testable mechanism, and gives Unit III's podcast a concrete diagram to reference.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] **Policy proposal:** a district-level "Evidence-Based Homework Policy" recommending spacing guidelines replace blanket homework-minutes rules.
- [ ] **Stakeholders:** school boards, curriculum directors, teachers' unions, parent associations.
- [ ] **Institutions that benefit:** public school districts, education nonprofits, homework-help platforms.
- [ ] **Evidence support:** directly cites the Unit II investigation design and Unit IV simulation results as the evidentiary backbone, with limitations honestly stated (small proposed sample, single school context).

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] The Summit presents one coherent narrative: the classroom problem (I) → the scientific hypothesis (II) → the public case for caring (III) → the mechanism made visible (IV) → the institutional ask (V). The exhibition table shows the mockup homework calendar next to the live simulation; the capstone presentation walks judges through the same throughline; the policy defense answers questions about feasibility using the same investigation blueprint. Future directions: piloting the protocol in a real classroom next season.

## Skills This Project Builds

*Technical skills:*spreadsheet/JS modeling, data visualization. *Research skills:* literature synthesis, hypothesis construction, experimental design. *Leadership skills:* running the PTA pitch. *Communication skills:* podcast production, translating jargon. *Computational skills:* decay-function modeling. *Policy skills:* stakeholder mapping, proposal writing.

## Why This Project Impresses

Admissions committees see a student who identified a real institutional inefficiency and built a full evidence pipeline around it — rare for a high schooler. Research mentors see a legitimate, executable study design. Nonprofits and accelerators see a scalable, low-cost intervention. Scholarship committees see social impact plus rigor. Employers see product-thinking.

## How the Six Outputs Link Into One Portfolio

all four artifacts describe the identical spacing-based homework system at increasing levels of rigor and audience — proposal, study design, public case, working model, and institutional ask — reading as a single thesis-to-implementation arc.
