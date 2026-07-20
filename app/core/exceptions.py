"""
Custom exception hierarchy for the Autonomous AI Agent.

This module defines application-specific exceptions that provide
clear, meaningful error reporting across the project.
"""


class AgentError(Exception):
    """
    Base exception for all application-specific errors.
    """

    pass


class ConfigurationError(AgentError):
    """
    Raised when the application configuration is invalid
    or required settings are missing.
    """

    pass


class ValidationError(AgentError):
    """
    Raised when user input fails validation.
    """

    pass


class LLMError(AgentError):
    """
    Raised when communication with the LLM fails.
    """

    pass


class PlanningError(AgentError):
    """
    Raised when the AI planner fails to generate
    a valid execution plan.
    """

    pass


class ExecutionError(AgentError):
    """
    Raised when execution of a planned task fails.
    """

    pass


class ToolExecutionError(ExecutionError):
    """
    Raised when an external tool or internal utility
    fails during execution.
    """

    pass


class ReflectionError(AgentError):
    """
    Raised when the reflection stage fails.
    """

    pass


class DocumentGenerationError(AgentError):
    """
    Raised when generating or saving a document fails.
    """

    pass
