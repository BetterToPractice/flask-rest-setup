import importlib.util
import os

import pluggy as pluggy_core
from flask import Flask
from pluggy import HookimplMarker


def get_modules(directory_path, location_dir):
    module_names = {}
    project_name = os.path.basename(directory_path)

    for root, _, files in os.walk(directory_path / location_dir):
        for filename in files:
            if filename.endswith(".py"):
                module_name = os.path.splitext(filename)[0]  # Remove the ".py" extension
                full_module_name = os.path.relpath(os.path.join(root, module_name), directory_path).replace(
                    os.path.sep, "."
                )
                module_names[full_module_name] = load_module_by_name(f"{project_name}.{full_module_name}")

    return module_names


def load_module_by_name(module_name):
    spec = importlib.util.find_spec(module_name)
    if spec:
        custom_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(custom_module)
        return custom_module
    else:
        return None


class Plugin:
    def __init__(self):
        self.plugin_name = None
        self.pm = None

    def init_app(self, app: Flask, plugin_name="plugins", hook_specs=None, apps_paths="apps") -> None:
        self.plugin_name = plugin_name
        self.pm = pluggy_core.PluginManager(self.plugin_name)

        if hook_specs:
            self.pm.add_hookspecs(hook_specs)
        for module_name, module in get_modules(app.config["APP_DIR"], apps_paths).items():
            self.pm.register(module, module_name)

        app.extensions["plugin"] = self.pm

    def get_impl(self):
        return HookimplMarker(self.plugin_name)
