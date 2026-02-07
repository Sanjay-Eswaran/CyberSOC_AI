from flask import Blueprint, jsonify
from database.db import get_threats

api = Blueprint("api", __name__)

@api.route("/api/threats", methods=["GET"])
def get_all_threats():
    rows = get_threats()

    threats = []
    for r in rows:
        threats.append({
            "id": r[0],
            "name": r[1],
            "attack_type": r[2],
            "severity": r[3],
            "confidence": r[4],
            "status": r[5],
            "source_ip": r[6],
            "detected_by": r[7],
            "created_at": r[8]
        })

    return jsonify(threats)
