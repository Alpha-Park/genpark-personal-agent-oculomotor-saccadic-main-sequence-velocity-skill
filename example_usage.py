"""
Example Usage: Oculomotor Saccadic Main Sequence & Executive Inhibitory Kinetics.
Demonstrates zero-dependency calculation of saccadic peak velocity, latency, antisaccade error rate, and executive scoring.
"""

from client import OculomotorSaccadicMainSequenceClient


def main():
    client = OculomotorSaccadicMainSequenceClient()
    print("=== Oculomotor Saccadic Main Sequence Demo ===")

    # Test Case 1: Healthy sharp visual target acquisition (10 deg saccade)
    res1 = client.evaluate_saccadic_kinetics(
        amplitude_deg=10.0,
        peak_velocity_deg_s=335.0,
        latency_ms=205.0,
        antisaccade_error_rate_pct=11.5,
        duration_ms=42.0
    )
    print("\nTest Case 1: Optimal Saccadic Dynamics (10 deg saccade)")
    print(f"  Amplitude: {res1['amplitude_deg']} deg | Peak Velocity: {res1['peak_velocity_deg_s']} deg/s (Pred: {res1['predicted_velocity_deg_s']} deg/s)")
    print(f"  Main Sequence Ratio: {res1['main_sequence_ratio']} | Latency: {res1['latency_ms']} ms")
    print(f"  Antisaccade Error Rate: {res1['antisaccade_error_rate_pct']}%")
    print(f"  Executive Score: {res1['saccadic_executive_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Slowed saccades & elevated distractibility (prefrontal gating deficit)
    res2 = client.evaluate_saccadic_kinetics(
        amplitude_deg=15.0,
        peak_velocity_deg_s=250.0,
        latency_ms=275.0,
        antisaccade_error_rate_pct=38.0
    )
    print("\nTest Case 2: Saccadic Slowing & Prefrontal Distractibility Pattern")
    print(f"  Peak Velocity: {res2['peak_velocity_deg_s']} deg/s (Pred: {res2['predicted_velocity_deg_s']} deg/s, Ratio: {res2['main_sequence_ratio']})")
    print(f"  Antisaccade Error Rate: {res2['antisaccade_error_rate_pct']}%")
    print(f"  Executive Score: {res2['saccadic_executive_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
