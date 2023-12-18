import model
import view


class Application:
    def add(self, mail):
        self.new = model.Email(mail)
        self.new.email = mail
    
    def save(self):
        model.FileIO.add_email(self.new.__email)

    def loop(self):
        while True:
            n = input('Почта: ')
            if len(n) > 1:
                view.CLI.output(n)
            else:
                exit()
