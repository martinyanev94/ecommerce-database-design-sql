# Final Project: Database Design and Implementation

## Overview

This project aims to encourage students to apply their knowledge of database design and implementation using PostgreSQL and MySQL. Students will create a functional database system for a fictional e-commerce platform, demonstrating their understanding of key concepts discussed in the course.

## Project Objectives

1. **Database Design**: Create an Entity-Relationship Diagram (ERD) that represents the database schema for the e-commerce platform.
2. **Implementation**: Build the database using SQL commands on either PostgreSQL or MySQL.
3. **Testing and Validation**: Populate the database with sample data and perform various queries to ensure the system works as intended.
4. **Documentation**: Document the design and implementation process, providing insights into the decisions made during development.

## Project Steps

### 1. Define Requirements

- Develop a list of entities relevant to the e-commerce platform:
  - Users (customers/admins)
  - Products
  - Orders
  - Categories
  - Reviews

### 2. Create an Entity-Relationship Diagram (ERD)

- Identify and define the attributes for each entity. For instance:
  - **User**: UserID, UserName, Email, Password, ContactNumber
  - **Product**: ProductID, ProductName, Price, Description, CategoryID
  - **Order**: OrderID, UserID, OrderDate, TotalAmount
  - **Category**: CategoryID, CategoryName
  - **Review**: ReviewID, UserID, ProductID, Rating, Comment

- Illustrate the relationships between entities:
  - One-to-Many: One user can place many orders.
  - Many-to-One: Many products can belong to one category.
  - Many-to-Many: Users can review many products.

### 3. Build Database Schema

Use the SQL commands to create the necessary tables, ensuring proper normalization (1NF, 2NF, 3NF). An example command for creating the Users table is:

```sql
CREATE TABLE Users (
    UserID BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    UserName VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(255),
    ContactNumber VARCHAR(15)
);
```

### 4. Populate the Database

Insert sample data into the tables to simulate a functioning e-commerce system. Provide SQL commands for inserting data such as:

```sql
INSERT INTO Users (UserName, Email, Password, ContactNumber) VALUES
('JohnDoe', 'john@example.com', 'securepassword', '+1234567890'),
('JaneSmith', 'jane@example.com', 'anotherpassword', '+0987654321');
```

### 5. Query the Database

Develop SQL queries to extract meaningful insights from the database:
- Retrieve all products within a specific category.
- List all orders made by a user.
- Calculate the average rating for each product.

### 6. Documentation

Create comprehensive documentation that includes:
- Overview of entities and attributes.
- ERD and explanations of relationships.
- SQL scripts used for creating and populating the database.
- Examples of queries and the output they produce.

### 7. Presentation

Prepare a presentation summarizing the project including:
- Design choices and normalization process.
- Challenges faced during implementation and how they were overcome.
- Lessons learned from the project.

## Assessment Criteria

- Completeness of database schema and ERD.
- Correctness of SQL syntax and functionality of queries.
- Clarity and thoroughness of documentation.
- Overall presentation and explanation of the project.

## Submission

Students are required to submit the following by the deadline:
- ERD diagram (in a supported format like PNG, JPEG, or PDF).
- SQL scripts used to create and populate the database.
- Project documentation.
- Presentation slides.

---

This project will consolidate your learning and prepare you to tackle real-world database design challenges successfully.