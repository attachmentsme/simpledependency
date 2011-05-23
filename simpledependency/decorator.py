from simpledependency import dependency_store

def dependency_decorator(klass):
         
    def wrap(*args, **kwargs):
        
        if dependency_store.stored_dependencies.has_key(klass.__name__):
            return dependency_store.stored_dependencies[klass.__name__](*args, **kwargs)
    
        return klass(*args, **kwargs)
    
    wrap.__dict__['___name'] = klass.__name__
    
    return wrap