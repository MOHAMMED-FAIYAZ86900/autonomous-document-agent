"""
Document template definitions.
"""

from dataclasses import dataclass


@dataclass
class DocumentTemplate:
    """
    Represents a document template.
    """

    title: str
    headings: list[str]


class TemplateManager:
    """
    Provides templates for different
    document types.
    """

    def get_template(
        self,
        document_type: str | None,
    ) -> DocumentTemplate:
        """
        Return a template based on
        document type.
        """

        templates = {

            "proposal": DocumentTemplate(

                title="Project Proposal",

                headings=[

                    "Executive Summary",

                    "Problem Statement",

                    "Objectives",

                    "Proposed Solution",

                    "Implementation Plan",

                    "Timeline",

                    "Budget",

                    "Conclusion",
                ],
            ),

            "report": DocumentTemplate(

                title="Technical Report",

                headings=[

                    "Abstract",

                    "Introduction",

                    "Methodology",

                    "Results",

                    "Discussion",

                    "Conclusion",

                    "References",
                ],
            ),

            "meeting_notes": DocumentTemplate(

                title="Meeting Minutes",

                headings=[

                    "Date",

                    "Attendees",

                    "Agenda",

                    "Discussion",

                    "Action Items",

                    "Next Meeting",
                ],
            ),

            "summary": DocumentTemplate(

                title="Summary",

                headings=[

                    "Overview",

                    "Key Points",

                    "Conclusion",
                ],
            ),
        }

        return templates.get(

            document_type,

            DocumentTemplate(

                title="Generated Document",

                headings=[],
            ),
        )