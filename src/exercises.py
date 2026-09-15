sim = [
    {"id": 1, "sistema": "kepler", "excentricidad": 0.1, "pasos": 1000, "ok": True},
    {"id": 2, "sistema": "oscilador", "excentricidad": None, "pasos": 500, "ok": True},
    {"id": 3, "sistema": "kepler", "excentricidad": 0.9, "pasos": 50000, "ok": False},
    {"id": 4, "sistema": "kepler", "excentricidad": 0.5, "pasos": 2000, "ok": True},
    {"id": 5, "sistema": "oscilador", "excentricidad": None, "pasos": 100, "ok": False},
]

id_list = [s["id"] for s in sim]

con_list = [s["id"] for s in sim if s["ok"]]
