import os
from importlib import import_module

src_dir = os.listdir("./src")


def compile_tools(tool_dir):
    tool_src_dir = f"./src/{tool_dir}"
    output_tool = ""
    tool_files = os.listdir(tool_src_dir)
    tool_metadata = import_module(f"src.{tool_dir}._tool_metadata")

    common = open(f"{tool_src_dir}/_common.py")
    output_tool += common.read()

    def get_tool_file_code(tool_src_dir, tool_file):
        tool_file_path = f"{tool_src_dir}/{tool_file}.py"
        output_code = f"\n######\n# FILE: {tool_file}\n######\n"
        with open(tool_file_path) as tool:
            for line in tool:
                if line.startswith(("from ", "import ")):
                    continue
                output_code += line
        return output_code

    for tool_file in tool_files:
        if tool_file.startswith("_"):
            continue
        if tool_file.replace(".py", "") not in tool_metadata.INCLUDE:
            raise Exception(f"Tool: {tool_file} in not in the _compile_order INCLUDES")

    for tool_file in tool_metadata.INCLUDE:
        tool_file_contents = get_tool_file_code(tool_src_dir, tool_file)
        output_tool += tool_file_contents

    open(f"./dist/{tool_dir}.py", "w").write(output_tool)


for tool in src_dir:
    compile_tools(tool)
