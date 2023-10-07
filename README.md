# Med-aphor ⚕️🏥

An application that crawls the web to bring you the latest at home remedies, treatments and need-to-know information for any medical issues. 

### Powered by [Metaphor API](https://metaphor.systems) and [OpenAI](https://openai.com)

***This is not medical advice, information provided is purely from the public web***

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Project Overview

Med-aphor was inspired by my interest in holistic medicine and goal of taking care of my body. I found myself constantly scouring the web for hours, looking at remedies for certain ailments from fatigue to insomnia to a simple cold and flu. I love learning about at-home remedies and my health is my top priority. Thanks to the wonderful Metaphor API and help of OpenAI's API, I was able to streamline this process and view in-depth summaries and reccomendations from the latest medical journals with a single button and prompt.

## Directory Structure

Here's a brief overview of the project's directory structure:

- **frontend**: Contains the frontend application.
- **backend**: Houses the backend server and data logic.
  - **data**: Comprehensive dataset of diseases

## Installation

This project was built by **Flask**, **Pandas** and **React**

To set up Med-aphor on your local development environment, follow these steps:

1. Clone the repository to your machine:

   ```bash
   git clone https://github.com/your-username/med-aphor.git

2. **Frontend Setup:**

    - Go to the frontend directory:

        ```bash
        cd frontend
        ```

    - Install frontend dependencies:

        ```bash
        npm install
        ```

### Backend Setup

1. **Backend Setup:**

    - Go to the backend directory:

        ```bash
        cd backend
        ```

    - Install backend dependencies (if necessary):

        ```bash
        pip install -r requirements.txt
        ```

2. Configure environment variables, including API keys and database settings, as needed.
```
OPENAI_API_KEY = " "
METAPHOR_API_KEY = " "
```

## Usage

### Running the App

You can run Med-aphor as follows:

- **Frontend:**

    Start the frontend development server:

    ```bash
    npm run dev
    ```

- **Backend:**

    Start the backend server:

    ```bash
    flask --app server run
    ```

## Features

The creation of Med-aphor includes

- Elegant React frontend with HTML forms, animations, and HTTP transactions
- Raw data cleaning and wrangling of disease information to filter nonsensical inputs
- Dual integration of Metaphor API and OpenAI API
- Robust error & exception checking across http requests and web-scraping calls

## Med-aphor in action


https://github.com/anabi77498/med-aphor/assets/104233184/e41fe3e6-18d5-440f-bfe2-54293eb1720e



