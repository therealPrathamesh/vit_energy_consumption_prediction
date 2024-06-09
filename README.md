# Energy Consumption Prediction for VIT Vellore, Tamil Nadu

This project utilizes Python, FastAPI, HTML5, CSS, and JavaScript to predict future energy consumption by identifying and leveraging trends from past energy consumption data. The application uses data from the past 10 years provided by VIT and implements NeuralProphet to account for anomalies such as COVID-19 while making predictions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Credits](#credits)

## Introduction

This project aims to predict future energy consumption in Vellore, Tamil Nadu, using advanced machine learning techniques. By analyzing past energy consumption data, the application can provide accurate forecasts, even considering anomalies like the COVID-19 pandemic.

## Features

- Predicts future energy consumption.
- Utilizes 10 years of historical data.
- Accounts for anomalies with NeuralProphet.
- Interactive web interface using HTML5, CSS, and JavaScript.
- Backend powered by FastAPI.

## Installation

### Prerequisites

- Python 3.x
- FastAPI
- NeuralProphet
- HTML5, CSS, JavaScript

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/energy-consumption-prediction.git
    cd energy-consumption-prediction
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

4. Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Launch the web application by following the installation steps.
2. Enter the required details to view energy consumption predictions.
3. The application will process the data and display the predicted energy consumption trends.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out:

- GitHub: [therealPrathamesh](https://github.com/therealPrathamesh)

## Credits

- Developed by [Prathamesh Prabhu](https://github.com/therealPrathamesh)
- Data provided by VIT
- Used libraries and frameworks: NeuralProphet, FastAPI, HTML5, CSS, JavaScript
