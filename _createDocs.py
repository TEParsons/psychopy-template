from pathlib import Path
from docs.utils import createModuleDocs, createComponentDocs

# Get source folder
src = Path(__file__).parent / "docs"

# List all modules in this plugin
from template_package import template_module
modules = (template_module, )

# Generate an rst file for each module
for module in modules:
    content = createModuleDocs(module)
    name = module.__name__.split(".")[-1]
    with open(str(src / (name + ".rst")), "w") as f:
        f.write(content)

# List all components in this plugin
from template_package import template_component
components = (template_component.TemplatePluginComponent, )

# Generate an rst file for each component
for comp in components:
    content = createComponentDocs(comp)
    with open(str(src / (comp.__name__ + ".rst")), "w") as f:
        f.write(content)