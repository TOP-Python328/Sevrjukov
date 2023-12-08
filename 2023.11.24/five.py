from abc import ABC, abstractmethod
from random import randrange as rr, sample
from string import ascii_lowercase as letters

class TestCase:
    """
    Адресат.
    """
    def __init__(self):
        self.messages = [
            ''.join(sample(letters, k=rr(3, 7)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 6))) 
            for _ in range(1000)
        ]
    
    def print_msg(self):
        msg = self.messages.pop()
        print(msg)
    
    def print_nums(self):
        nums = self.numbers.pop()
        print(*nums)
    




class Command(ABC):
    def __init__(self, reciever) -> None:
        self.reciever = reciever

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass 


class CommandCompleter(Command):
   def execute(self):
       return self.reciever.print_msg()

   def undo(self):
       self.reciever.messages.append(self.reciever.messages.pop())


class Chat:
    def __init__(self) -> None:
        self.messages_list = []
        self.undo_list = []

    def execute_command(self, command):
        command.execute()
        self.messages_list.append(command)
        self.undo_list.clear()

    def undo(self):
        if not self.messages_list:
            return 
        last_command = self.messages_list.pop()
        last_command.undo()
        self.undo_list.append(last_command)

    def redo(self):
       if not self.undo_list:
            return
       last_command = self.undo_list.pop()
       last_command.execute()
       self.messages_list.append(last_command)









# test_case = TestCase()
# manager = Chat()

# print_msg_command = CommandCompleter(test_case)
# manager.execute_command(print_msg_command)

# manager.undo()
# manager.redo()




