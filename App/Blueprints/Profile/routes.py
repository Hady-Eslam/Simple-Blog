from flask import render_template, request, url_for, flash, redirect
from flask_login import current_user, login_required
from App.Blueprints.Profile import profile
from App import db
from .utilits import save_image
from .forms import UpdateAccountForm



@profile.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.image_file.data:
            image = save_image(current_user.image_file, form.image_file.data)
            current_user.image_file = image
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your Profile Updated Successfully', 'success')
        return redirect(url_for('profile.account'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    image_file = url_for('profile.static', filename='profile_pic/' + current_user.image_file)
    return render_template('account.html', title='Account', form=form, image_file=image_file)
