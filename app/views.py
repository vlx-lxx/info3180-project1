"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import PropertyForm
from werkzeug.utils import secure_filename
from .models import Property
from flask import send_from_directory


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

# Route for displaying the form to add a new property
@app.route('/properties/create', methods=['POST', 'GET'])
def new_property():
    form = PropertyForm()

    if form.validate_on_submit():
        # Get file data and save to your uploads folder
        file = form.photo.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Create new property
        new_property = Property(
            property_title = form.property_title.data,
            property_description = form.property_description.data,
            num_rooms = form.num_rooms.data, 
            num_bathrooms = form.num_bathrooms.data, 
            price = form.price.data, 
            property_type = form.property_type.data, 
            location = form.location.data, 
            photo= filename
        )
        db.session.add(new_property)
        db.session.commit()        
        flash('Property successfully added!', 'success')
        return redirect(url_for('home')) # Update this to redirect the user to a route that displays all uploaded image files
    return render_template('new_property.html', form=form)

# Route for displaying a list of all properties
@app.route('/properties')
def properties():
    # Assuming properties is a list of properties fetched from the database
    properties = Property.query.all()
    # for property in properties:
    #     property.photo_url = url_for('get_image', filename=property.photo)
    return render_template('properties.html', properties=properties)


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'uploads'), filename)


# Route for viewing an individual property by the specific property id
@app.route('/property/<int:property_id>')
def view_property(property_id):
    property = Property.query.get(property_id)
    if property:
        return render_template('view_property.html', property=property)
    else:
        flash('Property not found', 'error')
        return redirect(url_for('home'))

# @app.route('/property/<int:property_id>')
# def property(property_id):
#     # Logic to fetch the property with the given ID from the database
#     property = Property.query.get_or_404(property_id)
#     property.image_url = url_for('send_image', filename=property.image_filename)
#     return render_template('property.html', property=property)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
