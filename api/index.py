import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
