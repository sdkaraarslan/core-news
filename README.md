# core-news

This project is a keyword generator which uses the Guardian API to fetch top news of a chosen date and generates relevant keywords and images. It's built with FastAPI, React, Python, and Tailwind CSS, and it's containerized using Docker.

## Installation

Follow these steps to install and run the project:

1. Clone the repository:
    ```
    git clone https://github.com/sdkaraarslan/core-news.git
    ```
2. Navigate to the project directory:
    ```
    cd core-news
    ```
3. Build the Docker image:
    ```
    docker build -t core-news .
    ```
4. Run the Docker container:
    ```
    docker run -d -p 8000:8000 core-news
    ```

The application should now be running at `http://localhost:8000`.

## Usage

To use the keyword generator, navigate to `http://localhost:8000` in your web browser. Enter a date, and the application will fetch the top news for that date from the Guardian API and generate relevant keywords and images.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.