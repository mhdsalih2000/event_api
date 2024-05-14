# Event Management Service

## Overview

This project is a RESTful service that manages and queries event data based on a user's geographical location and a specified date. It provides endpoints for data creation and event finding based on user-provided parameters. The service ingests data from a provided CSV dataset containing details of various events, including event names, city names, dates, times, latitudes, and longitudes.

## Tech Stack

- **Backend Framework**: python Django and Django rest framework
- **Database**: postgresql
- **External APIs**: Weather API, Distance Calculation API
- **Deployment**: AWS EC2

## Core Features

1. **Data Creation API**: Allows adding events into the system using details provided in the CSV dataset.
2. **Event Finder API**: Finds events based on the user's latitude, longitude, and a specified date, returning events occurring within the next 14 days from the specified date.

## Design Decisions

- **Choice of Tech Stack**: i chose Django and Django REST Framework for the backend framework. Django provides a robust and scalable framework for building web applications, offering features such as ORM (Object-Relational Mapping) for database interactions, built-in authentication, and a powerful admin interface. Django REST Framework extends Django's capabilities to facilitate the creation of RESTful APIs, providing tools for serialization, authentication, and viewsets for defining API endpoints. We chose Django and Django REST Framework for their extensive documentation, strong community support, and ease of development, making them ideal for building the RESTful service required for this project.

- **Database Design**: For this project, we chose PostgreSQL as the database management system due to its robust features, reliability, and performance. To optimize query performance, we structured the database with the following considerations:

1. **Normalization**: We employed normalization techniques to reduce data redundancy and improve data integrity. This involved organizing data into separate tables and establishing relationships between them using foreign keys.

2. **Indexes**: We created appropriate indexes on columns frequently used in queries, such as latitude, longitude, and date fields. Indexing helps speed up data retrieval by allowing the database engine to quickly locate relevant rows.



- **Error Handling**: Implemented robust error handling for external API failures and other errors, ensuring graceful degradation.

## Installation and Setup

1. **Clone the Repository**: 
   ```bash
   git clone [repository-url]

pip install -r requirements.txt

setup database in settings.py

**Run Command**:
python manage.py makemigrations

python manage.py migrate

python manage.py runserver



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






