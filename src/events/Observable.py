'''
<description>
    Observable class that is an abstract class.
</description>
'''
from events.DungeonEvent import DungeonEvent


class Observable:
    '''
    <description>
        Observable class that is an abstract class.
    </description>
    <return> None </return>
    '''
    def __init__(self):
        self.observers = []
    
    '''
    <description>
        Method to register an observer.
    </description>
    <param name=observer> Observer object. </param>
    <return> None </return>
    '''
    def register(self, observer):
        self.observers.append(observer)
    
    '''
    <description>
        Method to unregister an observer.
    </description>
    <param name=observer> Observer object. </param>
    <return> None </return>
    '''
    def unregister(self, observer):
        self.observers.remove(observer)
    
    '''
    <description>
        Method to notify all the observers.
    </description>
    <param name=message> Message to notify the observers. </param>
    <return> None </return>
    '''
    def notify(self, event: DungeonEvent):
        for observer in self.observers:
            observer.update(event)
