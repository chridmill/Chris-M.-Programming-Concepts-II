import inspect
import ChrisMiller_ProgrammingExercise_1 # replace with your assignment name (without .py)
#replace docstring_example with your assignment name in the next 2 lines of code
with open("ChrisMiller_ProgrammingExercise_1_design_doc.txt", "w", encoding="utf-8") as doc:
    doc.write(f"# Technical Design Document: {ChrisMiller_ProgrammingExercise_1.__name__}\n\n")
    #replace with your name, the date, and the description of the program
    doc.write(f"# Name: Chris Miller\n")
    doc.write(f"# Date: January 23, 2026\n")
    doc.write(f"# Program Description: A console application to sell up to 20 movie tickets with a limit of 4 per buyer.\n\n")
    #replace docstring_example with your assignment name
    for name, func in inspect.getmembers(ChrisMiller_ProgrammingExercise_1, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")
        #replace with link to your repository
        doc.write(f"#Link to your repository: https://github.com/chridmill/Chris-M.-Programming-Concepts-II")
print('Complete')
