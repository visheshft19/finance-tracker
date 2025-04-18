from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Storing transactions in memory for now (temporary, non-persistent)
transactions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transactions', methods=['GET', 'POST'])
def transactions_page():
    if request.method == 'POST':
        # Collecting form data
        description = request.form['description']
        amount = float(request.form['amount'])
        category = request.form['category']
        transactions.append({
            'description': description,
            'amount': amount,
            'category': category
        })
        return redirect(url_for('transactions_page'))
    
    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
