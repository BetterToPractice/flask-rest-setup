from pluggy import HookspecMarker

specs = HookspecMarker("plugins")


@specs
def load_routes(app):
    ...
