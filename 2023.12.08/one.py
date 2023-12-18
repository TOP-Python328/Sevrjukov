import model
import view
import controller


def main():
    m = model.FileIO()
    v = view.CLI
    c = controller.Application(m, v)

    c.loop()

if __name__ == "__main__":
    main()