from core.setup import create_app

app = create_app(__name__)

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=True)
