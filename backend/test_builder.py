from app.agents.architect import ArchitectAgent
from app.core.project_builder import ProjectBuilder



task = """
создай калькулятор
с интерактивными графиками
"""


architect = ArchitectAgent()


architecture = architect.analyze_project(
    task
)


print("ARCHITECTURE:")
print(architecture)



builder = ProjectBuilder()


result = builder.create_project(
    architecture
)


print(result)
