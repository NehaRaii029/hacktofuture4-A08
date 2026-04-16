# def detect_anomaly(signals):
#     if signals["cpu"] > 90:
#         return True
#     if signals["memory"] > 90:
#         return True
#     if signals["restarts"] > 3:
#         return True
#     if signals["latency"] > 2000:
#         return True
#     return False

# anomaly_engine/rule_detector.py

def detect_anomaly(signals):
    return True