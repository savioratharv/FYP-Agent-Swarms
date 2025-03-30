from create_graph import build_dependency_graph, visualize_dependency_graph
from level_segregation import segregate_levels
import os

def main():
    project_root = input("Enter the project root directory: ").strip()
    if not os.path.isdir(project_root):
        print("Invalid directory. Please check the path.")
        return
    graph = build_dependency_graph(project_root)
    print("Nodes:", graph.nodes)
    print("Edges:", graph.edges)
    visualize_dependency_graph(graph)

    print(graph)

    # Get Levels
    levels, dependencies = segregate_levels(graph)

    # Print Levels
    for level, nodes in sorted(levels.items()):
        print(f"Level {level}: {nodes}")

    print("Dependencies:", dependencies)


if __name__ == "__main__":
    main()
