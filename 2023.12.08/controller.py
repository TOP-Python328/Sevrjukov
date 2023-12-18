import model
import view


class Application:
    def __init__(self, model: model, view: view) -> None:
        self.model = model
        self.view = view

    def add(self, n_mail):
        self.new = self.model.Email(n_mail)
        self.new.email = n_mail
    
    def save(self):
        self.model.FileIO.add_email(self.new.__email)

    def loop(self):
        while True:
            n = view.CLI()
            n.output()
            continue
    