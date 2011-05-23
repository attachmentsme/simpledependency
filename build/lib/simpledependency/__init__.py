from simpledependency.dependency_store import DependencyStore
dependency_store = DependencyStore()

from simpledependency.decorator import dependency_decorator

def override_dependency(original_class=None, replacement_class=None):
    if original_class.__dict__.has_key('___name'):
        dependency_store.stored_dependencies[original_class.___name] = replacement_class
    else:
        raise Exception('You must wrap a class in the dependency_decorator to override it.')