from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os
import re
from typing import List

# Load environment variables
load_dotenv()

class LLMHelper:
    """Handles communication with Hugging Face LLM"""
    def __init__(self):
        self.client = InferenceClient(
            model=os.getenv("HF_MODEL", "HuggingFaceH4/zephyr-7b-beta"),
            token=os.getenv("HF_TOKEN")
        )

    def generate_text(self, prompt: str, max_tokens: int = 500) -> str:
        """Generate text from the LLM"""
        try:
            response = self.client.text_generation(
                prompt,
                max_new_tokens=max_tokens,
                temperature=0.7,
                do_sample=True
            )
            return response.strip()
        except Exception as e:
            print(f"[LLM Error] {e}")
            return ""

def parse_tech_stack(input_str: str) -> List[str]:
    """Clean and normalize a free-form tech stack input into a list"""
    if not input_str.strip():
        return []

    # Normalize common shorthand
    replacements = {
        "c#": "C#",
        "c++": "C++",
        "f#": "F#",
        "golang": "Go",
        "js": "JavaScript",
        "ts": "TypeScript"
    }

    # Split by comma, semicolon, slash, or newline
    techs = re.split(r'[,;/\n]', input_str)
    cleaned = []

    for tech in techs:
        tech = tech.strip().lower()
        if tech:
            tech = replacements.get(tech, tech)
            if not re.match(r'^[a-z0-9+#]+$', tech):
                tech = tech.title()
            if tech not in cleaned and len(tech) > 1:
                cleaned.append(tech)

    return cleaned

def generate_tech_questions(tech_stack: List[str], years_experience: int) -> List[str]:
    """Generate 3 technical questions per tech based on experience"""
    if not tech_stack:
        return ["Please describe your technical experience."]

    llm = LLMHelper()
    difficulty = (
        "beginner" if years_experience < 2 else
        "intermediate" if years_experience < 5 else
        "advanced"
    )

    questions = []

    for tech in tech_stack:
        prompt = f"""Generate exactly 3 technical questions about {tech} for a candidate with {years_experience} years of experience.
Difficulty level: {difficulty}
Format each question clearly numbered like:
1. [Question about {tech}]
2. [Question about {tech}]
3. [Question about {tech}]

The questions should:
- Be technical and specific to {tech}
- Cover different aspects (syntax, architecture, debugging)
- Require detailed answers
- Avoid simple yes/no or one-word answers
"""

        response = llm.generate_text(prompt)

        tech_questions = []
        for line in response.split('\n'):
            line = line.strip()
            if line and line[0].isdigit() and any(c in line for c in ['.', ')']):
                question = line.split('.', 1)[-1].split(')', 1)[-1].strip()
                if question.startswith('[') and question.endswith(']'):
                    question = question[1:-1].strip()
                if question:
                    tech_questions.append(f"{tech}: {question}")

        default_questions = [
            f"{tech}: Explain the most challenging {tech} project you've worked on.",
            f"{tech}: How would you handle performance optimization in {tech}?",
            f"{tech}: Describe a debugging strategy in {tech} you used recently."
        ]

        questions.extend(tech_questions[:3] if len(tech_questions) >= 3 else default_questions)

    return questions
