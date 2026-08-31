# 3. Building a Tiny Brain Network

*Simple Graphs and Neuron Connections*

**Field:** Neuroscience × Computer Science &nbsp;·&nbsp; **Project ID:** `computer-science/03-building-a-tiny-brain-network`

```{admonition} Big Question
:class: tip
Using only basic data structures (a simple list of connections, like a friend-network diagram), can students build a small model showing how a signal spreads through a simplified network of connected "neurons"?
```

```{admonition} Why This Matters
:class: note
Real neural networks are built from exactly this basic idea — nodes connected to other nodes, with a signal passing along connections — and building a tiny, simplified version from scratch with beginner-level tools makes the concept of "neural network" concrete instead of a buzzword.
```

## Core Literature — Read This Before Starting Unit II

Real, verified sources for this project. Read these before Unit II begins — they're what your literature review and hypothesis should be built on.

### 1. Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. Nature, 393(6684), 440-442.

Watts and Strogatz's landmark paper showed that networks built with mostly local connections plus a small number of random long-range connections combine high clustering with short overall path length — a "small-world" structure found in systems ranging from social networks to real brain connectivity. This is a useful, more advanced companion source for a student wanting to extend the project's simple node-and-connection model into the specific network-structure question of how connection density and pattern affect how efficiently a signal spreads.

### 2. Bassett, D. S., & Bullmore, E. T. (2006). Small-world brain networks. The Neuroscientist, 12(6), 512-523.

Bassett and Bullmore review evidence that real brain connectivity, at multiple scales, shows this small-world structure — efficiently combining local, specialized processing with fast global communication between distant regions. This grounds the project's simplified node-network model in real neuroscience, showing that "more connections generally spread signals faster and further" is a genuine, well-evidenced property of real brain organization, not just an assumption.

### 3. Sporns, O. (2011). Networks of the Brain. MIT Press.

Sporns's book provides an accessible, thorough introduction to applying network-science concepts (nodes, connections, paths) specifically to brain connectivity, including how signal spread through a network depends on its connection pattern — directly relevant background for a student wanting a deeper, more rigorous foundation for extending this project's simple simulator.

## Exact Steps, Unit by Unit

Every step below plugs into the fixed season process described in {doc}`../../process` — tournaments and laboratories run identically regardless of field. Only the content below is specific to this project.

### Unit I — Learning Innovation Challenge
*Weeks 1–4 · Required artifact: **Innovation Proposal I***

**Process for this unit (same for every project in the chapter):** Run the Week 2 **Confidence Gap** tournament (see the Universal Process chapter).

**Steps specific to this project:**

- [ ] Students design a "Tiny Brain Network Builder" — a simple diagram or program representing a small number of "neurons" (nodes) connected to each other (like a friend-network or flowchart), where clicking or triggering one node passes a signal to its connections. Innovation Proposal I documents the network design (how many nodes, how they're connected) and the signal-passing rule.

### Unit II — Research Investigation
*Weeks 5–8 · Required artifact: **Research Investigation / Prospectus***

**Process for this unit (same for every project in the chapter):** Week 6 **Prediction Ladder** tournament + Week 7 **Build-a-System** laboratory.

**Steps specific to this project:**

- [ ] **Literature review:** basic explanations of how real neurons connect and pass signals (plain-language, no advanced circuit math), and basic graph/network concepts (nodes, connections, paths) already familiar from things like friend-network diagrams.
- [ ] **Hypothesis:** a small network built with more connections between nodes will spread an initial signal to more of the network, and faster, than a network with fewer connections, tested by comparing signal-spread patterns across differently-connected sample networks.
- [ ] **Variables:** number of connections in the network as the thing being compared; how many nodes receive the signal, and how quickly, as the outcome.
- [ ] **Methodology:** build a few small toy networks with different amounts of connection, trigger a signal at one starting node in each, and record/compare how the signal spreads.
- [ ] **Investigation blueprint:** the network-building method and signal-spread recording method, fully documented and doable by hand for a small enough network or with simple code for a larger one.

### Unit III — Public Communication & Social Impact
*Weeks 9–12 · Required artifact: **Communication Product + Dissemination Plan***

**Process for this unit (same for every project in the chapter):** Week 10 **Signal and the Noise** tournament + Week 11 **Message Transmission** laboratory.

**Steps specific to this project:**

- [ ] A short video, "I Built a Tiny Brain Out of Code," using the same network builder and results; dissemination through school coding club and STEM outreach for younger students.

### Unit IV — Memory/Decision Systems Simulation
*Weeks 13–16 · Required artifact: **Simulation Model IV***

**Process for this unit (same for every project in the chapter):** Week 14 **Distortion Chain** tournament + Week 15 **Distortion & Reconstruction** laboratory.

**Steps specific to this project:**

- [ ] Simulates the tiny brain network interactively, letting users add or remove connections and nodes and watch a signal spread visually, directly illustrating the Unit II comparison; documented on GitHub.

### Unit V — Policy Formation Simulation
*Weeks 17–20 · Required artifact: **Policy Draft Document***

**Process for this unit (same for every project in the chapter):** Week 18 **Self-Forecast Duel** tournament + Week 19 **Identity & System Construction** laboratory.

**Steps specific to this project:**

- [ ] Policy proposal recommending this project be used as a standard beginner data-structures assignment (introducing the idea of nodes and connections) in intro computer science classes, aimed at computer science curriculum coordinators.

### Unit VI — Integration & Summit
*Weeks 21–24 · Required artifact: **Capstone Project***

**Process for this unit (same for every project in the chapter):** Week 22 **Capstone Prototype Development** laboratory, leading into the Week 24 Summit.

**Steps specific to this project:**

- [ ] Capstone integrates the network builder, the connection-comparison study, the video, the interactive signal-spread simulator, and the curriculum proposal into one "tiny brain network" portfolio.

## Skills This Project Builds

- Building basic graph/network data structures (nodes, connections).
- Designing a controlled comparison across differently-structured networks.
- Producing a clear, visual explanation of a genuinely complex computer-science concept.
- Building an interactive, adjustable network-visualization tool.
- Proposing a foundational data-structures lesson to a CS curriculum.


## Why This Project Impresses

Introduces a genuinely important computer-science and neuroscience concept (networks, connections, signal spread) using only beginner-level tools, with a real, hands-on comparison study.

---

## How the Six Outputs Link Into One Portfolio

Every unit of this project makes the same idea more concrete: connections determine how far and how fast a signal spreads. Unit I builds the first toy network. Unit II turns it into a genuine comparison between differently-connected networks. Unit III explains that finding to an audience who's heard "neural network" as a buzzword without ever seeing one built from scratch. Unit IV makes the whole thing interactive and visual. Unit V asks CS classes to adopt this exact project as the introduction to data structures and networks. A CS mentor sees a student who built one of computer science's most important concepts — the network — from first principles, small enough to fully understand and explain.

## Maximize Your Impact — What To Do With This After the Season

- Propose the project as a standard introduction to data structures and networks in your CS curriculum.
- Submit the connection-comparison study to a science fair under computer science or computational neuroscience.
- Publish the interactive network-builder publicly as a teaching resource.

