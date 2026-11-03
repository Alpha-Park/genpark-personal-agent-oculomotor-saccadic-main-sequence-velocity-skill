# Oculomotor Saccadic Main Sequence Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Oculomotor Saccadic Main Sequence peak velocity saturation, reaction latency, antisaccade directional error rate, and frontal executive inhibitory control.

```mermaid
flowchart TD
    VisualTarget["Peripheral Visual Target Jump (Eccentricity 5-30 deg)"] --> SuperiorColliculus["Superior Colliculus & FEF Burst Generation"]
    SuperiorColliculus --> PPRF["Paramedian Pontine Reticular Formation (PPRF)"]
    PPRF --> MainSeq["Main Sequence Peak Velocity Saturation (Vmax vs Amp)"]
    VisualTarget --> DLPFC["Dorsolateral Prefrontal Cortex (Antisaccade Inversion)"]
    DLPFC --> ErrorCalc["Antisaccade Directional Error Rate (%)"]
    MainSeq & ErrorCalc --> ExecutiveEngine["Saccadic Neuro-Kinetic & Executive Alertness Score"]
    ExecutiveEngine --> Agent["OpenClaw / Hermes Personal Agent Focus Gating"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Oculomotor Electrophysiology Standards**: Formulates Bahill exponential saturation main sequence curves, latency distribution, and antisaccade inhibition.
- **Cognitive Distractibility & Sedation Screening**: Detects brainstem burst neuron deceleration and loss of prefrontal executive gating.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import OculomotorSaccadicMainSequenceClient

client = OculomotorSaccadicMainSequenceClient()
result = client.evaluate_saccadic_kinetics(
    amplitude_deg=10.0,
    peak_velocity_deg_s=335.0,
    latency_ms=205.0
)
print("Main Sequence Ratio:", result["main_sequence_ratio"])
print("Executive Score:", result["saccadic_executive_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
