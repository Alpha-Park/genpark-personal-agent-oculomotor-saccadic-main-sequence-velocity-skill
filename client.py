"""
Oculomotor Saccadic Main Sequence & Executive Inhibitory Kinetics Engine.
Provides deterministic, zero-dependency modeling of saccadic peak velocity vs amplitude saturation,
prosaccade latency (ms), antisaccade directional error rate (%), and frontal eye field (FEF) executive control.
"""

import math
from typing import Dict, Any, List, Optional


class OculomotorSaccadicMainSequenceClient:
    """
    Deterministic client for calculating Oculomotor Saccadic Main Sequence Kinetics.
    Assesses paramedian pontine reticular formation (PPRF) burst neurons, superior colliculus drive,
    dorsolateral prefrontal cortex (DLPFC) inhibitory gating, and central dopaminergic tone.
    """

    def __init__(self):
        pass

    def evaluate_saccadic_kinetics(
        self,
        amplitude_deg: float,
        peak_velocity_deg_s: float,
        latency_ms: float,
        antisaccade_error_rate_pct: float = 12.0,
        duration_ms: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates Main Sequence velocity ratio and executive inhibitory control score.
        Exponential saturation formula: V_pred = 650.0 * (1.0 - exp(-amplitude / 14.0))
        Normative values:
        - Latency: 180.0 - 240.0 ms
        - Main Sequence Ratio (V_actual / V_pred): 0.85 - 1.18
        - Antisaccade Directional Error Rate: < 20.0%
        """
        if amplitude_deg <= 0 or peak_velocity_deg_s <= 0 or latency_ms <= 0:
            return {"error": "Amplitude, peak velocity, and latency must be strictly positive"}
        if antisaccade_error_rate_pct < 0 or antisaccade_error_rate_pct > 100:
            return {"error": "Antisaccade error rate must be between 0% and 100%"}

        # 1. Main Sequence Predicted Velocity
        v_pred = round(650.0 * (1.0 - math.exp(-amplitude_deg / 14.0)), 1)
        velocity_ratio = round(peak_velocity_deg_s / v_pred, 2)

        # 2. Executive Inhibitory & Saccadic Control Score (0 - 100)
        score = 80.0
        if 0.88 <= velocity_ratio <= 1.15:
            score += 10.0
        elif velocity_ratio < 0.72:
            score -= 25.0  # Slow saccades / brainstem depression
        elif velocity_ratio < 0.82:
            score -= 12.0
        elif velocity_ratio > 1.25:
            score -= 8.0  # Hypermetric saccadic burst

        if 180.0 <= latency_ms <= 235.0:
            score += 5.0
        elif latency_ms > 290.0:
            score -= 18.0
        elif latency_ms > 255.0:
            score -= 8.0
        elif latency_ms < 140.0:
            score -= 10.0  # Express saccades / premature triggers

        if antisaccade_error_rate_pct <= 15.0:
            score += 5.0
        elif antisaccade_error_rate_pct >= 35.0:
            score -= 22.0
        elif antisaccade_error_rate_pct > 22.0:
            score -= 10.0

        saccade_score = round(min(100.0, max(5.0, score)), 1)

        if saccade_score >= 85.0 and 0.85 <= velocity_ratio <= 1.18 and antisaccade_error_rate_pct <= 18.0:
            tier = "OPTIMAL_SACCADIC_EXECUTIVE_CONTROL"
            interp = f"Crisp saccadic acceleration (Vel {peak_velocity_deg_s} deg/s, {velocity_ratio}x pred) and low error ({antisaccade_error_rate_pct}%); intact FEF and superior colliculus bursts."
            guidance = "Superior visual target acquisition and top-down prefrontal executive inhibition."
        elif velocity_ratio < 0.75:
            tier = "SACCADIC_VELOCITY_SLOWING"
            interp = f"Markedly slowed saccades ({peak_velocity_deg_s} deg/s < {v_pred} deg/s pred, Ratio {velocity_ratio}); reflects pontine reticular burst neuron fatigue or pharmacological sedation."
            guidance = "Brainstem saccadic generator slowing. Minimize visual clutter; screen for sedating medications or central neuro-fatigue."
        elif antisaccade_error_rate_pct > 30.0:
            tier = "PREFRONTAL_INHIBITORY_GATING_DEFICIT"
            interp = f"Elevated antisaccadic error rate ({antisaccade_error_rate_pct}% > 20%); reflects DLPFC failure to suppress reflexive prosaccades to visual distractors."
            guidance = "Executive distractibility detected. Implement focus-gating intervals and minimize peripheral screen notifications."
        else:
            tier = "PROLONGED_SACCADIC_LATENCY"
            interp = f"Delayed saccadic reaction time ({latency_ms} ms > 250 ms); visual attention disengagement latency."
            guidance = "Attention disengagement delay. Optimize screen contrast and take structured visual resting breaks."

        return {
            "amplitude_deg": amplitude_deg,
            "peak_velocity_deg_s": peak_velocity_deg_s,
            "predicted_velocity_deg_s": v_pred,
            "main_sequence_ratio": velocity_ratio,
            "latency_ms": latency_ms,
            "duration_ms": duration_ms,
            "antisaccade_error_rate_pct": antisaccade_error_rate_pct,
            "saccadic_executive_score": saccade_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
