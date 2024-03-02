from flask import Flask, redirect, render_template, flash, url_for

from models import Pet, db, connect_db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


@app.route('/')
def pets_home():
    """List pets on homepage"""
    pets = Pet.query.all()
    return render_template('pets_home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show form to add a pet and submit to db if validations met"""
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.itmes() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added!")
        return redirect(url_for('pets_home'))
    else:
        flash(f"Error adding pet, make sure all required fields are filled out.")
        return render_template('/add_pet_form.html', form=form)
    
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit selected pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} has been updated")
        return redirect(url_for('pets_home'))
    else:
        flash(f"Pet update failed")
        return render_template('edit_pet_form.html', form=form, pet=pet)
    