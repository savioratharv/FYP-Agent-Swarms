import os

import os
import ast
import sys
import pkg_resources
import networkx as nx
import matplotlib.pyplot as plt

def get_python_files(root_dir):
    """Recursively get all Python files in a project."""
    py_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                py_files.append(os.path.relpath(os.path.join(dirpath, filename), root_dir))
    return py_files

def extract_imports(file_path):
    """Extract import statements from a Python file."""
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    
    return imports

def is_internal_import(import_name, project_files, project_root):
    """Check if the import is internal (i.e., part of the project)."""
    # Convert import name to a relative path
    import_path = import_name.replace(".", os.sep) + ".py"
    if import_path in project_files:
        return True

    # Check for module directories (e.g., package/module structure)
    for file in project_files:
        if file.startswith(import_name.replace(".", os.sep) + os.sep):
            return True

    return False

def build_dependency_graph(root_dir):
    """Construct a dependency graph for the project."""
    project_files = get_python_files(root_dir)
    project_files_set = set(project_files)

    # Get list of standard library modules
    stdlib_modules = set(sys.builtin_module_names)

    # Get installed third-party libraries
    installed_packages = set(pkg.key for pkg in pkg_resources.working_set)

    # Create a directed graph
    dep_graph = nx.DiGraph()

    for file in project_files:
        file_path = os.path.join(root_dir, file)
        imports = extract_imports(file_path)

        for imp in imports:
            if imp in stdlib_modules or imp in installed_packages:

                continue  # Ignore standard lib and third-party imports
            
            if is_internal_import(imp, project_files_set, root_dir):
                dep_graph.add_edge(imp.replace(".", os.sep) + ".py", file)

    return dep_graph

def visualize_dependency_graph(graph):
    """Visualize the dependency graph using matplotlib and networkx."""
    plt.figure(figsize=(10, 6))

    pos = nx.spring_layout(graph, seed=42)  # Position nodes using spring layout
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10, font_weight="bold", arrows=True)

    plt.title("Python Project Dependency Graph")
    plt.savefig("dependency_graph.png")
