from src.app import Application

def main():
    app = Application()
    app.run(host="localhost", port=4000, debug=True, load_dotenv=True)

if __name__ == '__main__':
    main()
