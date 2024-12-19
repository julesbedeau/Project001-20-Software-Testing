from graphviz import Digraph

# Create a workflow diagram using Graphviz
workflow_diagram = Digraph("Bug_Lifecycle", format="png")

# Add nodes representing the states of the bug lifecycle
workflow_diagram.node("Open", "Open", shape="ellipse", style="filled", fillcolor="lightblue")
workflow_diagram.node("Assigned", "Assigned", shape="ellipse", style="filled", fillcolor="lightblue")
workflow_diagram.node("In Progress", "In Progress", shape="ellipse", style="filled", fillcolor="lightblue")
workflow_diagram.node("Ready for Testing", "Ready for Testing", shape="ellipse", style="filled", fillcolor="lightblue")
workflow_diagram.node("Verified", "Verified", shape="ellipse", style="filled", fillcolor="lightblue")
workflow_diagram.node("Closed", "Closed", shape="ellipse", style="filled", fillcolor="lightgreen")
workflow_diagram.node("Reopen", "Reopen", shape="ellipse", style="filled", fillcolor="lightcoral")

# Add edges representing transitions between states
workflow_diagram.edges([
    ("Open", "Assigned"),
    ("Assigned", "In Progress"),
    ("In Progress", "Ready for Testing"),
    ("Ready for Testing", "Verified"),
    ("Verified", "Closed"),
    ("Ready for Testing", "Reopen"),
    ("Reopen", "In Progress")
])

# Save the diagram to a file
diagram_path = "/mnt/data/Bug_Lifecycle_Workflow"
workflow_diagram.render(diagram_path, format="png", cleanup=True)

diagram_path + ".png"
