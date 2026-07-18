"""
Prompt templates for the Autonomous Document Agent.
"""

from textwrap import dedent


class PromptManager:
    """
    Centralized prompt templates.
    """

    @staticmethod
    def planner_prompt(user_request: str) -> str:
        return dedent(
            f"""
            You are an autonomous document planning agent.

            Your responsibilities are:

            1. Understand the user's request.
            2. Identify the requested document type.
            3. Break the task into logical execution steps.
            4. List assumptions.
            5. Produce an execution plan.

            User Request:

            {user_request}
            """
        ).strip()

    @staticmethod
    def document_prompt(execution_plan: str) -> str:
        return dedent(
            f"""
            You are an expert technical writer.

            Generate a professional document using
            the following execution plan.

            {execution_plan}
            """
        ).strip()

    @staticmethod
    def reflection_prompt(document: str) -> str:
        return dedent(
            f"""
            Review the following document.

            Check for:

            - Missing information
            - Grammar issues
            - Logical consistency
            - Readability
            - Professional tone

            Document:

            {document}
            """
        ).strip()