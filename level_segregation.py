import networkx as nx

def segregate_levels(graph):
    """Segregate nodes into levels based on dependencies and return dependency mapping."""
    levels = {}  # Dictionary to store node levels
    dependencies = {}  # Dictionary to store dependencies per file
    level = 0

    # Start with leaf nodes (no outgoing edges)
    current_level_nodes = {node for node in graph.nodes if graph.in_degree(node) == 0}

    while current_level_nodes:
        levels[level] = current_level_nodes
        next_level_nodes = set()

        # Find nodes that point to the current level and store dependencies
        for node in graph.nodes:
            if node not in levels:
                children = {child for child in graph.predecessors(node) if child in current_level_nodes}
                if children:
                    next_level_nodes.add(node)
                    dependencies[node] = dependencies.get(node, set()) | children

        current_level_nodes = next_level_nodes
        level += 1

    return levels, dependencies
