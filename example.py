from simpledependency import override_dependency
from simpledependency import dependency_decorator
        
@dependency_decorator
class Example(object):
    
    def __init__(self):
        print 'Example class called.'
        
class MockExample(object):
    
    def __init__(self):
        print 'Mock example class called.'

example = Example()
override_dependency(original_class=Example, replacement_class=MockExample)
example = Example()