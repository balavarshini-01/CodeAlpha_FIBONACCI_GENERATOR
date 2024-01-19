from flask import Flask, render_template, request
app = Flask(__name__)
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        n = int(request.form['n'])
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        fibonacci_sequence = generate_fibonacci(n)
        return render_template('index.html', n=n, fibonacci_sequence=fibonacci_sequence)
    except ValueError as e:
        return render_template('index.html', error=str(e))
if __name__ == '__main__':
    app.run(debug=True)

