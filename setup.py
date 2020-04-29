import os
import re

# TODO: update this explanation
# while ArcGIS Pro can decipher packages, it doesn't refresh automatically when developing
# that's why we need to use a single .pyt file
# this is used to create the .pyt, transfering all tools to single .pyt file...

pyt_path = os.path.join('output', 'African Parks Python Toolbox.pyt')
tools_dir = os.path.join('src', 'tools')

# get toolbox code
with open('src/toolbox.py', 'r') as f:
    toolbox_code = f.read()

# get toolbox imports and remove them from toolbox code
toolbox_imports = re.findall(r'(^import .*|^from .*)$', toolbox_code, flags=re.MULTILINE)
for ti in toolbox_imports:
    toolbox_code = toolbox_code.replace(ti + '\n', '')

# for each file in tools/ add
ignore_files = ['__init__.py']
tool_files = [f for f in os.listdir(tools_dir) if f not in ignore_files]
for file_name in tool_files:

    # get tool code
    with open(os.path.join(tools_dir, file_name), 'r') as f:
        tool_code = f.read()

    # get tool imports and remove them from tool code
    tool_imports = re.findall(r'(^import .*|^from .*)$', tool_code, flags=re.MULTILINE)
    for ti in tool_imports:
        tool_code = tool_code.replace(f'{ti}\n', '')

    # replace stub in toolbox with tool code
    tool_name = file_name.replace('.py', '')
    toolbox_code = toolbox_code.replace(f'{tool_name} = object\n', tool_code.strip())

    # add combined imports to toolbox code
    imports = set(toolbox_imports + tool_imports)
    for _import in imports:
        toolbox_code = f'{_import}\n' + toolbox_code

# write toolbox code to .pyt file
with open(pyt_path, 'w') as f:
    f.write(toolbox_code)

