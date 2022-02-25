from flask import render_template, request
from App.Blueprints.Posts.models import Posts
from App.Blueprints.Main import main




@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('home.html', posts=posts)



@main.route('/about')
def about():
    return render_template('about.html', title='About Page')
