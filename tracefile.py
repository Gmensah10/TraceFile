import os
import csv
from datetime import datetime
import argparse
import matplotlib.pyplot as plt


def generate_visual_timeline(timeline):
    # Debugging: Check if timeline has entries
    if not timeline:
        print("No data to visualize. Timeline is empty.")
        return

    created_times = [entry["Created"] for entry in timeline]
    modified_times = [entry["Modified"] for entry in timeline]
    accessed_times = [entry["Accessed"] for entry in timeline]

    # Debugging: Print collected timestamps
    print(f"Created times: {created_times}")
    print(f"Modified times: {modified_times}")
    print(f"Accessed times: {accessed_times}")

    plt.figure(figsize=(10, 6))
    plt.scatter(created_times, [1] * len(created_times), color="green", label="Created")
    plt.scatter(
        modified_times, [2] * len(modified_times), color="blue", label="Modified"
    )
    plt.scatter(
        accessed_times, [3] * len(accessed_times), color="red", label="Accessed"
    )

    plt.yticks([1, 2, 3], ["Created", "Modified", "Accessed"])
    plt.xlabel("Timestamp")
    plt.title("Forensic Timeline")
    plt.legend()
    plt.tight_layout()
    plt.show()


class ForensicTimelineGenerator:
    def __init__(
        self, target_dir, output_file, start_date=None, end_date=None, file_types=None
    ):
        self.target_dir = target_dir
        self.output_file = output_file
        self.start_date = datetime.fromisoformat(start_date) if start_date else None
        self.end_date = datetime.fromisoformat(end_date) if end_date else None
        self.file_types = file_types if file_types else []

    def collect_file_metadata(self):
        timeline = []
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if self.file_types and not file.endswith(tuple(self.file_types)):
                    continue
                try:
                    stats = os.stat(file_path)
                    created = datetime.fromtimestamp(stats.st_ctime)
                    modified = datetime.fromtimestamp(stats.st_mtime)
                    accessed = datetime.fromtimestamp(stats.st_atime)

                    # Debugging: Print file metadata being added
                    print(f"Processing file: {file_path}")
                    print(f"Created: {created}, Modified: {modified}, Accessed: {accessed}")

                    if self.start_date and (created < self.start_date):
                        continue
                    if self.end_date and (created > self.end_date):
                        continue

                    timeline.append(
                        {
                            "File Path": file_path,
                            "Created": created,
                            "Modified": modified,
                            "Accessed": accessed,
                        }
                    )
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
        # Debugging: Print the timeline after processing
        print(f"Collected timeline: {timeline}")
        return timeline

    def save_to_csv(self, timeline):
        try:
            with open(self.output_file, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=["File Path", "Created", "Modified", "Accessed"]
                )
                writer.writeheader()
                for entry in timeline:
                    writer.writerow(
                        {
                            "File Path": entry["File Path"],
                            "Created": entry["Created"].isoformat(),
                            "Modified": entry["Modified"].isoformat(),
                            "Accessed": entry["Accessed"].isoformat(),
                        }
                    )
        except IOError as e:
            print(f"Failed to save CSV file: {e}")

    def run(self):
        print(f"Scanning directory: {self.target_dir}")
        timeline = self.collect_file_metadata()
        print(f"Collected metadata for {len(timeline)} files.")

        print(f"Saving timeline to {self.output_file}...")
        self.save_to_csv(timeline)
        print("Timeline saved successfully.")

        print("Generating visual timeline...")
        generate_visual_timeline(timeline)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a forensic timeline from file metadata."
    )
    parser.add_argument("target_dir", help="Directory to scan for files.")
    parser.add_argument("output_file", help="Path to save the CSV timeline.")
    parser.add_argument(
        "--start_date",
        help="Filter files created after this date (YYYY-MM-DD).",
        default=None,
    )
    parser.add_argument(
        "--end_date",
        help="Filter files created before this date (YYYY-MM-DD).",
        default=None,
    )
    parser.add_argument(
        "--file_types",
        nargs="+",
        help="List of file extensions to include (e.g., .txt .jpg).",
        default=None,
    )
    parser.add_argument(
        "--test_data_dir", help="Directory to create test data.", default="test_data"
    )

    args = parser.parse_args()

    generator = ForensicTimelineGenerator(
        target_dir=args.target_dir,
        output_file=args.output_file,
        start_date=args.start_date,
        end_date=args.end_date,
        file_types=args.file_types,
    )
    generator.run()

    # Sample Test Data
    if not os.path.exists(args.test_data_dir):
        os.makedirs(args.test_data_dir)
        with open(os.path.join(args.test_data_dir, "sample1.txt"), "w") as f:
            f.write("Sample file 1.")
        with open(os.path.join(args.test_data_dir, "sample2.txt"), "w") as f:
            f.write("Sample file 2.")
        with open(os.path.join(args.test_data_dir, "sample3.txt"), "w") as f:
            f.write("Sample file 2.")
