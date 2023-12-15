import model


class CLI:
    def __init__(self) -> None:
        self.mail = input('Почта: ')
        self.mod = model.Email(self.mail)

    def output(self):
        self.mod.email = self.mail
        model.FileIO.add_email(self.mod.email)
        print('Успешно')

    
# n = CLI()
# n.output()