
from pathlib import Path
import pandas as pd


def find_project_root():
    """Find the project folder automatically."""

    current_folder = Path(__file__).resolve().parent

    for folder in [current_folder, *current_folder.parents]:
        if (folder / "data" / "raw").is_dir():
            return folder

    raise FileNotFoundError(
        "Project folder not found. "
        "Please check the data/raw folder."
    )


def load_project_csv(file_name):
    """Load a CSV file from the project's raw data folder."""

    project_root = find_project_root()
    file_path = project_root / "data" / "raw" / file_name

    if not file_path.is_file():
        raise FileNotFoundError(
            f"CSV file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def require_columns(data, required_columns, file_name):
    """Check whether required columns exist."""

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"{file_name} is missing columns: "
            f"{missing_columns}"
        )



def save_report(data, file_name):
    """Save a report in the project's reports folder."""

    if Path(file_name).name != file_name:
        raise ValueError(
            "Please provide only a file name, not a folder path."
        )

    project_root = find_project_root()
    report_folder = project_root / "reports"
    report_folder.mkdir(parents=True, exist_ok=True)

    report_path = report_folder / file_name
    data.to_csv(report_path, index=False)

    print(f"Report saved: {report_path}")

