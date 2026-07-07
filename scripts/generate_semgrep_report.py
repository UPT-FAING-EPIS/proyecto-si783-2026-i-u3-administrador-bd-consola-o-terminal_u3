import json
import html
import os

PATH = "public/semgrep/results.json"


def load_results():
    if not os.path.exists(PATH):
        return []
    try:
        with open(PATH, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("results", [])
    except Exception:
        return []


def build_page(results):
    rows = "".join(
        "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            html.escape(r.get("check_id", "")),
            html.escape(r.get("path", "")),
            r.get("start", {}).get("line", ""),
            html.escape(r.get("extra", {}).get("message", "")),
        )
        for r in results
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Semgrep - Reporte SAST</title>
  <style>
    body {{ font-family: sans-serif; margin: 30px; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccc; padding: 6px 10px; text-align: left; font-size: 14px; vertical-align: top; }}
    th {{ background: #eee; }}
  </style>
</head>
<body>
  <h1>Semgrep &ndash; Hallazgos SAST</h1>
  <p>Total de hallazgos: {len(results)}</p>
  <table>
    <tr><th>Regla</th><th>Archivo</th><th>Linea</th><th>Mensaje</th></tr>
    {rows}
  </table>
</body>
</html>
"""


def main():
    results = load_results()
    os.makedirs("public/semgrep", exist_ok=True)
    with open("public/semgrep/index.html", "w", encoding="utf-8") as f:
        f.write(build_page(results))


if __name__ == "__main__":
    main()
