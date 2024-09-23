from flask import Flask, render_template

app = Flask(__name__)

# Serve home page
@app.route('/')
def index():
    return render_template('index.html')

# Serve diet plan page
@app.route('/diet-plan-page')
def diet_plan_page():
    return render_template('diet-plan.html')

# Serve community page
@app.route('/community-page')
def community_page():
    return render_template('community.html')

# Serve fitness plan page (if needed)
@app.route('/fitness-plan-page')
def fitness_plan_page():
    # Ensure all variables are defined and not None
    workout_data = [30, 45, 60, 40, 50, 70, 65]  # Example data
    body_measurements = [70, 68, 66, 65]         # Example data
    goal_progress = [75, 25]                     # Example data

    # Ensure none of these variables are None by defaulting to empty lists
    return render_template('fitness-plan.html', 
                           workout_data=workout_data or [], 
                           body_measurements=body_measurements or [], 
                           goal_progress=goal_progress or [])

@app.route('/progress-page')
def progress_page():
    # Example dynamic data fetched from the database
    workout_data = [30, 45, 60, 40, 50, 70, 65]  # Workout progress (minutes)
    body_measurements = [70, 68, 66, 65]         # Body weight in kg over 4 weeks
    goal_progress = [75, 25]                     # Percentage of goal completed vs remaining

    # Render the progress page with data
    return render_template('progress.html', 
                            workout_data=workout_data, 
                            body_measurements=body_measurements, 
                            goal_progress=goal_progress)

@app.route('/login-page')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
