
from log_analyzer import analyze_logs, application_health


def test_log_analysis(tmp_path):
    file = tmp_path / "test.log"

    file.write_text(
        "INFO Started\n"
        "WARNING Slow response\n"
        "ERROR Failed\n"
        "INFO Completed\n",
        encoding="utf-8"
    )

    counts = analyze_logs(file)

    assert counts["INFO"] == 2
    assert counts["WARNING"] == 1
    assert counts["ERROR"] == 1


def test_health_with_errors():
    assert application_health({"ERROR": 1}) == "ATTENTION"


def test_health_without_errors():
    assert application_health({"ERROR": 0}) == "NORMAL"
