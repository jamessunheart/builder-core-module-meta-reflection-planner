import datetime

class MetaReflectionPlanner:
    """
    Oversees self-assessment, schedules optimization plans, and aligns them
    with long-term system goals using diagnostic data.
    """

    def __init__(self):
        self.planning_log = []
        self.last_run = None

    def generate_improvement_plan(self, diagnostics_report):
        """
        Create a prioritized plan based on a diagnostics report from self_diagnostic_engine
        """
        now = datetime.datetime.utcnow()
        self.last_run = now
        plan = {
            "timestamp": now.isoformat(),
            "issues": diagnostics_report.get("issues", []),
            "actions": []
        }

        for issue in diagnostics_report.get("issues", []):
            if "permissions" in issue:
                plan["actions"].append("Review and update GitHub token scope.")
            elif "API" in issue:
                plan["actions"].append("Synchronize all API calls with latest OpenAPI spec.")
            elif "fallback" in issue:
                plan["actions"].append("Add new routing rule to task_intent_router.")

        self.planning_log.append(plan)
        return plan

    def get_planning_history(self):
        return self.planning_log