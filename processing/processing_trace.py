from datetime import datetime
import time


class ProcessingTrace:
    def __init__(self):
        self.execution_timestamp=(
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        self.overall_status = "SUCCESS"

        self.steps = []

    def add_step(self, step_name, details):

        self.steps.append({
            "step":step_name,
            "details":details
        })

    def get_trace(self):
        return {

            "execution_timestamp":self.execution_timestamp,
            "overall_status":self.overall_status,
            "processing_trace":self.steps
        }

    def get_human_readable_trace(self):

        lines = []

        for step in self.steps:
            lines.append(
                f"{step['step']} "
                f"→ "
                f"{step['details']}"
            )
        return "\n".join(lines)

    def get_summary(self):
        return {
            "execution_timestamp":self.execution_timestamp,
            "overall_status":self.overall_status,
            "total_steps":len(self.steps)
        }

    def replay_trace(self,delay=0.1):

        total = len(self.steps)

        for index, step in enumerate(self.steps,start=1):
            print(
                f"[{index}/{total}] "
                f"{step['step']}",
                end="", flush = True
            )

            for _ in range(3):
                time.sleep(delay)
                print(".",end="",flush=True)

            print(f" DONE")
            print(f"{step['details']}")
            print()
        