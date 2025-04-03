# import os
# from dotenv import load_dotenv
# load_dotenv()
# from openai import OpenAI                     # Import OpenAI API 
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from create_graph import build_dependency_graph
# from level_segregation import segregate_levels

# def compute_reverse_dependencies(dependencies):
#     """Invert dependency dict to map a parent file to a list of (child, functions)."""
#     reverse_deps = {}
#     for child, mapping in dependencies.items():
#         for parent, funcs in mapping.items():
#             reverse_deps.setdefault(parent, []).append((child, funcs))
#     return reverse_deps

# def document_node(node, level, inherited_context, reverse_deps):
#     """Generate a markdown documentation file for a given node and obtain function summary via LLM."""
#     doc_lines = [f"# Documentation for {node}",
#                  f"**Level:** {level}",
#                  ""]
#     if inherited_context:
#         doc_lines.append("## Inherited Context:")
#         for ctx in inherited_context:
#             doc_lines.append(f"- {ctx}")
#         doc_lines.append("")
#     if node in reverse_deps:
#         doc_lines.append("## Dependent Nodes Import Summary:")
#         for dep, funcs in reverse_deps[node]:
#             funcs_list = ", ".join(funcs) if funcs else "module import"
#             doc_lines.append(f"- Dependent: {dep} imports [{funcs_list}]")
#     else:
#         doc_lines.append("*(No dependent nodes importing from this file)*")
    
#     # Call OpenAI API to generate a function summary only (not appended in the markdown)
#     prompt = f"Generate a concise function summary for file {node} based on the context below:\n" + "\n".join(doc_lines)
#     client = OpenAI()
#     client.api_key = os.getenv("OPENAI_API_KEY")
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     llm_summary = response.choices[0].message.content.strip()
    
#     # Write the markdown documentation WITHOUT the function summary
#     docs_dir = os.path.join(os.getcwd(), "docs")
#     os.makedirs(docs_dir, exist_ok=True)
#     doc_path = os.path.join(docs_dir, f"{node}.md")
#     with open(doc_path, "w", encoding="utf-8") as f:
#         f.write("\n".join(doc_lines))
    
#     # Return both documentation status and the generated function summary
#     return {"node": node, "msg": f"Documented {node}", "func_summary": llm_summary}

# def process_level(nodes, level, reverse_deps, inherited_contexts):
#     """Process all nodes at a given level in parallel.
#        inherited_contexts: dict mapping node -> list of inherited context strings.
#     """
#     results = []
#     with ThreadPoolExecutor() as executor:
#         future_to_node = {
#             executor.submit(document_node, node, level, inherited_contexts.get(node, []), reverse_deps): node 
#             for node in nodes
#         }
#         for future in as_completed(future_to_node):
#             results.append(future.result())
#     return results

# def document_project(project_root):
#     """Main function to build docs across levels."""
#     dep_graph = build_dependency_graph(project_root)
#     levels, dependencies = segregate_levels(dep_graph)
#     reverse_deps = compute_reverse_dependencies(dependencies)
#     inherited_contexts = {}
#     # Process levels in order (lowest level first)
#     for lvl in sorted(levels.keys()):
#         print(f"Processing level {lvl} ...")
#         nodes = levels[lvl]
#         results = process_level(nodes, lvl, reverse_deps, inherited_contexts)
#         for res in results:
#             print(res["msg"])
#         # Use the LLM-generated function summary as context for dependent higher-level nodes
#         for res in results:
#             node = res["node"]
#             summary = res["func_summary"]
#             for child, mapping in reverse_deps.get(node, []):
#                 inherited_contexts.setdefault(child, []).append(summary)
#     print("Documentation generation complete.")

# if __name__ == "__main__":
#     prj_root = input("Enter project root directory: ").strip()
#     if os.path.isdir(prj_root):
#         document_project(prj_root)
#     else:
#         print("Invalid project root directory.")




