from dotenv import load_dotenv
load_dotenv('App/.env')


from App import init_app

app = init_app(__name__)
