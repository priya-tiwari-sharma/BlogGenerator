# Blog Title and Content Generator

This project is a Django-based web application that helps generate blog titles, content, and accompanying images using OpenAI's GPT-3.5 and DALL-E models. The application is designed to assist content creators, particularly those working in the IT industry, by generating tailored titles, detailed blog content, and relevant images.

## Features

- **Blog Title Generator:** Generate a creative and relevant blog title based on user input keywords.
- **Content Generator:** Create detailed blog content tailored for IT professionals, focusing on specific technical topics.
- **Image Generator:** Generate an informative and visually appealing image to complement the blog content.

## Technologies Used

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework:** A powerful toolkit for building Web APIs.
- **OpenAI API:** Utilized for generating text and images through GPT-3.5 and DALL-E models.
- **Python-dotenv:** A Python library for loading environment variables from a `.env` file.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/blog-generator.git
    cd blog-generator
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key:
      ```plaintext
      OPENAI_API_KEY=your-openai-api-key
      ```

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Blog Title Generation:**
   - Navigate to `/generate-title/` and fill out the form with your area of work and keywords.
   - Click the "Generate Title" button to receive a tailored blog title.

2. **Content Generation:**
   - After generating a title, navigate to `/generate-content/` and input the area of work, keywords, and generated title.
   - Click "Generate Content" to receive a detailed blog post.

3. **Image Generation:**
   - Navigate to `/generate-image/` after generating content, input the keywords, and generated title.
   - Click "Generate Image" to receive an image that complements the blog content.

## Project Structure

- **BlogApp:** Contains the views, forms, and templates for generating titles, content, and images.
- **static:** Stores static files like CSS, JS, and images.
- **templates:** HTML templates for rendering the forms and displaying results.
- **.env:** Environment variables for secret keys and API keys (not included in the repository).

## Future Enhancements

- Implement user authentication to save and manage generated blogs.
- Add more customization options for generated content and images.
- Enhance the UI/UX for better user interaction.
