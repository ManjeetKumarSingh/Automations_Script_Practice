import logging
from datetime import datetime
import traceback
from typing import List, Dict, Any, Optional

logging.basicConfig(
    filename="task_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def perform_task(taks, function, *args, **kwargs):
    """Perform a task and log its status.
    Args:
        taks (str): The name of the task.
        function (callable): The function to execute for the task."""

    try:
        logging.info(f"Starting task: {taks}")
        result = function(*args, **kwargs)
        logging.info(f"Task {taks} completed successfully.")
        return result
    except Exception as e:
        logging.error(f"Error occurred while performing task {taks}: {e}")
        logging.error(traceback.format_exc())
        return None


# Example tasks
def clean_temp_files():
    # Simulate success
    print("Cleaning temporary files...")
    return "Cleaned successfully"


def sync_data():
    # Simulate failure
    raise ConnectionError("Unable to connect to server")


tsks = [
    {"name": "Clean Temp Files", "function": clean_temp_files},
    {"name": "Sync Data", "function": sync_data},
]

if __name__ == "__main__":
    for task in tsks:
        perform_task(task["name"], task["function"])
