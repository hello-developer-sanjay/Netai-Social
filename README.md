# Netai-Social

Netai-Social is a social media application built with Flask, React, and MongoDB. It includes sentiment analysis and emotion detection features using natural language processing (NLP) models.

## Features

- **Sentiment Analysis**: Analyze the sentiment of messages posted on the platform.
- **Emotion Detection**: Detect emotions in messages, providing a more nuanced understanding of user content.
- **User-Friendly Interface**: Intuitive UI/UX for seamless user experience.
- **Real-time Updates**: Messages and sentiments are updated in real-time for dynamic user interaction.
- **Responsive Design**: Mobile-friendly design ensures accessibility on various devices.

## Technologies Used

- **Backend**: Flask, MongoDB, Transformers library (Hugging Face)
- **Frontend**: React, Axios for API requests
- **NLP Models**: DistilBERT for sentiment analysis and emotion detection
- **Deployment**: Render for hosting the application, GitHub Actions for CI/CD

## Getting Started

1. Clone the repository: `git clone https://github.com/hello-developer-sanjay/netai-social.git`
2. Install dependencies: `pip install -r requirements.txt` for the backend, `npm install` for the frontend.
3. Set up environment variables: Create a `.env` file and define your MongoDB URI and other sensitive information.
4. Run the backend: `python app.py`
5. Run the frontend: `npm start`

## Deployment

The application is automatically deployed on [Render](https://render.com/) upon pushing to the `main` branch. GitHub Actions handle the deployment process, ensuring continuous integration and delivery.

## Folder Structure

- **`/server`**: Backend Flask application.
  - **`/config`**: Database configuration files.
  - **`/models`**: Data models and logic.
  - **`/routes`**: API endpoints.
- **`/client`**: Frontend React application.
  - **`/src`**: React components and styles.

## Contributions

Contributions are welcome! Feel free to open issues or create pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
