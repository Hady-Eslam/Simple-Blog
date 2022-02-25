from dotenv import load_dotenv
load_dotenv('App/.env')



from App import init_app



if __name__ == '__main__':
    app = init_app(__name__)
    app.run(debug=True)
