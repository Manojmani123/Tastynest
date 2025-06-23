# Divya Kitchen

Divya Kitchen is a Django project designed to provide a platform for sharing recipes and cooking tips. This README file contains information on how to set up and run the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Divya-Kitchen.git
   cd Divya-Kitchen
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`. You can navigate through the different pages to explore recipes and cooking tips.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.