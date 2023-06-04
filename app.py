from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola! Sam.... You created a Flask app in a Docker container!'

@app.route('/about')
def about():
    return 'I am Sam Prince Franklin, a DevOps engineer with expertise in cloud computing, CI/CD, and infrastructure automation.'

@app.route('/skills')
def skills():
    return 'My skills include Docker, Kubernetes, Jenkins, AWS, Azure, Git, and Ansible.'

@app.route('/experience')
def experience():
    return 'I have worked on various projects implementing DevOps practices to streamline software delivery and improve scalability.'

@app.route('/education')
def education():
    return 'I hold a Bachelor\'s degree in Computer Science and have pursued certifications in DevOps and cloud technologies.'

if __name__ == '__main__':
    app.run()
