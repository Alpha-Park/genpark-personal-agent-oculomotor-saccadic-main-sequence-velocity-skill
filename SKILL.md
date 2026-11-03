---
name: genpark-personal-agent-oculomotor-saccadic-main-sequence-velocity-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Oculomotor Saccadic Main Sequence peak velocity saturation, reaction latency, antisaccade directional error rate, and frontal executive inhibitory control.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Oculomotor Saccadic Main Sequence Skill

A sovereign personal agent capability for evaluating fast eye movement kinematics, pontine burst neuron firing velocity, frontal eye field (FEF) target acquisition, and dorsolateral prefrontal cortex (DLPFC) antisaccade suppression.

## Core Capabilities
- **Main Sequence Velocity Saturation**: Formulates asymptotic peak velocity scaling ($V_{pred} = 650 \cdot (1 - e^{-A / 14})$ in $\text{deg/s}$) across variable target eccentricities.
- **Saccadic Latency Timing**: Measures visual disengagement and motor execution reaction time (normative: $180 - 240\text{ ms}$).
- **Antisaccade Directional Error Rate**: Quantifies prefrontal executive failure to suppress reflexive prosaccades toward peripheral distractions ($< 20\%$).
- **Visual Distraction & Focus Gating**: Triggers focus corridors, minimizes desktop notification popups, and prescribes eye convergence exercises.

## Fast Invocation
```python
from client import OculomotorSaccadicMainSequenceClient

client = OculomotorSaccadicMainSequenceClient()
res = client.evaluate_saccadic_kinetics(
    amplitude_deg=10.0,
    peak_velocity_deg_s=335.0,
    latency_ms=205.0
)
print("Main Sequence Ratio:", res["main_sequence_ratio"])
print("Executive Score:", res["saccadic_executive_score"], "/ 100")
```
