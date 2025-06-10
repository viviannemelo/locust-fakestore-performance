# Performance Testing with Locust - FakeStore API

## 📝 Project Description
This project demonstrates performance testing of a RESTful e-commerce API using [Locust](https://locust.io/). We simulate user behaviors such as browsing products, authenticating, and using the cart feature. The FakeStore API (https://fakestoreapi.com) is used as the testing target.

## 🚀 Tools Used
- Locust
- Faker (data generator)
- Python 3.11+
- GitHub Actions (CI workflow)

## 📌 Test Scenarios
- User registration
- User authentication
- Retrieve all products
- Retrieve a single product
- Add product to cart

## ▶️ How to Run
```bash
pip install -r requirements.txt
locust
```
Visit `http://localhost:8089` and configure number of users and spawn rate.

## 📊 Results
- HTML and CSV reports are available in the `/reports` directory
- Insights include latency, response time, and error rates

## ⚙️ GitHub Actions Workflow
This workflow runs a basic Locust test automatically:

```yaml
name: Locust Performance Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  loadtest:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Locust in headless mode
      run: |
        locust -f locustfile.py --headless -u 20 -r 5 -t 1m --host https://fakestoreapi.com --csv=reports/results

    - name: Upload Locust CSV Results
      uses: actions/upload-artifact@v4
      with:
        name: locust-results
        path: reports/
```