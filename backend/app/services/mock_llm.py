class MockResponse:

    def __init__(self, text):
        self.content = text


class MockLLM:

    def invoke(self, prompt: str):

        prompt_lower = prompt.lower()


        if "planning agent" in prompt_lower:

            return MockResponse(
                "1. Identify the main concepts and differences.\n"
                "2. Compare the approaches using available evidence.\n"
                "3. Examine their impact on hallucination reduction."
            )


        if "evidence verification agent" in prompt_lower:

            return MockResponse(
                '{'
                '"evidence": ['
                '{'
                '"task": "Development research task",'
                '"claim": "The research workflow collects information from external sources.",'
                '"evidence": "The researcher retrieves information from the configured search tool.",'
                '"source": {'
                '"title": "Development Mock Source",'
                '"url": "https://example.com",'
                '"snippet": "Mock source used during development."'
                '},'
                '"verification": "supported",'
                '"confidence": 0.85'
                '}'
                ']'
                '}'
            )


        if "final research synthesis agent" in prompt_lower:

            return MockResponse(
                "## Executive Summary\n\n"
                "The research workflow analyzed the available evidence "
                "and synthesized the findings.\n\n"

                "## Key Findings\n\n"
                "- Finding generated from collected evidence.\n"
                "- Additional findings require verification from sources.\n\n"

                "## Evidence\n\n"
                "Evidence collected by the research agents is presented here.\n\n"

                "## Sources\n\n"
                "Sources collected through the research process.\n\n"

                "## Limitations\n\n"
                "This report was generated using development-mode mock responses."
            )


        return MockResponse(
            "Development-mode response."
        )


mock_llm = MockLLM()