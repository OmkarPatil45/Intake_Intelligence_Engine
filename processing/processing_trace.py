from datetime import datetime
import time


class ProcessingTrace:
    def __init__(self):

        self.steps = []

    def add_step(
        self,
        step_name,
        status,
        details
    ):

        self.steps.append({

            "timestamp":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "step":
                step_name,

            "status":
                status,

            "details":
                details
        })

    def get_trace(self):

        return self.steps

    def get_human_readable_trace(
        self
    ):

        lines = []

        for step in self.steps:

            lines.append(

                f"[{step['status']}] "
                f"{step['step']} "
                f"→ "
                f"{step['details']}"
            )

        return "\n".join(lines)

    def get_summary(self):

        total = len(self.steps)

        success = len(

            [
                step
                for step
                in self.steps

                if step["status"]
                == "SUCCESS"
            ]
        )

        return {

            "total_steps":
                total,

            "successful_steps":
                success,

            "overall_status":
                (
                    "SUCCESS"
                    if total == success
                    else "PARTIAL"
                )
        }
    

    def replay_trace(
        self,
        delay=0.3
    ):

        total = len(self.steps)

        for index, step in enumerate(
            self.steps,
            start=1
        ):

            print(
                f"[{index}/{total}] "
                f"{step['step']}",
                end="",
                flush=True
            )

            for _ in range(3):

                time.sleep(delay)

                print(
                    ".",
                    end="",
                    flush=True
                )

            print(
                f" DONE"
            )

            print(
                f"    {step['details']}"
            )

            print()
        
