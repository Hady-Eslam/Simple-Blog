from flask import render_template, request, url_for, flash, redirect, abort
from flask_login import current_user, login_required
from App.Blueprints.Authentication.models import User
from App.Blueprints.Posts import posts
from App import db
from .models import Posts
from .forms import CreatePostForm, UpdatePostForm



@posts.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Post Created Successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Create New Post', form=form, legend='Create New Post')


@posts.route('/posts/<int:post_id>')
def post(post_id):
    post = Posts.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/posts/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Posts.query.get(post_id)
    if current_user != post.author:
        abort(403)
    
    form = UpdatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Post Updated Successfully', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Posts.query.get(post_id)
    if current_user != post.author:
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.home'))


@posts.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Posts.query\
        .filter_by(author=user)\
            .order_by(Posts.date_posted.desc())\
                .paginate(per_page=5, page=page)
    return render_template('user_posts.html', title=user.username, posts=posts, user=user)
