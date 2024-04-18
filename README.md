# Event Management Service

## Overview

This project is a RESTful service that manages and queries event data based on a user's geographical location and a specified date. It provides endpoints for data creation and event finding based on user-provided parameters. The service ingests data from a provided CSV dataset containing details of various events, including event names, city names, dates, times, latitudes, and longitudes.

## Tech Stack

- **Backend Framework**: [Choose your preferred backend framework here]
- **Database**: [Specify the database you chose and why]
- **External APIs**: Weather API, Distance Calculation API
- **Deployment**: [Optional: Mention if you deployed the service and where]

## Core Features

1. **Data Creation API**: Allows adding events into the system using details provided in the CSV dataset.
2. **Event Finder API**: Finds events based on the user's latitude, longitude, and a specified date, returning events occurring within the next 14 days from the specified date.

## Design Decisions

- **Choice of Tech Stack**: We chose [Explain your choice of backend framework, database, etc.]
- **Database Design**: [Explain how you structured your database to optimize query performance]
- **Error Handling**: Implemented robust error handling for external API failures and other errors, ensuring graceful degradation.

## Installation and Setup

1. **Clone the Repository**: `git clone [repository-url]`
2. **Install Dependencies**: `npm install` or `yarn install`
3. **Environment Variables**: Set up environment variables for API keys and other sensitive information.
4. **Run the Service**: `npm start` or `yarn start`

## API Endpoints

### Data Creation API

- **Endpoint**: `POST /events`
- **Request Format**: JSON
- **Response Format**: JSON
- **Example**: `curl -X POST -H "Content-Type: application/json" -d '{"event_name": "EventName", "city_name": "CityName", "date": "YYYY-MM-DD", "time": "HH:MM", "latitude": 40.7128, "longitude": -74.0060}' http://localhost:3000/events`

### Event Finder API

- **Endpoint**: `GET /events/find`
- **Request Format**: Query Parameters: `latitude`, `longitude`, `date`
- **Response Format**: JSON
- **Example**: `curl -X GET "http://localhost:3000/events/find?latitude=40.7128&longitude=-74.0060&date=2024-03-15"`

## Test Case Execution

1. **Input**: User's Source Latitude: 40.7128, User's Source Longitude: -74.0060, Search Date: 2024-03-15
2. **Output**: [Paste the output JSON response here]

## Bonus (Optional)

- **Hosted API**: The API is hosted on [mention hosting platform] at [API URL]
- **Curl Requests**: `curl` requests to test the provided test case input against the hosted API.

## Screenshots (Optional)

- [Include screenshots or screen recordings showing the execution of the provided test case through your API]

## Contributors

- [Your Name]
- [Other contributors if applicable]
