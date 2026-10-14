
from collections import Counter
from pathlib import Path


def analyze_logs(file_path):
    counts = Counter()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            for level in ["INFO", "WARNING", "ERROR"]:
                if level in line.upper():
                    counts[level] += 1
                    break

    return counts


def application_health(counts):
    return "ATTENTION" if counts.get("ERROR", 0) > 0 else "NORMAL"


def main():
    log_file = Path("app.log")

    if not log_file.exists():
        log_file.write_text(
            "INFO Application started\n"
            "INFO Request processed\n"
            "WARNING Slow response\n"
            "ERROR Database failed\n",
            encoding="utf-8"
        )

    counts = analyze_logs(log_file)

    print("===== LOG ANALYSIS REPORT =====")
    print("INFO:", counts["INFO"])
    print("WARNING:", counts["WARNING"])
    print("ERROR:", counts["ERROR"])
    print("Total Logs:", sum(counts.values()))
    print("Application Health:", application_health(counts))


if __name__ == "__main__":
    main()

