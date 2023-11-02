from flask import Flask, render_template, request, redirect, url_for
from app import app, models,forms, db
from .forms import IncomeForm, ExpenditureForm, GoalForm, GoalSearchForm, IncomeDeleteForm
from .models import Income, Expenditure, Goal



#to show total income, expenditure and goal value in home page
@app.route('/')
def home():
    total_income = db.session.query(db.func.sum(Income.value)).scalar()
    total_expenditure = db.session.query(db.func.sum(Expenditure.value)).scalar()
    all_goals = Goal.query.all()
    total_goal_value = sum(goal.value for goal in all_goals)
    return render_template('home.html', total_income=total_income, total_expenditure=total_expenditure, total_goal_value=total_goal_value)

#to calculate all income in the income page
@app.route('/income')
def incomes():
    all_incomes = Income.query.all()
    print(all_incomes)
    return render_template('income.html', all_incomes=all_incomes)

#to calculate all expenditure in the expenditure  page
@app.route('/expenditure')
def expenditures():
    all_expenditures = Expenditure.query.all()
    print(all_expenditures)
    return render_template('expenditure.html', all_expenditures=all_expenditures)

#to show all goals in the  goal page
@app.route('/edit_goal')
def edit_goals():
    all_goals = Goal.query.all()
    print(all_goals)
    return render_template('edit_goal.html', all_goals=all_goals)

@app.route('/add_income', methods=['GET', 'POST'])
def add_income():
    form = IncomeForm()
    # to indicate form has been submitted and validation is used
    if form.validate_on_submit():
        new_income = Income( name=form.name.data, value=form.value.data)
        #add new income record to the database
        db.session.add(new_income)
        print('successfully added')
        #commit changes to database
        db.session.commit()
        return  redirect(url_for ('incomes'))
    #if POST method is mot used, it will render add_income html
    return render_template('income.html',form=form)

@app.route('/add_expenditure', methods=['GET', 'POST'])
def add_expenditure():
    form = ExpenditureForm()
    if form.validate_on_submit():
        new_expenditure = Expenditure( name=form.name.data, value=form.value.data)
        db.session.add(new_expenditure)
        print('successfully added')
        db.session.commit()
        return  redirect(url_for ('expenditures'))
    return render_template('expenditure.html',form=form)

# @app.route('/edit_goal', methods=['GET', 'POST'])
# def edit_goal():
#     form = GoalForm()
#     if form.validate_on_submit():
#         new_goal = Goal( name=form.name.data, value=form.value.data)
#         db.session.add(new_goal)
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template('edit_goal.html', form=form)

# @app.route('/delete_goal', methods=['GET', 'POST'])
# def delete_goal():
#     form = GoalSearchForm()
#     if form.validate_on_submit():
#         Goal.query.filter_by(name=form.name.data).delete()
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template('delete_goal.html', form=form)


@app.route('/delete/<id>',methods = ['GET','POST'])
def delete(id):
    income_data = Income.query.get(int(id))
    db.session.delete(income_data)
    db.session.commit()
    return redirect(url_for('incomes'))

@app.route('/update', methods=['GET', 'POST'])
def update_income():
    if request.method == 'POST':
        my_data = Income.query.get(request.form.get('id'))
        print(request.form)
        my_data.name = request.form['name']
        my_data.value = request.form['value']
        db.session.commit()
        return redirect(url_for('incomes'))
    
@app.route('/insert_income',methods = ['POST'])
def insert_income():
    if request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        #validation when adding income
        if not name:
            return 'Name is required.'
        if not value:
            return 'Value is required.'
        if not value.isdigit():
            return 'Value must be a number and value cannot be negative.'

        # Convert the value to a float if it is valid
        value = float(value)

        # Perform additional validation as needed
        if value < 100:
            return 'Value cannot be too low.'

        # If all details pass, proceed to insert data into the database
        my_data = Income(name=name, value=value)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('incomes'))
    
@app.route('/expenditure/delete/<id>',methods = ['GET','POST'])
def delete_expenditure(id):
    expenditure_data = Expenditure.query.get(int(id))
    db.session.delete(expenditure_data)
    db.session.commit()
    return redirect(url_for('expenditures'))

@app.route('/expenditure/update', methods=['GET', 'POST'])
def update_expenditure():
    if request.method == 'POST':
        my_data = Expenditure.query.get(request.form.get('id'))
        print(request.form)
        my_data.name = request.form['name']
        my_data.value = request.form['value']
        db.session.commit()
        return redirect(url_for('expenditures'))
    
@app.route('/expenditure/insert_expenditure',methods = ['POST'])
def insert_expenditure():
    if request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        #validation for adding expenditure
        if not name:
            return 'Name is required.'
        if not value:
            return 'Value is required.'
        if not value.isdigit():
            return 'Value must be a number and value cannot be a negative number.'

        # Convert the value to a float if it is valid
        value = float(value)

        # Perform additional validation as needed
        if value < 5:
            return 'Value cannot be too low.'

        # If all details pass, proceed to insert data into the database
        my_data = Expenditure(name=name, value=value)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('expenditures'))
    

@app.route('/edit_goal/delete/<id>',methods = ['GET','POST'])
def delete_goal(id):
    goal_data = Goal.query.get(int(id))
    db.session.delete(goal_data)
    db.session.commit()
    return redirect(url_for('edit_goals'))

@app.route('/edit_goal/update', methods=['GET', 'POST'])
def update_goal():
    if request.method == 'POST':
        my_data = Goal.query.get(request.form.get('id'))
        print(request.form)
        my_data.name = request.form['name']
        my_data.value = request.form['value']
        db.session.commit()
        return redirect(url_for('edit_goals'))
    
@app.route('/edit_goal/insert_goal',methods = ['POST'])
def insert_goal():
    if request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        #validation for adding expenditure
        if not name:
            return 'Name is required.'
        if not value:
            return 'Value is required.'
        if not value.isdigit():
            return 'Value must be a number and value cannot be a negative number.'

        # Convert the value to a float if it is valid
        value = float(value)

        # Perform additional validation as needed
        if value < 1000:
            return 'Value cannot be too low.'

        # If all details pass, proceed to insert data into the database
        my_data = Goal(name=name, value=value)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('edit_goal'))
