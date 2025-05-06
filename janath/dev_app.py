# Development Environment URL Redirects (Python)
from flask import Flask, redirect

app = Flask(__name__)

# Dev Redirect Rules
@app.route('/login')
def dev_login_redirect():
    return redirect('https://dev-auth.example.com/signin', code=302)

@app.route('/dashboard')
def dev_dashboard_redirect():
    return redirect('https://dev-app.example.com/home', code=302)

@app.route('/api/v1')
def dev_api_redirect():
    return redirect('https://dev-api.example.com/v1', code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Dev server runs on port 5000
