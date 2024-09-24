from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Existing Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diet-plan-page')
def diet_plan_page():
    return render_template('diet-plan.html')

@app.route('/fitness-plan-page')
def fitness_plan_page():
    workout_data = [30, 45, 60, 40, 50, 70, 65]
    body_measurements = [70, 68, 66, 65]
    goal_progress = [75, 25]
    return render_template('fitness-plan.html', workout_data=workout_data, body_measurements=body_measurements, goal_progress=goal_progress)

@app.route('/progress-page')
def progress_page():
    workout_data = [30, 45, 60, 40, 50, 70, 65]
    body_measurements = [70, 68, 66, 65]
    goal_progress = [75, 25]
    return render_template('progress.html', workout_data=workout_data, body_measurements=body_measurements, goal_progress=goal_progress)

@app.route('/login-page')
def login_page():
    return render_template('login.html')

@app.route('/signup-page')
def signup_page():
    return render_template('signup.html')

# Blog-related routes
posts = [
    {
        'id': 1,
        'title': 'My Fitness Journey',
        'content': 'Started my fitness journey with Calorie Crush. The personalized plan is amazing!',
        'author': 'John Doe',
        'comments': [{'author': 'Jane', 'comment': 'Great work! Keep going!'}]
    }
]

next_post_id = 2  # For generating post IDs

@app.route('/community-page')
def community_page():
    return render_template('community.html', posts=posts)

@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    global next_post_id
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        new_post = {
            'id': next_post_id,
            'title': title,
            'content': content,
            'author': author,
            'comments': []
        }
        posts.append(new_post)
        next_post_id += 1
        return redirect(url_for('community_page'))
    return render_template('create-post.html')

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post-detail.html', post=post)
    return "Post not found", 404

@app.route('/add-comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    author = request.form['author']
    comment = request.form['comment']
    for post in posts:
        if post['id'] == post_id:
            post['comments'].append({'author': author, 'comment': comment})
            break
    return redirect(url_for('post_detail', post_id=post_id))

if __name__ == '__main__':
    app.run(debug=True)
