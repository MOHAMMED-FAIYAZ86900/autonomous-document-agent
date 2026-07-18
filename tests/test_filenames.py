"""
Unit tests for filename generation.
"""

from app.storage.filenames import FilenameGenerator


def test_generate_filename():
    """
    Generated filename should have
    the correct extension.
    """
    filename = FilenameGenerator.generate(
        "Project Proposal"
    )

    assert filename.endswith(".docx")


def test_sanitize():
    """
    Filename should be filesystem-safe.
    """
    result = FilenameGenerator.sanitize(
        "AI / ML Project Proposal"
    )

    assert result == "ai_ml_project_proposal"