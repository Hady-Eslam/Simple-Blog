from flask import current_app
from PIL import Image
import secrets, os



def save_image(old_user_image, form_image):
    new_file_name = secrets.token_hex(10)
    _, ext = os.path.splitext(form_image.filename)
    new_file_path = os.path.join(
        current_app.root_path,
        'App', 'Blueprints', 'Profile', 'static', 'Profile', 'profile_pic',
        new_file_name + ext
    )
    if old_user_image != 'default.png':
        os.remove(
            os.path.join(
                current_app.root_path,
                'App', 'Blueprints', 'Profile', 'static', 'Profile', 'profile_pic',
                old_user_image
            )
        )

    i = Image.open(form_image)
    i.thumbnail((125, 125))
    i.save(new_file_path)

    return new_file_name + ext
