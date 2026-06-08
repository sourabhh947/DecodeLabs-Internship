from bot import show_banner, process


def run():
    show_banner()

    while True:
        raw_input = input("You: ")
        keep_running = process(raw_input)

        if not keep_running:
            break


if __name__ == "__main__":
    run()