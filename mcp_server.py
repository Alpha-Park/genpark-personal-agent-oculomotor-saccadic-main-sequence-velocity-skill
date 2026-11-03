"""
MCP Server for Oculomotor Saccadic Main Sequence Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating saccadic peak velocity saturation, latencies, and antisaccade errors.
"""

import sys
import json
from typing import Dict, Any
from client import OculomotorSaccadicMainSequenceClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_saccadic_kinetics",
                "description": "Calculates Oculomotor Saccadic Main Sequence predicted velocity, latency (ms), antisaccade error rate (%), and executive inhibitory control score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "amplitude_deg": {
                            "type": "number",
                            "description": "Target saccade amplitude in degrees of visual angle (e.g. 10.0 deg, 20.0 deg)."
                        },
                        "peak_velocity_deg_s": {
                            "type": "number",
                            "description": "Peak saccadic angular velocity in degrees per second (e.g. 330.0 deg/s)."
                        },
                        "latency_ms": {
                            "type": "number",
                            "description": "Saccadic reaction time / latency in milliseconds (e.g. 205.0 ms, normative 180-240 ms)."
                        },
                        "antisaccade_error_rate_pct": {
                            "type": "number",
                            "description": "Antisaccade directional suppression error rate percentage (normative < 20.0%, default: 12.0%).",
                            "default": 12.0
                        },
                        "duration_ms": {
                            "type": "number",
                            "description": "Total saccade duration in milliseconds (optional, e.g. 45.0 ms)."
                        }
                    },
                    "required": ["amplitude_deg", "peak_velocity_deg_s", "latency_ms"]
                }
            }
        ]
    }


def handle_request(client: OculomotorSaccadicMainSequenceClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_saccadic_kinetics":
            dur = args.get("duration_ms")
            res = client.evaluate_saccadic_kinetics(
                amplitude_deg=float(args.get("amplitude_deg", 10.0)),
                peak_velocity_deg_s=float(args.get("peak_velocity_deg_s", 330.0)),
                latency_ms=float(args.get("latency_ms", 205.0)),
                antisaccade_error_rate_pct=float(args.get("antisaccade_error_rate_pct", 12.0)),
                duration_ms=float(dur) if dur is not None else None
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = OculomotorSaccadicMainSequenceClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
